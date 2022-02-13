from budget_state import OKAY, ONAPPROVAL, DISAPPROVED, FINISHED


class Budget:
    def __init__(self):
        self.__items = []
        self.current_state = ONAPPROVAL()
        self.__extra_discount = 0

    def apply_extra_discount(self):
        self.current_state.apply_extra_discount(self)

    def approves(self):
        self.current_state.approves(self)

    def fails(self):
        self.current_state.fail(self)

    def ends(self):
        self.current_state.ends(self)

    @property
    def extra_discount(self):
        return self.__extra_discount

    def add_extra_discount(self, value):
        self.__extra_discount += value

    # When the property is accessed, it sums each item returning the budget amount
    @property
    def value(self):
        total = 0.0
        for item in self.__items:
            total += item.value

        return total - self.__extra_discount

    # We return a tuple, as it makes no sense to change items in a quote
    def get_items(self):
        return tuple(self.__items)

    # We ask for the budget the total of items
    @property
    def total_items(self):
        return len(self.__items)

    def add_item(self, item):
        self.__items.append(item)


# A created item cannot be changed, its properties are read-only
class Item(object):
    def __init__(self, name, value):
        self.__name = name
        self.__value = value

    @property
    def value(self):
        return self.__value

    @property
    def name(self):
        return self.__name
