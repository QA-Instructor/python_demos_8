from accounts.saving_account import SavingAccount

lisa_saving_account = SavingAccount(300, 'Lisa', 'Simpson', 250)
print(lisa_saving_account)
print(lisa_saving_account.method_a()) # this calls the implementation of whichever class is
# inherited from first unless you override it and call a specific (or both) implementations

