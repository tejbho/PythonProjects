class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    def display(self):
        print(self.name, self.balance)
    def withdraw(self, amount):
        self.balance = self.balance - amount
    def deposit(self, amount):
        self.balance = self.balance + amount
        
x = Account('bob')
y = Account('frank', 20)
x.display()
y.display()
x.deposit(8)
y.deposit(3)
x.deposit(7)
x.withdraw(5)
y.deposit(9)
y.withdraw(1)
x.display()
y.display()
