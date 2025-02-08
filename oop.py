class Account:
    
    def __init__(self, path):
        self.path = path
        with open(path,'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount
    
    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.path, 'w') as file:
            file.write(str(self.balance))

# account = Account('balance.txt')
# print(account.balance)
# account.deposit(4000)
# account.commit()
# print(account.balance)

class Checking(Account):
    def __init__(self, path, fee):
        super().__init__(path)
        self.fee = fee
    
    def tranfer(self, amount):
        self.balance = self.balance - amount - self.fee

checking = Checking('balance.txt', 2)
checking.tranfer(50)
print(checking.balance)
checking.commit()