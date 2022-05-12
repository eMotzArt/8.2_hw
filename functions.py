import json


def json_file_to_mem(file_name: str) -> list:
    """Декодирует json файл в переменную-словарь"""
    with open(file_name) as file:
        content = json.load(file)
    return content


def statistic(list_of_questions):
    points = 0
    correct_answers = 0
    for question in list_of_questions:
        if question.is_correct:
            points += question.get_points
            correct_answers += 1
    return f"Вот и всё! \n" \
           f"Отвечено на {correct_answers} из {len(list_of_questions)}\n" \
           f"Набрано баллов: {points}"
