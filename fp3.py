# Importing the random module to generate a secret number
import random

# Function for the number guessing game
def number_guessing_game():
    # Greeting the user
    play_game = input("Welcome! Would you like to play the number guessing game? (yes/no): ").lower()

    if play_game == 'no':
        # If the user says no, print a farewell message and exit
        print("Maybe next time!")
        return
    elif play_game == 'yes':
        # If the user says yes, proceed with the game
        secret_number = random.randint(1, 10)  # Generate a secret number between 1 and 10

        # Loop until the user guesses correctly
        while True:
            guess = int(input("Guess a number between 1 and 10: "))

            if guess == secret_number:
                # If the guess is correct, congratulate the user and exit the loop
                print("Congratulations! You've guessed the number!")
                break
            else:
                # If the guess is incorrect, ask the user to try again
                print("Try again!")

    # Farewell message after the game ends
    print("Thanks for playing! Goodbye!")

# Calling the function to start the game
number_guessing_game()