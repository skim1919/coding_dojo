#<Let's first just get some more practice writing classes by writing a new BankAccount class.>
# The BankAccount class should have a balance. 
# When a new BankAccount instance is created, if an amount is given, 
# the balance of the account should initially be set to that amount; otherwise, the balance should start at $0. 
# The account should also have an interest rate in decimal format. For example, a 1% interest rate would be saved as 0.01. The interest rate should be provided upon instantiation. (Hint: when using default values in parameters, the order of parameters matters!)

# <The class should also have the following methods>:
class BankAccount:

    all_instances = []

    def __init__(self, int_rate, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        print(int_rate)
        print(balance)
        BankAccount.all_instances.append(self)
        
    # deposit(self, amount) - increases the account balance by the given amount
    def deposit(self, amount):
        self.balance += amount
        return self

    # withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5   
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: charging a $5 fee")
            self.balance -= 5
            return self
        self.balance -= amount
        return self

    # display_account_info(self) - print to the console: eg. "Balance: $100"
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    # yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

    @classmethod
    def print_all_instances(cls):
        for i in range(len(cls.all_instances)):
            instance = cls.all_instances[i]
            print(f"Account {i} - balance: ${instance.balance}, interest rate: {instance.int_rate}")

# create 2 accounts
user1 = BankAccount(0.1, 100)
user2 = BankAccount(0.02, 50)

# # To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
user1.deposit(100).deposit(300).deposit(500).withdraw(50).yield_interest().display_account_info()

# # To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
user2.deposit(500).deposit(1000).withdraw(10).withdraw(10).withdraw(5).withdraw(1).yield_interest().display_account_info()

# # NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
BankAccount.print_all_instances()

