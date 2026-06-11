import random
num = random.randint(1, 10)

userGuess = input("Guess a number between 1 and 10: ")
userGuess = int(userGuess)

if userGuess == num:
    print("Congratulations! You guessed the number.")
else:
    while userGuess != num:
        print("Sorry, that's not the number.")
        userGuess = int(input("Guess a number between 1 and 10: "))
        if userGuess == num:
            print("Congratulations! You guessed the number.")
            break