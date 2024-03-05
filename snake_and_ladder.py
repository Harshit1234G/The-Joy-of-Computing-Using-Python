import random

def dice() -> int:
    return random.randint(1, 6)

def game(player: str, score: int) -> int:

    ladders = {
        4: 14,
        9: 31,
        21: 42,
        51: 67,
        28: 84,
        80: 99,
        72: 91
    }

    snakes = {
        17: 7,
        54: 34,
        64: 60,
        79: 19,
        87: 36,
        98: 79,
        93: 73,
        94: 75
    }

    print(f"{player}'s turn:")

    dice_value = dice()
    print(f"Dice shows: {dice_value}")

    print(f"Current position: {score}")

    if score + dice_value > 100:
        print("Sorry! the dice value is greater than you needed. Better luck in next chance.\n")
        input("Press any key to continue...\n")
        return score
    
    score += dice_value
    print(f"After move: {score}")

    if score in ladders.keys():
        print("Its a ladder, Woo-Hoo!\nAscending the ladder.\nYour position now:", score := ladders[score])
    
    elif score in snakes.keys():
        print("Oh! its a snake, You are down.\nYour position now:", score := snakes[score])

    elif score == 100:
        print(f"Congratulations! {player}, You won the game.")

    print()
    input("Press any key to continue...\n")
    
    if dice_value == 6:
        print("Here's your another chance as you got 6\n")
        score = game(player, score)

    return score

if __name__ == '__main__':
    player1 = input("Player1, Enter your name: ")
    player2 = input("Player2, Enter your name: ")

    player1_score, player2_score = 0, 0

    while True:
        player1_score = game(player1, player1_score)

        if player1_score == 100:
            break

        player2_score = game(player2, player2_score)

        if player2_score == 100:
            break