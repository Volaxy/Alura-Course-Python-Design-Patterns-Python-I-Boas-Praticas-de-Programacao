from abc import ABCMeta, abstractmethod


class BudgetState:
    __metaclass__ = ABCMeta

    @abstractmethod
    def apply_extra_discount(self, budget):
        pass

    @abstractmethod
    def approves(self, budget):
        pass

    @abstractmethod
    def fail(self, budget):
        pass

    @abstractmethod
    def ends(self, budget):
        pass


class ONAPPROVAL(BudgetState):
    def apply_extra_discount(self, budget):
        budget.add_extra_discount(budget.value * 0.05)

    def approves(self, budget):
        budget.current_state = OKAY()

    def fail(self, budget):
        budget.current_state = DISAPPROVED()

    def ends(self, budget):
        raise Exception("Approved budget cannot go to finalized directly")


class OKAY(BudgetState):
    def apply_extra_discount(self, budget):
        budget.add_extra_discount(budget.value * 0.02)

    def approves(self, budget):
        raise Exception("Budget is already in approval status")

    def fail(self, budget):
        raise Exception("Budget is in approval status and cannot be disapproved")

    def ends(self, budget):
        budget.current_state = FINISHED()


class DISAPPROVED(BudgetState):
    def apply_extra_discount(self, budget):
        raise Exception("Failed quotes do not receive extra discount")

    def approves(self, budget):
        raise Exception("Failed budget cannot be approved")

    def fail(self, budget):
        raise Exception("Budget is already in a state of disapproval")

    def ends(self, budget):
        raise Exception("Failed budget cannot be finalized")


class FINISHED(BudgetState):
    def apply_extra_discount(self, budget):
        raise Exception("Finished budgets do not receive extra discount")

    def approves(self, budget):
        raise Exception("Finalized budget has already been approved")

    def fail(self, budget):
        raise Exception("Budget already finalized cannot be disapproved")

    def ends(self, budget):
        raise Exception("Budget has already been finalized")
