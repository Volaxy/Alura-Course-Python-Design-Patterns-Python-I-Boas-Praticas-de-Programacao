from budget import Budget


class ISS:
    def calculate(self, budget):
        return budget.value * 0.1


class ICMS:
    def calculate(self, budget):
        return budget.value * 0.06
