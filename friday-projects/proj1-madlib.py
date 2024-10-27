def get_user_input(prompt):
    """
    Helper function to get user input with proper formatting and error handling
    """
    while True:
        user_input = input(prompt).strip()
        if user_input:  # Ensure input is not empty
            return user_input
        print("Please enter a valid response.")

def collect_words():
    """
    Collect all required words from the user with clear instructions
    """
    print("\nWelcome to Mad Libs! Please provide the following words to create your story:")
    print("(Press Enter after each word)\n")
    
    # Dictionary to store all user inputs
    words = {
        'large_object': get_user_input("Enter a large object: "),
        'large_objects_plural': get_user_input("Enter large objects (plural): "),
        'adjective': get_user_input("Enter an adjective: "),
        'body_part': get_user_input("Enter a body part: "),
        'restaurant': get_user_input("Enter a restaurant name: "),
        'food1': get_user_input("Enter a food: "),
        'food2': get_user_input("Enter another food: ")
    }
    
    return words

def create_story(words):
    """
    Generate the story using the collected words
    """
    story = f"""
I've had a very {words['adjective']} day.
This morning, I dropped a box of {words['large_objects_plural']} on my {words['body_part']}.
Then, at lunch, I went to {words['restaurant']} for their delicious {words['food1']},
But the waiter brought me {words['food2']}, which I was not hungry for.
Finally, on my way home, I was cut off by a van with a large {words['large_object']} strapped to the roof.
"""
    return story

def main():
    """
    Main function to run the Mad Libs game
    """
    print("Welcome to Mad Libs Story Generator!")
    print("====================================")
    
    # Collect words from user
    words = collect_words()
    
    # Generate and display the story
    print("\nHere's your Mad Libs story:")
    print("===========================")
    story = create_story(words)
    print(story)

if __name__ == "__main__":
    main()