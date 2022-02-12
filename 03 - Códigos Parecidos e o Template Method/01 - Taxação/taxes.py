from abc import abstractmethod, ABC


# The "Template Method" is a pattern where child classes implement the part of code that is "missing"
class ConditionalTaxTemplate(object):
    def calculate(self, budget):
        if self.must_use_maximum_taxation(budget):
            return self.maximum_taxation(budget)
        else:
            return self.minimum_taxation(budget)

    @abstractmethod
    def must_use_maximum_taxation(self, budget):
        pass

    @abstractmethod
    def maximum_taxation(self, budget):
        pass

    @abstractmethod
    def minimum_taxation(self, budget):
        pass


class ISS:
    def calculate(self, budget):
        return budget.value * 0.1


class ICMS:
    def calculate(self, budget):
        return budget.value * 0.06


class ICPP(ConditionalTaxTemplate):
    def must_use_maximum_taxation(self, budget):
        return budget.value > 500

    def maximum_taxation(self, budget):
        return budget.value * 0.07

    def minimum_taxation(self, budget):
        return budget.value * 0.05


class IKCV(ConditionalTaxTemplate):
    def must_use_maximum_taxation(self, budget):
        return budget.value > 500 and self.__has_item_greater_than_100_reais(budget)

    def maximum_taxation(self, budget):
        return budget.value * 0.10

    def minimum_taxation(self, budget):
        return budget.value * 0.06

    def __has_item_greater_than_100_reais(self, budget):
        for item in budget.get_itens():
            if item.value > 100:
                return True

        return False
