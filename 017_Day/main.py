from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = [] # Create a list which we will hold Question data-types

# creating completed 'question_bank' iterating through the data file and constructing Question constructor in each element in the list 
for question in question_data:
    # create new variable in question index that will grab both the text and the answer
    question_text = question["text"]
    question_answer = question["answer"]
    # create new question from question class that will use the initalize constructor
    new_question = Question(question_text , question_answer)
    # append into the question bank 
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()
        
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
