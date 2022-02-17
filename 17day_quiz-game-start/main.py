from data import question_data
from quiz_brain import QuizBrain
from data import question_bank

quiz_brain = QuizBrain(question_bank)


while quiz_brain.still_has_question():
    quiz_brain.next_question()
print("You've completed the quiz")
print(f"Your final score was: {quiz_brain.score}/{len(quiz_brain.question_list)}")
