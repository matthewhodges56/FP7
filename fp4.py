# Function to create a simple quiz using a dictionary of questions and answers
def trivia_quiz():
    # Defining a dictionary with questions (keys) and answers (values)
    questions = {
        "What is the capital of France?": "Paris",
        "Who wrote 'Hamlet'?": "Shakespeare",
        "What is the smallest planet in our solar system?": "Mercury",
        "What is the chemical symbol for water?": "H2O",
        "Which year did the Titanic sink?": "1912"
    }

    correct_count = 0  # Counter for correct answers

    # Loop through the dictionary to ask each question
    for question, correct_answer in questions.items():
        # Display the question to the user
        user_answer = input(f"{question} ")

        # Check if the user's answer matches the correct answer (case-insensitive)
        if user_answer.strip().lower() == correct_answer.lower():
            print("Correct!")
            correct_count += 1  # Increment the correct count
        else:
            print(f"Incorrect! The correct answer is: {correct_answer}")

    # Display the total number of correct answers
    print(f"You got {correct_count} out of {len(questions)} correct!")

# Calling the function to start the quiz
trivia_quiz()