number = 10

print("I'm thinking of a number...")

while True:
    guess = input("What number am I thinking of? Type 'q' to quit. ")

    if guess.lower() == 'q':
        print(f"The number was {number}.")
        break

    try:
        guess = int(guess)
        if guess == number:
            print("Congratulations! You guessed the right number.")
            break
        elif guess < number:
            print("Sorry! Your guess was too low. Try again.")
        else:
            print("Sorry! Your guess was too high. Try again.")
    except ValueError:
        print("Please enter a valid number or 'q' to quit.")
