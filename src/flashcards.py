class Flashcard:
    def __init__(self, question, answer, category):
        self.question = question
        self.answer = answer
        self.category = category

    def display_question(self):
        return self.question

    def display_answer(self):
        return self.answer

flashcard1 = Flashcard("What is the capital of France?", "Paris", "Geography")
flashcard2 = Flashcard("What is 2 + 2?", "4", "Math")

(flashcard1.display_question(), flashcard1.display_answer()), (flashcard2.display_question(), flashcard2.display_answer())

print(f"Flashcard 1 Question: {flashcard1.display_question()}, Answer: {flashcard1.display_answer()}")
print(f"Flashcard 2 Question: {flashcard2.display_question()}, Answer: {flashcard2.display_answer()}")
