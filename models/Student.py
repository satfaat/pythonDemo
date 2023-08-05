from models.User import User


class Student(User):
    def __init__(self, name) -> None:
        super().__init__(name, None)

    def ask_question(self, someone, question) -> None:
        print(f'{someone.name}, {question}')
        someone.answer_question(question)
        print('')
