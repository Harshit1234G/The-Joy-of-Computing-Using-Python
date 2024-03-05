import random

def jumbled_word(length: int) -> str:
    word = random.choice(words[length])
    words[length].remove(word)

    jumble_word = list(word)
    random.shuffle(jumble_word)
    return ''.join(jumble_word), word

def game(jumble_word: tuple, player: str, score: int) -> int:
    print(f"{player}'s turn:\nGuess the jumbled word: {jumble_word[0]}")
    player_guess = input("Enter your guess (You will only get one chance): ")

    if player_guess == jumble_word[1]:
        print("You guessed it right!")
        score += 1
        return score
    print("You guessed it wrong!")
    return -1

if __name__ == '__main__':
    words = [
        "apple", "banana", "chocolate", "elephant", "fluffy", "guitar", "happiness","islands", "jazz", "kangaroo", "lemon", "moon", "notebook", "ocean", "penguin","rainbow", "sunflower", "tiger", "umbrella", "violin", "watermelon", "xylophone", "yogurt","zebra", "airplane", "butterfly", "dolphin", "elephant", "fireworks","giraffe", "honey", "jellyfish", "kite", "lighthouse", "mango", "night","octopus", "parrot", "queen", "rain", "sailboat", "tulip", "unicorn", "volcano", "whale","xylophone", "zeppelin", "acorn", "butter", "cactus", "daisy", "eggplant", "feather","grape", "hedgehog", "iceberg", "jackal", "kiwi", "leopard", "mushroom", "narwhal", "ostrich","peacock", "quokka", "raccoon", "starfish", "toucan", "umbrella", "violet", "walrus", "xylophone","yarn", "zebra", "alpaca", "bison", "cheetah", "dandelion", "eagle", "giraffe", "hyena","iguana", "jaguar", "koala", "lemur", "meerkat", "otter", "panda", "quokka", "seahorse", "tiger", "unicorn", "vulture", "wombat", "zebra"
    ]

    words = {length : [word for word in words if len(word) == length] for length in set(map(len, words))}

    player1 = input("Enter player1's name:")
    player2 = input("Enter player2's name:")

    player1_score = 0
    player2_score = 0

    while True:
        length = random.choice(list(words.keys()))

        player1_score = game(jumbled_word(length), player1, player1_score)
        player2_score = game(jumbled_word(length), player2, player2_score)

        if player1_score > player2_score:
            print(f"{player1} wins by the score of {player1_score}")
            break
        elif player2_score > player1_score:
            print(f"{player2} wins by the score of {player2_score}")
            break

        elif player2_score == -1 and player1_score == -1:
            print("The match is a draw!")
            break
