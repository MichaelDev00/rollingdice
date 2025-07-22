from random import Random

roll = Random()
wrong_guesses = 0

while wrong_guesses < 5:
    ui = input("Gamble something:(y/n) ")

    if ui == "y":
        numbers = roll.sample((1, 2, 3, 4, 5), 2)
        print(numbers)
    elif ui == "n":
        print("Thank you for gambling!")
    else:
        wrong_guesses += 1
        print(f"Invalid input {5 - wrong_guesses} attempts left.")

print("Gambling over! Too many wrong attempts.")
