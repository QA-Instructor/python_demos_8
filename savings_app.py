import sys

from accounts.saving_account import SavingAccount
from accounts.minimum_balance_breached_exception import MinimumBalanceBreachedException

try:
    lisa_saving_account = SavingAccount(300, 'Lisa', 'Simpson', 250)
    print(lisa_saving_account)
    lisa_saving_account.deposit(50)
    print(lisa_saving_account)

    lisa_saving_account.withdraw(25)
    print(lisa_saving_account)

    lisa_saving_account.withdraw(10)
#     toggle between 10 and 100

except MinimumBalanceBreachedException as ex:
    print("@" * 10)
    print(f"An exception has occurred!")
    print(f"You would have breached your minimum balance by {ex.get_breach_amount()}")

else:
    print("no exception occurred")

finally:
    print("The FINALLY block always runs")
    print(lisa_saving_account)


