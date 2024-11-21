from accounts.account import Account

# print(dir(Account))

# instantiation
# this is when we create objects based on classes
#
lisa_account = Account(100, 'Lisa', 'Simpson')
print(lisa_account)
lisa_balance = lisa_account.get_balance()
print(f"Lisa's balance is ${lisa_balance}")
#
# add some cash to Lisa's account
# OOP notation: object.method()
lisa_account.deposit(20)
lisa_balance = lisa_account.get_balance()
print(f"Lisa's new balance is ${lisa_balance}")

# this accesses the field directly because it is public
firstname = lisa_account.first_name
print(firstname)

# # this doesn't work because it is private
# lastname = lisa_account.last_name
# print(lastname)

lastname = lisa_account.get_lastname()
print(lastname)

lisa_account.set_lastname("Van Houten")
print(f"Lisa's old lastname was {lastname} and her new lastname is {lisa_account.get_lastname()}")

# instantiate an account for Bart Simpson and experiment with it
bart_account = Account(20, 'Bart', 'Simpson')
print(bart_account)

bart_account.withdraw(50)
print(bart_account)

bart_account.withdraw(-5000)
print(bart_account)

print(dir(Account))
first_name_exists = hasattr(bart_account, 'first_name')
print(f"The Bart account object has a first_name attribute: {first_name_exists}")

print('#' * 40)
print('Public, semi-private and private fields / attributes')
print('FIRSTNAME has no preceding underscores so it is public')
print(bart_account.first_name)

print('BALANCE has a single preceding underscores so it is semi-private')
# PyCharm warns you about accessing a protected member
print(bart_account._balance)

print('LASTNAME has double preceding underscores so it is private')
# print(bart_account.__last_name)
print("If you know it exists you can access it via it's mangled name")
print(bart_account._Account__last_name)

print('\\' * 40)
print('Operator overloading')

simpson_total = bart_account + lisa_account
print(f"Bart's balance: {bart_account.get_balance()}")
print(f"Lisa's balance: {lisa_account.get_balance()}")
print(f"Simpson total balance: {simpson_total}")

# bart_account.deposit(1000)
print(f"Bart's balance: {bart_account.get_balance()}")
print(f"Lisa's balance: {lisa_account.get_balance()}")
bart_account.deposit(150)
print(f"Bart's balance: {bart_account.get_balance()}")
print(f"Lisa's balance: {lisa_account.get_balance()}")

if lisa_account > bart_account:
    print("Lisa has more money in the bank than Bart")
elif lisa_account < bart_account:
    print("Lisa has less money in the bank than Bart")
else:
    print("Bart and Lisa have the same amount of money in their accounts")

lisa_clone_account = lisa_account

if lisa_account == bart_account:
    print("Lisa and Bart have the same balance")

if lisa_account is bart_account:
    print("Lisa and Bart are the same account")

if lisa_account == lisa_clone_account:
    print("Lisa and CLONE have the same balance")

if lisa_account is lisa_clone_account:
    print("Lisa and CLONE are the same account")

marge_account = Account(250, 'Marge', 'Simpson')
print(marge_account)

# getters
print(marge_account.get_firstname())
print(marge_account.get_lastname())

# properties
# notice there are no brackets
print(marge_account.account_holder_name)

# setters
# property syntax
marge_account.account_holder_name = "Margorie Simpson"
print(marge_account.account_holder_name)

print(marge_account.get_firstname())
print(marge_account.get_lastname())

marge_account.set_firstname("Margie")
print(marge_account.get_firstname())

print('/' * 40)
print('Class methods and fields / attributes')
print(f"There are {Account.numCreated} accounts")

Account.set_bank_name("Bank of Victoria")
print(f"Bank Name: {Account.get_bank_name()}")

# the class method can be accessed via the class or an object instance
print(marge_account.get_bank_name())

# Class members are shared amongst ALL object instances
bart_account.set_bank_name("National Skateboard Bank")
print(marge_account.get_bank_name())

# errors
print("#" * 40)
print(bart_account)
print("Attempt to deposit a negative amount")
print("Writing to stderr")
bart_account.deposit(-50)

# print(bart_account)
