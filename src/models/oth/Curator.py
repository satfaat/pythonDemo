from models.web.User import User


class Curator(User):
    def __init__(self, name):
        super().__init__(name, None)

    def answer_question(self, question):
        if question == 'мне грустненько, что делать?':
            print('Держись, всё получится. Хочешь видео с котиками?')
        else:
            super().answer_question(question)
