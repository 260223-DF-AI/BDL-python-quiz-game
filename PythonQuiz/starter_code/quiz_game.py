# quiz_game.py - Python Quiz Game
# Starter code for e004-exercise-control-flow (Collaborative Project)

from subprocess import call # clear terminal command
import os # check os for correct terminal command
from datetime import datetime # for question timer
import random # for question shuffling

"""
Python Quiz Game
----------------
A multiple-choice quiz game that tests Python knowledge.

This is a collaborative project - use pair programming!
- Driver: Types the code
- Navigator: Reviews and guides

Switch roles every 20-30 minutes!
"""

# =============================================================================
# TODO: Task 1 - Question Bank (Driver 1)
# =============================================================================

def create_question_bank():
    """
    Return a list of quiz questions.
    
    Each question is a dictionary with:
    - question: The question text
    - options: List of 4 options (A, B, C, D)
    - answer: Correct answer letter
    - explanation: Why this answer is correct
    
    Add at least 10 questions covering Week 1 topics.
    """
    questions = [
        {
            "question": "What keyword is used to define a function in Python?",
            "options": ["A) func", "B) def", "C) function", "D) define"],
            "answer": "B",
            "explanation": "The 'def' keyword is used to define functions in Python."
        },
        {
            "question": "Select the true statement",
            "options": ["A) Python uses semicolons to denote line endings.", "B) Python requires declaration of variable types", "C) The official name of Python is 'Big Snake Language!'", "D) Python is whitespace sensitive."],
            "answer": "D",
            "explanation": "Python relies on whitespace instead of semicolons, and does not require type declarations because it is interpretted, not compiled. And it is definitely not called 'Big Snake Language!'"
        },
        {
            "question": "What would the following code snippet output:\nnumbers = [1, 2, 3, 4, 5]\nlist = [x**2 for x in numbers]\nprint(list)",
            "options": ["A)\n1\n4\n9\n16\n25", "B) [1, 4, 9, 16, 25]", "C) [2, 4, 6, 8, 10]", "D) list at 0x0000001738"],
            "answer": "B",
            "explanation": "The list of numbers will be printed out in one line, with each number being the square of its counterpart in 'list.'"
        },
        {
            "question": "This data type is ordered, immutable, and allows duplicates.",
            "options": ["A) List", "B) Tuple", "C) Set", "D) Dictionary"],
            "answer": "B",
            "explanation": "All of the above except for Tuples are mutable."
        },
        {
            "question": "What is the output the following logical operator: return not (True or False) or (1 and 0)",
            "options": ["A) True", "B) False", "C) None", "D) Error"],
            "answer": "B",
            "explanation": "Not inverts the output of the comparison in the first set of parentheses, and 1 and 0 are equivalent to True and False, respectively, in Python."
        },
        {
            "question": "Which of the following is NOT a way to format strings in Python?",
            "options": ["A) print(\"Hello, \" + name)", "B) print(\"Hello\", name)", "C) print(\"Hello, {name}\")", "D) print(f\"Hello, {name}\")"],
            "answer": "C",
            "explanation": "Option C is missing the 'f' before the string starts to denote an interpolated string."
        },
        {
            "question": "What is the output of the following equation in Python: 12 - 3 * 2 ** 2 + 8 / 4 * (3 - 1) // 2",
            "options": ["A) 2", "B) 0", "C) 83", "D) 4"],
            "answer": "A",
            "explanation": "Following PEMDAS, you should arrive to 2."
        },
        {
            "question": "What is the output of the following: float(14)",
            "options": ["A) 14", "B) 14.00", "C) \"14\"", "D) 14.0"],
            "answer": "D",
            "explanation": "Python uses a decimal point to differentiate between an integer and a float, and since 14 is a whole number, it only needs one 0 following the decimal."
        },
        {
            "question": "Which of the following is a valid Python datatype",
            "options": ["A) int", "B) null", "C) None", "D) Both A and C"],
            "answer": "D",
            "explanation": "Null is not a valid Python datatype, as that purpose is served by None in Python."
        },
        {
            "question": "What is the proper formatting for a lambda function?",
            "options": ["A) func = lambda x, y: x * y", "B) func = func(): lambda x, y : x * y l", "C) func(lambda x, y: x * y)", "D) func = lambda : x * y"],
            "answer": "A",
            "explanation": "The other options will give syntax errors"
        }
        # TODO: Add 9 more questions covering:
        # - Python syntax and indentation
        # - Data types (strings, lists, dictionaries)
        # - Control flow (if/else, loops)
        # - Functions and parameters
        # - Variables and operators
    ]
    return questions


# =============================================================================
# TODO: Task 2 - Core Game Functions (Driver 2)
# =============================================================================

def display_question(question, number, total):
    """
    Display a question and its options.
    
    Args:
        question: A question dictionary
        number: The current question number (1-based)
        total: Total number of questions
    
    Output format:
    --------------------------------------------------
    Question 1 of 10
    --------------------------------------------------
    [question text]
    
    A) option A
    B) option B
    C) option C
    D) option D
    """
    # TODO: Implement this function
    print("-"*44)
    print(f"Question {number} of 10")
    print("-"*44)
    print(question["question"])
    print()
    for x in question["options"]:
        print(x)



