player1 = {
    0: 'rock',
    2: 'paper',
    1: 'scissors',
}

player2 = {
    0: 'scissors',
    1: 'paper',
    2: 'rock',
}

def game(code1: str, code2: str, index1: int, index2: int) -> None:
    p1 = int(code1[index1]) % 3
    p2 = int(code2[index2]) % 3

    print(f"Player1 chooses: {player1[p1]}\nPlayer2 chooses: {player2[p2]}")

    if player1[p1] == player2[p2]:
        print("Its a Draw!")

    elif player1[p1] == 'rock':
        if player2[p2] == 'paper':
            winner = "Player2"
        else:
            winner = "Player1"

    elif player1[p1] == 'paper':
        if player2[p2] == 'scissor':
            winner = "Player2"
        else:
            winner = "Player1"

    elif player1[p1] == 'scissors':
        if player2[p2] == 'rock':
            winner = "Player2"
        else:
            winner = "Player1"

    print(f"{winner} wins this game!")

while True:
    code1 = input("Player1, Enter your code: ")
    code2 = input("Player2, Enter your code: ")

    index1 = int(input("Player1, Enter index where your choice: "))
    index2 = int(input("Player2, Enter index where your choice: "))

    game(code1, code2, index1, index2)

    ch = input("Do you want to play more (y/n): ").lower()
    if ch != 'y':
        break