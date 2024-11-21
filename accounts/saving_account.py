from accounts.account import Account
from accounts.minimum_balance_breached_exception import MinimumBalanceBreachedException
from accounts.product import Product


# inheritance
class SavingAccount(Product, Account):

    def __init__(self, amount, firstname, lastname, minimum_balance):
        # super().__init__(amount, firstname, lastname) # this calls the first inherited class's constructor
        # better to be explicit
        # must include self param explicitly
        Account.__init__(self, amount, firstname, lastname) # this calls the first inherited class's constructor
        Product.__init__(self, "Unknown category") # this explicitly calls the Product constructor
        self._minimum_balance = minimum_balance

    def method_a(self):
        message = Account.method_a(self)
        message += "\n" + Product.method_a(self)
        return message

    def withdraw(self, amount):
        if amount >= 0 and self._balance - amount > self._minimum_balance:
            self._balance -= amount
        else:
            breach_amount = self._minimum_balance - (self._balance - amount)
            raise MinimumBalanceBreachedException(breach_amount)


