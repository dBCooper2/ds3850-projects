import random

# ANSI escape codes for colors
COLORS = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'purple': '\033[95m',
    'reset': '\033[0m'  # Reset color to default
}

def red_text(text):
    """Return text formatted in red color"""
    return f"{COLORS['red']}{text}{COLORS['reset']}"

def green_text(text):
    """Return text formatted in green color"""
    return f"{COLORS['green']}{text}{COLORS['reset']}"

def yellow_text(text):
    """Return text formatted in yellow color"""
    return f"{COLORS['yellow']}{text}{COLORS['reset']}"

def blue_text(text):
    """Return text formatted in blue color"""
    return f"{COLORS['blue']}{text}{COLORS['reset']}"

def purple_text(text):
    """Return text formatted in purple color"""
    return f"{COLORS['purple']}{text}{COLORS['reset']}"

def random_color_text(text):
    """Return text formatted in a random color"""
    color = random.choice(list(COLORS.keys())[:-1])  # Exclude 'reset' from choices
    return f"{COLORS[color]}{text}{COLORS['reset']}"

def print_color_menu():
    """Display the available color options"""
    print("\nAvailable colors:")
    print("1. Red")
    print("2. Green")
    print("3. Yellow")
    print("4. Blue")
    print("5. Purple")
    print("6. Random")
    print("7. Custom ANSI code")
    print("8. Exit")

def custom_color_text(text, color_code):
    """Return text formatted with a custom ANSI color code"""
    return f"\033[{color_code}m{text}{COLORS['reset']}"

def get_valid_choice():
    """Get and validate user's color choice"""
    while True:
        try:
            choice = int(input("\nEnter your color choice (1-8): "))
            if 1 <= choice <= 8:
                return choice
            print("Please enter a number between 1 and 8.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    """Main function to run the colorful text program"""
    print("\nWelcome to the Colorful Text Generator!")
    print("====================================")
    
    # Dictionary mapping choices to color functions
    color_functions = {
        1: red_text,
        2: green_text,
        3: yellow_text,
        4: blue_text,
        5: purple_text,
        6: random_color_text
    }
    
    while True:
        print_color_menu()
        choice = get_valid_choice()
        
        if choice == 8:
            print("\nThanks for using the Colorful Text Generator!")
            print("=========================================")
            break
            
        text = input("\nEnter the text you want to color: ")
        
        if choice == 7:
            # Handle custom ANSI code
            try:
                code = input("Enter custom ANSI color code (e.g., 95 for purple): ")
                result = custom_color_text(text, code)
            except Exception as e:
                print(f"Error with custom color code: {e}")
                continue
        else:
            # Use predefined color functions
            result = color_functions[choice](text)
        
        print("\nHere's your colored text:")
        print(result)
        print()  # Empty line for better readability

if __name__ == "__main__":
    main()