
class QuizBrain:
    def __init__(self, qList):

        self.questionNumber = 0
        self.score = 0
        self.questionList = qList

    def nextQuestion(self):
        currentQuestion = self.questionList[self.questionNumber]
        
        self.questionNumber+=1

        userAnswer = input(f"Q.{self.questionNumber} > {currentQuestion.text} (True/False) : ")

        self.checkAnswer(userAnswer,currentQuestion.answer)
        

    def stillHasQuestion(self):
        return self.questionNumber < len(self.questionList)
    
    def checkAnswer(self,userAnswer,correctAnswer) :
        if userAnswer.lower() == correctAnswer.lower():
            print("Correct")
            self.score += 1
            
        else:
            print(f"Incorrect. The correct answer is {correctAnswer}")
            
        print(f"Your current score is {self.score}/{self.questionNumber}")
        print("\n")

        return self.score

