#This is the source code for the Quiz game Application
#This can be modified to build an application

def load_questions():
    #Five questions for demonstration purpose
    #One can add more questions like these
    questions = [
        {
            'question': 'What is the capital of France?',
            'options': ['A. Berlin', 'B. Madrid', 'C. Paris', 'D. Rome'],
            'correct_answer': 'C'
        },
        {
            'question': 'Which planet is known as the Red Planet?',
            'options': ['A. Venus', 'B. Mars', 'C. Jupiter', 'D. Saturn'],
            'correct_answer': 'B'
        },
        {
            'question': 'What is the largest mammal in the world?',
            'options': ['A. Elephant', 'B. Blue Whale', 'C. Giraffe', 'D. Lion'],
            'correct_answer': 'B'
        },
        {
            'question': 'Who wrote "Romeo and Juliet"?',
            'options': ['A. Charles Dickens', 'B. William Shakespeare', 'C. Jane Austen', 'D. Mark Twain'],
            'correct_answer': 'B'
        },
        {
            'question': 'What is the capital of Japan?',
            'options': ['A. Seoul', 'B. Beijing', 'C. Tokyo', 'D. Bangkok'],
            'correct_answer': 'C'
        }
    ]
    return questions

#Display the result
def display_question(question):
    print(question['question'])
    for option in question['options']:
        print(option)
    user_answer = input("Your answer: ").upper()
    print()
    return user_answer

#Evaluate the answers
def evaluate_answers(user_answers, correct_answers):
    score = 0
    i = 1
    for user_answer, correct_answer in zip(user_answers, correct_answers):
        if user_answer == correct_answer:
            print(f"Question {i}:-  Your answer: {user_answer} ---> Correct!")
            score += 1
            i+=1
        else:
            print(f"Question {i}:-  Your answer: {user_answer} ---> Incorrect. The correct answer is {correct_answer}.")
            i+=1
    return score

#Display the final score
def display_final_results(score, total_questions):
    print(f"\nYour final score: {score}/{total_questions}\n")
    print("Thanks for playing!")

#Get the user's answers for evaluation
def quiz_game():
    while True:
        print("\n\nWelcome to the Quiz Game!\n")
        print("Instructions:\n 1) Answer each question by entering the corresponding letter.\n 2) Don't give the entire answer, Just the corresponding letter is enough.\n 3) Characters(Letters, Numbers, Symbols) other than the option character(letter) will not considered for the evaluation.\n")
        
        questions = load_questions()
        total_questions = len(questions)
        user_answers = []

        for current_question in questions:
            user_answer = display_question(current_question)
            user_answers.append(user_answer)

        correct_answers = [question['correct_answer'] for question in questions]
        score = evaluate_answers(user_answers, correct_answers)

        display_final_results(score, total_questions)

        play_again = input("\nDo you want to play again? (Type 'yes' or 'no'): ").lower()
        if play_again != 'yes':
            print("\nGoodbye!\n")
            break

# Run the quiz game
quiz_game()