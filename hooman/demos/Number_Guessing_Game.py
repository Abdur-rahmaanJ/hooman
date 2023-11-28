import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    attempts = 0
    max_attempts = 6

    while attempts < max_attempts:
        try:
            # Get user input
            user_guess = int(input("Enter your guess: "))

            # Increment the number of attempts
            attempts += 1

            # Check if the guess is correct
            if user_guess == secret_number:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
            elif user_guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Please enter a valid number.")

    if user_guess != secret_number:
        print(f"Sorry, you're out of attempts. The correct number was {secret_number}.")

if __name__ == "__main__":
    number_guessing_game()
