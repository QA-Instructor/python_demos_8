# this is our capsule
# it's a collection of attributes and methods
class Account:
    numCreated = 0
    __bank_name = None

    # this is a special method called the CONSTRUCTOR
    # a constructor method is used to get your object ready to be used
    def __init__(self, initial_amount, firstname, lastname):
        # _balance is an attribute, it's a piece of data
        # a single underscore means this field is semi-private
        self._balance = initial_amount
        self.first_name = firstname
        # dunder on a field means PRIVATE - KEEP OUT
        # double underscore means fully private
        self.__last_name = lastname
        self._account_holder_name = firstname + " " + lastname

        # class field
        Account.numCreated += 1

    # method
    def deposit(self, amount):
        self._balance += amount

    # method
    def withdraw(self, amount):
        # validation
        if amount >= 0:
            self._balance -= amount
    #         else situation we would raise an exception

    # this is what Java calls a getter
    # Java uses these to retrieve attribute values
    def get_balance(self):
        return self._balance

#     create a getter method to retrieve the first_name attribute
    def get_firstname(self):
        return self.first_name

    def set_firstname(self, firstname):
        self.first_name = firstname

    #     create a getter method to retrieve the last_name attribute
    def get_lastname(self):
        return self.__last_name.upper()

    # getters READ and setters WRITE
    # getters RETURN something, setters do not
    # setters have parameters
    def set_lastname(self, new_lastname):
        self.__last_name = new_lastname

    # getters can translate or modify the data before returning it
    # setters often validate the incoming data
    # setters often contain if statements

    # overriding a built-in method
    def __str__(self):
        return f"Account\nFirstname: {self.get_firstname()}\nLastname: {self.get_lastname()}" \
               f"\nBalance: ${self.get_balance()}\n********************"

    # operator overloading
    def __add__(self, other):
        return self._balance + other.get_balance()

    def __gt__(self, other):
        return self._balance > other.get_balance()

    def __lt__(self, other):
        return self._balance < other.get_balance()

    def __eq__(self, other):
        return self.get_balance() == other.get_balance()

#     PROPERTIES

    # @property
    # def mday(self):
    #     return self._day
    #
    # @mday.setter
    # def mday(self, day):
    #     self._day = day

    @property
    def account_holder_name(self):
        return self._account_holder_name

    @account_holder_name.setter
    def account_holder_name(self, name):
        self._account_holder_name = name
        name_parts = name.split()
        self.first_name = name_parts[0]
        self.__last_name = name_parts[1]

#     CLASS Methods

    @classmethod
    def get_bank_name(cls):
        return cls.__bank_name

    @classmethod
    def set_bank_name(cls, name):
        cls.__bank_name = name



