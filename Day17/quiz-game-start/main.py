from question_model import Question
from data import question_data 
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    question_bank.append(Question(i["question"],i["correct_answer"]))

quiz = QuizBrain(question_bank)

while quiz.stillHasQuestion():
    quiz.nextQuestion()

print("You've completed this quiz.")
print(f"Your final score is : {quiz.score}/{len(question_bank)}.")