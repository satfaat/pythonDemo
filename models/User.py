class User:
    def __init__(self, name, phone) -> None:
        self.name: str = name
        self.phone = phone

    def info(self) -> None:
        print(f'{self.name} ({self.phone})')
