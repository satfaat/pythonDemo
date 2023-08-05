from models.User import User


class CodeReviewer(User):
    def __init__(self, name):
        super().__init__(name, None)

    def answer_question(self, question):
        if question == 'что не так с моим проектом?':
            print('О, вопрос про проект, это я люблю.')
        else:
            super().answer_question(question)
