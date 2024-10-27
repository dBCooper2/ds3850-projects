import random

def create_quiz_questions():
    """
    Creates and returns a dictionary of quiz questions and answers
    """
    quiz_questions = {
        "What is the capital of France?": "paris",
        "Which planet is known as the Red Planet?": "mars",
        "What is the largest mammal in the world?": "blue whale",
        "Who painted the Mona Lisa?": "leonardo da vinci",
        "What is the chemical symbol for gold?": "au",
        "Which element has the atomic number 1?": "hydrogen",
        "What is the largest organ in the human body?": "skin"
    }
    return quiz_questions

def run_quiz(questions, randomize=True):
    """
    Runs the quiz game with given questions
    Parameters:
        questions (dict): Dictionary of questions and answers
        randomize (bool): Whether to randomize question order
    """
    score = 0
    total_questions = len(questions)
    
    # Convert questions to list for randomization
    question_list = list(questions.items())
    if randomize:
        random.shuffle(question_list)
    
    print("\nWelcome to Quiz Bowl!")
    print("===================")
    print(f"\nYou'll be asked {total_questions} questions. Let's begin!\n")
    
    # Loop through questions
    for i, (question, correct_answer) in enumerate(question_list, 1):
        print(f"\nQuestion {i}: {question}")
        
        # Get user's answer and convert to lowercase for comparison
        user_answer = input("Your answer: ").strip().lower()
        
        # Check answer and provide feedback
        if user_answer == correct_answer:
            print("Correct! Well done!")
            score += 1
        else:
            print(f"Sorry, that's incorrect. The correct answer is: {correct_answer.title()}")
    
    # Display final score
    print("\nQuiz completed!")
    print(f"Your final score: {score}/{total_questions}")
    percentage = (score / total_questions) * 100
    print(f"Percentage: {percentage:.1f}%")
    
    # Provide performance feedback
    if percentage == 100:
        print("Perfect score! Excellent work!")
    elif percentage >= 80:
        print("Great job!")
    elif percentage >= 60:
        print("Good effort!")
    else:
        print("Keep practicing!")

def main():
    """
    Main function to run the Quiz Bowl program
    """
    # Get questions and run quiz
    questions = create_quiz_questions()
    run_quiz(questions)
    
    # Farewell message
    print("\nThanks for playing Quiz Bowl!")
    print("===========================")

if __name__ == "__main__":
    main()
