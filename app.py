import random

RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'
random_number = random.randint(1, 10)
guesses = 0
while True:
    user_number = input("Guess a number between 1 and 10: ")
    try:
        user_number = int(user_number)
        guesses += 1
        if user_number == random_number:
            print(f"{GREEN}Congratulations! You guessed the number in {guesses} guesses.{RESET}")
            break
        elif user_number < 1 or user_number > 10:
            print(f"{RED}Please enter a number between 1 and 10.{RESET}")
        else:
            print(f"{RED}Sorry, that's not the number.{RESET}")
    except ValueError:
        print(f"{RED}Enter a valid number.{RESET}")
        