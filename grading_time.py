"""
In a school, teachers need to grade assignments based on the number of questions
completed by each student. Write a Python function called grading_time that calculates
the time (in minutes) a teacher will take to grade an assignment:

Up to 5 questions: 5 minutes
6–15 questions: 10 minutes
16–30 questions: 20 minutes
More than 30 questions: 30 minutes

The function should take the number of questions as input and return the estimated grading time.
"""


def grading_time(questions):
    if questions <= 5:
        return 5
    elif questions <= 15:
        return 10
    elif questions <= 30:
        return 20
    else:
        return 30
if __name__ == "__main__":
    # Example usage with interactive input
    try:
        questions = int(input("Enter the number of questions in the assignment: "))
        print(f"Estimated grading time: {grading_time(questions)} minutes")
    except ValueError:
        print("Please enter a valid number!")