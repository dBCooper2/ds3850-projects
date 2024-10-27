# ds3850-projects

A collection of Python projects demonstrating various programming concepts and implementations.

## Project 1: Madlib
An interactive Mad Libs game that collects words from users and inserts them into a story template.

### Features
- Input validation to ensure no empty responses
- Clear user instructions
- Organized code structure with separate functions
- Story template with multiple word insertions

### Technical Details
- Uses functions for organized code:
  - `get_user_input()`: Handles word collection with validation
  - `collect_words()`: Manages all required word collection
  - `create_story()`: Generates final story using collected words
  - `main()`: Orchestrates program flow

## Project 2: Powerball Number Generator
Generates random numbers for PowerBall lottery tickets with proper formatting and optional time delays between numbers.

### Features
- Generates 5 unique random numbers for white balls (1-69)
- Generates 1 random number for the red PowerBall (1-26)
- Proper spacing between numbers
- Optional time delay between displaying numbers
- Clear user interface with welcome and farewell messages

### Technical Details
- Uses Python's random module for number generation
- Implements number uniqueness check for white balls
- Optional time delay feature using time module
- Proper spacing implementation

## Project 3: Number Guessing Game
An interactive game where users try to guess a random number between 1 and 10.

### Features
- Random number generation
- Input validation for user responses
- Feedback system ("too high" or "too low")
- Attempt counter
- User-friendly interface

### Technical Details
- Uses functions for organized code:
  - `get_user_choice()`: Handles play/no-play decision
  - `get_valid_guess()`: Validates number guesses
  - `play_game()`: Contains main game logic
- Includes error handling for invalid inputs

## Project 4: Quiz Bowl
A quiz program that presents questions, accepts answers, and provides feedback with scoring.

### Features
- Dictionary-based question storage
- Randomized question order
- Case-insensitive answer checking
- Score tracking and percentage calculation
- Performance feedback
- Clear user interface with question numbering

### Technical Details
- Uses dictionary data structure for question/answer pairs
- Implements question randomization
- Calculates and displays performance statistics
- Includes case-insensitive answer checking

## Project 5: Colorful Text Functions
A text colorizer program that can display text in various colors using ANSI escape codes.

### Features
- Five predefined color functions
- Random color function
- Custom ANSI color code support
- Interactive menu system
- Input validation
- Continuous operation until user exits

### Technical Details
- Uses ANSI escape codes for color implementation
- Includes functions for each color option
- Supports custom color code input
- Error handling for invalid inputs

## Project 6: Bank Account
A banking system simulation using object-oriented programming that manages account operations.

### Features
- Object-oriented design with BankAccount class
- Account number verification
- Three main operations:
  - Deposit money
  - Withdraw money
  - Check balance
- Input validation
- Transaction feedback

### Technical Details
- BankAccount class with attributes:
  - account_number
  - balance
- Methods:
  - deposit()
  - withdraw()
  - check_balance()
- Input validation for all user inputs
- Proper decimal handling for monetary values

## Getting Started
Each project can be run independently. Navigate to the project directory and run the Python file:

```bash
python project_name.py
```

### This project was generated using Anthropic's Claude 3.5 Sonnet AI. 