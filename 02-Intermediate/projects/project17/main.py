"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Day 17
The Quiz Project
"""

# Imports

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Main

question_bank = []
for item in question_data:
    question_bank.append(Question(item['text'], item['answer']))

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print('You\'ve completed the quiz.')
print(f'Your final score was {quiz.score}/{quiz.question_number}.')