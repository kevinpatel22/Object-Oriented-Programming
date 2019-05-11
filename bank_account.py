class BankAccount:

    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
    
    def __str__(self):
        return (f"-------------------------------------\nAccount balance: {self.balance:.2f}\nYour interest rate is: {self.interest_rate:.2f}\n-------------------------------------")

    def deposit(self, amount):
        self.balance = self.balance + amount
        return (f"Total Balance after Deposit = {self.balance}")
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
        return (f"Total Balance after Withdrawl = {self.balance}")
    
    def gain_interest(self):
        self.balance += (self.balance * self.interest_rate) / 100
        return (f"Total Balance after interest earned = {self.balance}")
        


myaccount = BankAccount(1000, 10)
print(myaccount.deposit(1500))
print(myaccount.withdraw(200))
print(myaccount.gain_interest())
print(myaccount)
