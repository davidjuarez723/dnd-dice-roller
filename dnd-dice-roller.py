import random
from unittest import result

def roll_dice(sides):
    return random.randint(1,sides)

def main():
    dice_options = {
        '4': 4,
        '6': 6,
        '8': 8,
        '10': 10,
        '12': 12,
        '20': 20
    }

    print("Welcome to the DnD Dice Rolling Application!")

    while True:
        dice = input("Please enter the type of dice you want to role (4, 6, 8, 10, 12, 20) or 'q' to quit: ")

        if dice == 'q':
            print("Thank you for using the DnD Dice Rolling Application. Goodbye!")
            break

        if dice not in dice_options:
            print("Invalid dice selection. Please try again.")
            continue

        sides = dice_options[dice]
        result = roll_dice(sides)
        print(f"You rolled a {result} on a {sides}-sided dice.")

if __name__ == "__main__":
    main()