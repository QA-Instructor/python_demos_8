from accounts.account import Account
from accounts.minimum_balance_breached_exception import MinimumBalanceBreachedException


class SavingAccount(Account):

    def __init__(self, amount, firstname, lastname, minimum_balance):
        super().__init__(amount, firstname, lastname)
        self._minimum_balance = minimum_balance

    def withdraw(self, amount):
        if amount >= 0 and self._balance - amount > self._minimum_balance:
            self._balance -= amount
        else:
            breach_amount = self._minimum_balance - (self._balance - amount)
            raise MinimumBalanceBreachedException(breach_amount)


