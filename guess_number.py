number = 10
max_guesses = 5
guess_count = 0

print("I'm thinking of a number...")

while guess_count < max_guesses:
    guess = input("What number am I thinking of? Type 'q' to quit. ")

    if guess.lower() == 'q':
        print(f"The number was {number}.")
        break

    try:
        guess = int(guess)
        guess_count += 1
        if guess == number:
            print("Congratulations! You guessed the right number.")
            break
        elif guess < number:
            print("Sorry! Your guess was too low.")
        else:
            print("Sorry! Your guess was too high.")
        print(f"You have {max_guesses - guess_count} guesses left.")
    except ValueError:
        print("Please enter a valid number or 'q' to quit.")

if guess_count == max_guesses:
    print(f"Sorry, you've used all your {max_guesses} guesses. The number was {number}.")
