from data import question_data
from question_model import Question

question_bank = []
index = 0
for question in question_data:

    question_text = question['text']
    question_answer = question['answer']
    print(question_text,question_answer)
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question.text)

print(question_bank)