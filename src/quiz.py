# Import the Flashcard class from flashcards.py
from flashcards import Flashcard

# Define the Quiz class
class Quiz:
    def __init__(self):
        self.questions = []  # List to hold Flashcard instances
        self.score = 0  # User's score
        self.total_questions = 0  # Total number of questions

    def add_question(self, flashcard):
        self.questions.append(flashcard)
        self.total_questions += 1

    def remove_question(self, question_text):
        for flashcard in self.questions:
            if flashcard.question == question_text:
                self.questions.remove(flashcard)
                self.total_questions -= 1
                return True  # Question removed successfully
        return False  # Question not found

    def take_quiz(self):
        for flashcard in self.questions:
            user_answer = input(flashcard.display_question() + " ")
            if user_answer.lower() == flashcard.answer.lower():
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is {flashcard.display_answer()}")
        print(f"Your score is {self.score}/{self.total_questions}")

# Create some Flashcard instances for testing
flashcard1 = Flashcard("What is the capital of France?", "Paris", "Geography")
flashcard2 = Flashcard("What is 2 + 2?", "4", "Math")

# Create a Quiz instance and add flashcards to it
quiz = Quiz()
quiz.add_question(flashcard1)
quiz.add_question(flashcard2)

# Uncomment the line below to run the quiz interactively
quiz.take_quiz()
