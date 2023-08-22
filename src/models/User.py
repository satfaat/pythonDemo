class User:
    def __init__(self, name, phone=None) -> None:
        self.name: str = name
        self.phone: str | None = phone

    def info(self) -> None:
        print(f'{self.name} ({self.phone})')

    def answer_question(self, question):
        print('Очень интересный вопрос! Не знаю.')
