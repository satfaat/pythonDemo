

class Greetings:
    def __init__(self, default_name: str) -> None:
        self.defaut_name: str = default_name

    def greet(self, name: str = None) -> str:
        return f"Hello, {name if name else self.defaut_name}"
