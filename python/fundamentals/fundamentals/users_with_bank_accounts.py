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

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 0.02, balance = 0)

    # Add a make_deposit method to the User class that calls on it's bank account's instance methods.
    def make_deposit(self, amount):
        self.account.deposit(amount)
        
    # Add a make_withdrawal method to the User class that calls on it's bank account's instance methods.
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)

    # Add a display_user_balance method to the User class that displays user's account balance
    def display_user_balance(self):
        self.account.display_account_info()
    

user1 = User('Sarang Kim', 'sarangkim@gmail.com')
user1.display_user_balance()
user1.make_deposit(100)
user1.display_user_balance()
user1.make_withdrawal(10)
user1.display_user_balance()