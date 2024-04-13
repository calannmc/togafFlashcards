import random

# Questions and answers data
questions_answers = [
    ("What is the objective of the Preliminary Phase?", "To obtain approval for the Statement of Architecture Work."),
    ("Which of the following describes a purpose of Architecture Principles?", "To set precedence during trade-off discussions."),
    ("Which of the following is a responsibility of an Architecture Board?", "Enforcement of architecture compliance."),
    # Add more questions and answers here
]

# Function to generate flashcards
def generate_flashcards(data):
    for i, (question, answer) in enumerate(data, 1):
        print(f"Flashcard {i}:")
        print("Question:", question)
        print("Answer:", answer)
        print()

# Function to generate quizzes
def generate_quiz(data):
    score = 0
    random.shuffle(data)
    for question, answer in data:
        user_answer = input(f"Question: {question}\nYour Answer: ").strip().lower()
        if user_answer == answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
            print("Correct Answer:", answer)
        print()
    print("Quiz completed!")
    print("Your score:", score, "/", len(data))

# Main program
def main():
    print("Welcome to the Architecture Quiz!")
    print("Choose an option:")
    print("1. Generate Flashcards")
    print("2. Take a Quiz")
    option = input("Enter your choice (1 or 2): ")
    if option == "1":
        generate_flashcards(questions_answers)
    elif option == "2":
        generate_quiz(questions_answers)
    else:
        print("Invalid option. Please choose 1 or 2.")

if __name__ == "__main__":
    main()
