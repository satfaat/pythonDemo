from models.web.User import User


class Friend(User):
    def __init__(self, name, phone, address=None) -> None:
        # from parent class
        super().__init__(name, phone)
        # new field
        self.address = address

    def info(self):
        print(
            f'Имя: {self.name} || Телефон: {self.phone} || Адрес: {self.address}')
