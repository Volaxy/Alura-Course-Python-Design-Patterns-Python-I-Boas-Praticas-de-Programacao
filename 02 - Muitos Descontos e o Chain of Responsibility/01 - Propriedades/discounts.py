class DiscountForMore5Items:
    def __init__(self, next_discount):
        self.next_discount = next_discount

    def calculate(self, budget):
        if budget.total_items > 5:
            return budget.value * 0.1
        else:
            return self.next_discount.calculate(budget)


class DiscountForTotalAmountOver500:
    def __init__(self, next_discount):
        self.next_discount = next_discount

    def calculate(self, budget):
        if budget.value > 500:
            return budget.value * 0.07
        else:
            return self.next_discount.calculate(budget)


class WithoutDiscount:
    def calculate(self, budget):
        return 0
