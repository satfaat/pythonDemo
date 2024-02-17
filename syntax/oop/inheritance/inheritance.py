class A:
    def __init__(self, name) -> None:
        self.name = name

    def get_name(self):
        return self.name


class B:
    def __init__(self, age) -> None:
        self.age = age

    def get_age(self):
        return self.age


class C(A, B):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)
