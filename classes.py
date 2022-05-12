class Question:
    """Класс вопроса"""

    def __init__(self, question, complexity, answer):
        self.question = question
        self.complexity = int(complexity)
        self.answer = answer

        self.is_asked = False
        self.user_answer = ""
        self.points = self.complexity * 10

    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        return self.points

    def remember_answer(self, answer):
        self.user_answer = answer
        self.is_asked = True

    def is_correct(self):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """
        return self.answer == self.user_answer

    def build_question(self):

        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """

        return f"Вопрос: {self.question}? \n" \
               f"Сложность: {self.complexity}/5\n"

    def build_feedback(self):

        """Возвращает :
        Ответ верный, получено __ баллов
        или
        Ответ неверный, верный ответ __
        """
        if self.is_correct():
            return f"Ответ верный, получено {self.points} баллов\n"
        else:
            return f"Ответ неверный, верный ответ {self.answer}\n"
