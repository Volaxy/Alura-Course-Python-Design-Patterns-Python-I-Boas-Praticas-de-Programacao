from discount_calculator import DiscountCalculator
from budget import Budget, Item


def __main__():
    budget = Budget()
    budget.add_item(Item('Item A', 100.0))
    budget.add_item(Item('Item B', 50.0))
    budget.add_item(Item('Item C', 400.0))

    discount = DiscountCalculator.calculate(budget)
    print('Calculated discount: ', discount)


if __name__ == "__main__":
    __main__()
