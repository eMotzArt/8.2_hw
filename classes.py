class Question:
    """Класс вопроса"""

    def __init__(self, question, complexity, answer):
        self.__question = question
        self.__complexity = int(complexity)
        self.__answer = answer

        self.__is_asked = False
        self.__user_answer = ""
        self.__points = self.__complexity * 10

    @property #user_input
    def user_answer(self):
        return self.__user_answer

    @user_answer.setter
    def user_answer(self, value):
        self.__user_answer = value
        self.__is_asked = True

    @property #get_points
    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        return self.__points

    @property #is_correct
    def is_correct(self):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """
        return self.__answer == self.__user_answer

    def build_question(self):

        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """

        return f"Вопрос: {self.__question}? \n" \
               f"Сложность: {self.__complexity}/5\n"

    def build_feedback(self):

        """Возвращает :
        Ответ верный, получено __ баллов
        или
        Ответ неверный, верный ответ __
        """
        if self.is_correct:
            return f"Ответ верный, получено {self.__points} баллов\n"
        else:
            return f"Ответ неверный, верный ответ {self.__answer}\n"