def get_user_answer():
    """
    Get and validate user input.
    
    Keep prompting until the user enters a valid answer (A, B, C, or D).
    Accept both uppercase and lowercase input.
    
    Returns:
        A valid answer in uppercase (A, B, C, or D)
    """
    # TODO: Implement input validation loop
    start = datetime.now()
    while True:
        answer = input("Select your answer: ").upper()
        if (datetime.now() - start).seconds > 60: # if time limit has passed by the time user enters answer, ignore answer and return none
            print("Time expired before you could answer.")
            return None
        if answer in ["A", "B", "C", "D"]: # only accept valid answer (after being formatted with upper())
            return answer



def check_answer(question, user_answer):
    """
    Check if the user's answer is correct.
    
    Args:
        question: The question dictionary
        user_answer: The user's answer (uppercase letter)
    
    Returns:
        True if correct, False otherwise
    """
    # TODO: Compare user_answer with question["answer"]
    if user_answer == question["answer"]:
        return True
    else:
        return False


def display_feedback(question, user_answer, is_correct):
    """
    Display feedback after answering a question.
    
    If correct: Print "Correct!" with green styling (or just text)
    If incorrect: Print "Incorrect. The answer was X."
    Always show the explanation.
    """
    # TODO: Display appropriate feedback based on is_correct
    if is_correct:
        print("\033[32m" + "Correct!" + "\033[0m") #coloring text in terminal
    else:
        print("Incorrect. The answer was " + question["answer"])
    print(question["explanation"])


# =============================================================================
# TODO: Task 3 - Game Loop (Driver 1)
# =============================================================================

def run_quiz(questions):
    """
    Run the complete quiz game.
    
    1. Display welcome message
    2. Loop through all questions
    3. For each question:
       - Display the question
       - Get user answer
       - Check if correct
       - Display feedback
       - Update score
    4. Return final score
    
    Args:
        questions: List of question dictionaries
    
    Returns:
        Tuple of (score, total_questions)
    """
    score = 0
    total = len(questions)
    
    # Welcome message
    print("=" * 50)
    print("     WELCOME TO THE PYTHON QUIZ GAME!")
    print("=" * 50)
    print(f"\nYou will answer {total} questions.")
    print("Enter A, B, C, or D for each question.\n")
    print("You will have 60 seconds per question.")
    input("Press Enter to start...")
    
    # TODO: Implement the game loop
    # Hint: Use a for loop with enumerate
    call('clear' if os.name == "posix" else 'cls', shell=True) #clearing terminal, have to do this twice for first time
    random.shuffle(questions)
    for i, x in enumerate(questions):
        call('clear' if os.name == "posix" else 'cls', shell=True)
        display_question(x, i + 1, total)
        answer = get_user_answer()
        if answer: # will not execute if time limit passed, as None is returned
            check = check_answer(x, answer)
            if check: #only executes when check == "True"
                score += 1
        else:
            check = False #backup to make sure check is passed as false if time limit was passed (could also declare and define as False before "if answer" and omit else statement)
        display_feedback(x, answer, check)
        input("Hit Enter to continue...") #wait for user to get the chance to read the explanation before moving on and clearing the screen
    
    call('clear' if os.name == "posix" else 'cls', shell=True)
    
    return score, total


# =============================================================================
# TODO: Task 4 - Results and Grading (Driver 2)
# =============================================================================

def calculate_grade(score, total):
    """
    Calculate letter grade based on percentage.
    
    Grading scale:
    - 90-100%: A
    - 80-89%:  B
    - 70-79%:  C
    - 60-69%:  D
    - Below 60%: F
    
    Args:
        score: Number of correct answers
        total: Total number of questions
    
    Returns:
        Letter grade as string
    """
    # TODO: Calculate percentage and return grade
    grade = (score / total) * 100
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"


def display_results(score, total, high_score):
    """
    Display final results with grade and encouragement.
    
    Include:
    - Score (e.g., 8/10)
    - Percentage
    - Letter grade
    - Encouraging message based on performance
    """
    # TODO: Calculate percentage and grade
    # TODO: Display formatted results
    # TODO: Add encouragement message
    print("=" * 44)
    print("\tQUIZ COMPLETE!")
    print("=" * 44)
    print(f"Score: {score} / {total} ({int((score/total) * 100)}%)") # only 10 questions so should never be a float, change in future to round floats to 2 decimals 
    print(f"Grade: {calculate_grade(score, total)}")
    if score > high_score:
        high_score = score
        print(f"WOW! New high score! {high_score} / {total} ({int((high_score / total) * 100)}%)") # same as score report: change to floats
    print()
    print("Great job! Keep practicing!")
    print("=" * 44)
    return high_score #either returns old high score or the updated one to be stored between games (not sessions)


# =============================================================================
# Main Program
# =============================================================================

def main(high_score = 0): #added default high score to be passed in on first run through
    """Main entry point for the quiz game."""
    # Create question bank
    questions = create_question_bank()
    
    # Run the quiz
    score, total = run_quiz(questions)
    
    # Display results
    high_score = display_results(score, total, high_score)
    
    # Ask to play again
    while True:
        play_again = input("\nWould you like to play again? ([y]es/[n]o): ")

        if play_again.lower() in ["yes", "y"]:
            call('clear' if os.name == "posix" else 'cls', shell=True)
            main(high_score) #uses new high score to compare next score
        elif play_again.lower() in ["no", "n"]:
            print("\nThanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
