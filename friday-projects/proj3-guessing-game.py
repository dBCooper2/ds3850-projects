import random

def get_user_choice():
    """
    Gets user's choice to play the game
    Returns True if user wants to play, False otherwise
    """
    while True:
        choice = input("\nWould you like to play the number guessing game? (yes/no): ").lower().strip()
        if choice in ['yes', 'y']:
            return True
        elif choice in ['no', 'n']:
            return False
        else:
            print("Please enter 'yes' or 'no'.")

def get_valid_guess():
    """
    Gets and validates user's number guess
    Returns the validated guess as an integer
    """
    while True:
        try:
            guess = int(input("\nGuess a number between 1 and 10: "))
            if 1 <= guess <= 10:
                return guess
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Please enter a valid number.")

def play_game():
    """
    Main game logic for the number guessing game
    """
    # Generate random number between 1 and 10
    secret_number = random.randint(1, 10)
    attempts = 0

    while True:
        # Get user's guess
        guess = get_valid_guess()
        attempts += 1

        # Check if guess is correct
        if guess == secret_number:
            print("\nCongratulations! You've guessed the number!")
            print(f"It took you {attempts} attempts.")
            break
        else:
            # Provide hints
            if guess < secret_number:
                print("Too low! Try again!")
            else:
                print("Too high! Try again!")

def main():
    """
    Main function to run the number guessing game
    """
    print("\nWelcome to the Number Guessing Game!")
    print("===================================")

    if get_user_choice():
        play_game()
    else:
        print("\nMaybe next time!")
        
    print("\nThanks for playing! Goodbye!")
    print("===========================")

if __name__ == "__main__":
    main()