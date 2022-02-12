from budget import Budget, Item
from tax_calculator import TaxCalculator
from taxes import ISS, ICMS, ICPP, IKCV


def __main__():
    budget = Budget()

    budget.add_item(Item('ITEM 1', 50))
    budget.add_item(Item('ITEM 2', 200))
    budget.add_item(Item('ITEM 3', 250))

    tax = TaxCalculator.perform_calculation(budget, ISS())
    print("ISS: ", tax)
    tax = TaxCalculator.perform_calculation(budget, ICMS())
    print("ICMS: ", tax)

    tax = TaxCalculator.perform_calculation(budget, ICPP())
    print("ICPP: ", tax)
    tax = TaxCalculator.perform_calculation(budget, IKCV())
    print("IKCV: ", tax)

    tax = TaxCalculator.perform_calculation(budget, ISS(ICMS()))
    print(tax)


if __name__ == "__main__":
    __main__()
