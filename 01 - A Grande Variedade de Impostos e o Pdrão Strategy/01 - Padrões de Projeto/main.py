from budget import Budget
from tax_calculator import TaxCalculator
from taxes import ISS, ICMS


def __main__():
    budget = Budget(1000)

    # The pattern "Strategy" is the passing of functions as parameters, making the code more flexible
    # tax = TaxCalculator.perform_calculation(budget, ISS)
    # print(tax)
    # tax = TaxCalculator.perform_calculation(budget, ICMS)
    # print(tax)

    tax = TaxCalculator.perform_calculation(budget, ISS())
    print(tax)
    tax = TaxCalculator.perform_calculation(budget, ICMS())
    print(tax)


if __name__ == "__main__":
    __main__()
