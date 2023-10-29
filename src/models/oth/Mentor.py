from models.web.User import User


class Mentor(User):
    def __init__(self, name) -> None:
        super().__init__(name, None)

    def answer_question(self, question) -> None:
        if question == 'мне грустненько, что делать?':
            print('Отдохни и возвращайся с вопросами по теории.')
        elif question == 'как устроиться работать питонистом?':
            print('Сейчас расскажу.')
        else:
            super().answer_question(question)
