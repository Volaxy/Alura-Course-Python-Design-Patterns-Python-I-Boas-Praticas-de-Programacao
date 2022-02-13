from budget import Budget, Item
from tax_calculator import TaxCalculator
from taxes import ISS, ICMS, ICPP, IKCV


def __main__():
    budget = Budget()

    budget.add_item(Item('ITEM 1', 100))
    budget.add_item(Item('ITEM 2', 50))
    budget.add_item(Item('ITEM 3', 400))

    budget.apply_extra_discount()
    print(budget.value)  # Prints 522.5 because it discounted 5% from 550.0
    budget.approves()

    budget.apply_extra_discount()
    print(budget.value)  # Prints 512.05 because it discounted 2% from 522.5
    budget.ends()

    # budget.apply_extra_discount()  # Throws an exception, because you cannot apply a discount to a finalized quote


if __name__ == "__main__":
    __main__()
