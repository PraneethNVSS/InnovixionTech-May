import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a random number between 1 and 100.")
    print("You have 7 attempts to guess it correctly.")
    secret_number = random.randint(1, 100)

    # Initialize the number of attempts
    attempts = 0

    while attempts < 7:
        try:
            # Get user's guess
            guess = int(input("\nEnter your guess: "))

            # Increment the number of attempts
            attempts += 1

            # Check if the guess is correct
            if guess == secret_number:
                print("Congratulations! You guessed it right!")
                break
            elif guess < secret_number:
                print("Try a higher number.")
            else:
                print("Try a lower number.")

            # Display remaining attempts
            print("Attempts left:", 7 - attempts)

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    else:
        print("\nSorry, you've run out of attempts!")
        print("The correct number was:", secret_number)

# Run the game
number_guessing_game()