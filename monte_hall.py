import random

win_swap, win_dont_swap = 0,0

for _ in range(10):
    door = [0, 0, 0]
    goat_door = []

    door[x:= random.randint(0,2)] = 'BMW'

    for i in range(3):
        if i == x:
            continue
        
        else:
            door[i] = 'goat'
            goat_door.append(i)

    choice = int(input("Enter your choice: "))
    door_open = random.choice(goat_door)

    while choice == door_open:
        door_open = random.choice(goat_door)

    door.pop(door_open)

    print(f"Door opened: {door_open}, it is a goat!")

    swap = input(f"Your current choice {choice}, Do you want to swap or be on your choice (y/n): ").lower()
    if swap == 'y':
        choice = [d for d in door if d != choice][0]

    print(f"Opening the door: '{choice}'")

    if choice == 'BMW':
        print("You won")
        if swap == 'y':
            win_swap += 1
        else:
            win_dont_swap += 1

    else:
        print("You lose")

print(f"{win_swap=}\t{win_dont_swap=}")