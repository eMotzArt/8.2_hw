import random
from functions import json_file_to_mem, statistic
from classes import Question

def main():

    questions = []

    questions_list: list = json_file_to_mem('questions.json')

    for question in questions_list:
        new_question = Question(question['q'], question['d'], question['a'])
        questions.append(new_question)

    random.shuffle(questions)

    for question in questions:
        user_answer = input(question.build_question())
        question.remember_answer(user_answer)
        print(question.build_feedback())

    print(statistic(questions))


if __name__ == "__main__":
    main()
