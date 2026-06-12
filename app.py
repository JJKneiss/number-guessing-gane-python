import random

randomNumber = random.randint(1, 10)

while True:
    userGuess = input("Guess a number between 1 and 10: ")
    try:
        userNumber = int(userGuess)
        break
    except ValueError:
        print("Enter a valid number.")

if userNumber == randomNumber:
    print("Congratulations! You guessed the number.")
else:
    while userGuess != randomNumber:
        print("Sorry, that's not the number.")
        userGuess = int(input("Guess a number between 1 and 10: "))
        if userGuess == randomNumber:
            print("Congratulations! You guessed the number.")
            break