class Account:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        self.balance = self.balance+amount
        return "Deposit Accepted"
    def withdrawn(self,amount):
        self.balance=self.balance-amount
        if self.balance<amount:
            return "Funds Unavaiable"
        else:
            return "Withdrwan successful"
    def __str__(self):
        return (f"Owner details {self.owner},{self.balance}")

act1=Account('Pavithira',1000000)
print(act1)
print(act1.owner)
print(act1.balance)
print(act1.deposit(30000))
print(act1.withdrawn(20000))
print(act1.withdrawn(1000000))

