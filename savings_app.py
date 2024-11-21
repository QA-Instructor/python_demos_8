import sys
from accounts.account import Account
from accounts.saving_account import SavingAccount
from accounts.minimum_balance_breached_exception import MinimumBalanceBreachedException

try:
    lisa_saving_account = SavingAccount(300, 'Lisa', 'Simpson', 250)
    print(lisa_saving_account)
    lisa_saving_account.deposit(50)
    print(lisa_saving_account)

    lisa_saving_account.withdraw(25)
    print(lisa_saving_account)

    lisa_saving_account.withdraw(99)
#     toggle between 10 and 100

    # use 'isinstance' to see if an object is an instance of a base class
    if isinstance(lisa_saving_account, SavingAccount):
        print("Lisa's savings account is a kind of SAVING ACCOUNT")

    if isinstance(lisa_saving_account, Account):
        print("Lisa's savings account is a kind of ACCOUNT")

    # use 'issubclass' to see if a class is a subclass of a base class
    if issubclass(SavingAccount, Account):
        print("A saving account is a SUBCLASS of ACCOUNT")

except MinimumBalanceBreachedException as ex:
    print("@" * 10)
    print(f"An exception has occurred!")
    print(f"You would have breached your minimum balance by {ex.get_breach_amount()}")
#     you can get a traceback for detailed exception info using sys.exc_info() function
    ex_type, value, trace_back = sys.exc_info()
    print("Exception Type:", ex_type)
    print("Value:", value)
    print("Traceback:", trace_back)
    print("Line number:", trace_back.tb_lineno)

else:
    print("no exception occurred")

finally:
    print("The FINALLY block always runs")
    print(lisa_saving_account)


