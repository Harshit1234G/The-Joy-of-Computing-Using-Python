from string import ascii_letters
import random

def dobble_game() -> None:

    letters = list(ascii_letters)

    common_letter = random.choice(letters)
    letters.remove(common_letter)
    index1, index2 = random.randint(0,4), random.randint(0, 4)

    word1 = random.sample(letters, 5)

    for letter in word1:
        letters.remove(letter)

    word2 = random.sample(letters, 5)

    word1[index1] = common_letter
    word2[index2] = common_letter

    print(f"Dobble Game.\nFind the similar letter.\n1. {''.join(word1)}\t2.{''.join(word2)}")
    ans = input("Enter the similar word: ")
    if ans == common_letter:
        print("You won!")
    else:
        print("You lose!")

dobble_game()