from abc import abstractmethod, ABCMeta


class Tax:
    __metaclass__ = ABCMeta

    def __init__(self, other_tax=None):
        self._other_tax = other_tax

    @abstractmethod
    def calculate(self, budget):
        pass

    def calculate_other_tax(self, budget):
        if self._other_tax is None:
            return 0
        else:
            return self._other_tax.calculate(budget)


class ConditionalTaxTemplate(Tax):
    __metaclass__ = ABCMeta

    def calculate(self, budget):
        if self.must_use_maximum_taxation(budget):
            return self.maximum_taxation(budget) + self.calculate_other_tax(budget)
        else:
            return self.minimum_taxation(budget) + self.calculate_other_tax(budget)

    @abstractmethod
    def must_use_maximum_taxation(self, budget):
        pass

    @abstractmethod
    def maximum_taxation(self, budget):
        pass

    @abstractmethod
    def minimum_taxation(self, budget):
        pass


def IPVX(method_or_function):
    def wrapper(self, budget):
        return method_or_function(self, budget) + 50

    return wrapper


class ISS(ConditionalTaxTemplate):
    @IPVX
    def calculate(self, budget):
        return budget.value * 0.1 + self.calculate_other_tax(budget)


class ICMS(ConditionalTaxTemplate):
    def calculate(self, budget):
        return budget.value * 0.06 + self.calculate_other_tax(budget)


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
