import random
print("Hello, World!")
num = random.randint(1, 10)
print(f"The random number is: {num}")


userGuess = input("Press Enter to continue...")
userGuess = int(userGuess)

if userGuess == num:
    print("Congratulations! You guessed the number.")
else:
    while userGuess != num:
        print(f"Your guess is: {userGuess}, the number is: {num}")
        userGuess = int(input("Press Enter to continue..."))
        if userGuess == num:
            print("Congratulations! You guessed the number.")
            break
print(userGuess)