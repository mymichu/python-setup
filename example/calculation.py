class Calculcation:
    def __init__(self, number_a: int, number_b: int):
        self.number_a = number_a
        self.number_b = number_b

    def add(self) -> int:
        return self.number_a + self.number_b

    def sub(self) -> int:
        return self.number_a - self.number_b

    def mul(self) -> int:
        return self.number_a * self.number_b

    def div(self) -> int:
        return int(self.number_a / self.number_b)
