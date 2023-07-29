class Contact:
    def __init__(self, name, phone, address, birthday):
        self.name = name
        self.phone = phone
        self.address = address
        self.birthday = birthday
        print(f"New contact created: {name}")

    def show_contact(self):
        print(f"{self.name} — адрес: {self.address}, телефон: {self.phone}, день рождения: {self.birthday}")

    def __str__(self):
        return "Контакт: " + self.name
