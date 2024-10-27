import random
import time  # For the extra practice feature of adding delays

def generate_white_ball():
    """
    Generates a random number for white balls (1-69)
    """
    return random.randint(1, 69)

def generate_red_ball():
    """
    Generates a random number for the red PowerBall (1-26)
    """
    return random.randint(1, 26)

def display_numbers(numbers, with_delay=False):
    """
    Displays the PowerBall numbers with proper formatting
    Optional delay parameter for extra practice feature
    """
    # Display white balls with one space between them
    for i in range(5):
        print(str(numbers[i]), end=" ")
        if with_delay:
            time.sleep(1)  # 1 second delay between numbers
    
    # Display red ball with three spaces before it
    print("  " + str(numbers[5]))
    
def generate_powerball_numbers():
    """
    Generates a complete set of PowerBall numbers:
    5 white balls (1-69) and 1 red ball (1-26)
    """
    # Generate 5 unique white balls
    white_balls = []
    while len(white_balls) < 5:
        number = generate_white_ball()
        if number not in white_balls:  # Ensure numbers are unique
            white_balls.append(number)
    
    # Generate red ball
    red_ball = generate_red_ball()
    
    return white_balls + [red_ball]

def main():
    """
    Main function to run the PowerBall number generator
    """
    # Greeting
    print("\nWelcome to the PowerBall Number Generator!")
    print("==========================================")
    print("\nGenerating your lucky numbers...")
    print()
    
    # Generate and display numbers
    numbers = generate_powerball_numbers()
    display_numbers(numbers, with_delay=True)  # Set to True for the delay feature
    
    # Farewell message
    print("\nGood luck with your PowerBall ticket!")
    print("=====================================")

if __name__ == "__main__":
    main()