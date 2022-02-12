from discounts import DiscountForMore5Items, DiscountForTotalAmountOver500, WithoutDiscount


class DiscountCalculator(object):
    @staticmethod
    def calculate(budget):
        # This pattern is called of "Chain of Responsibility", which instead of writing procedural code, breaks the
        # responsibility into several classes, and then joins them as a chain
        discount = DiscountForMore5Items(
            DiscountForTotalAmountOver500(
                WithoutDiscount()
            )
        )

        return discount.calculate(budget)
