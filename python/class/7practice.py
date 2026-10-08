#create Account class 
# with class attribute as bank name, address
# with object attribute as  balance and accunt nuber 
# create methods for credit, debit and printing the balance

class Account :
    bank_name="NIMB"
    address="kathmandu"
    def __init__(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number
    def credit(self, amount):
       self.balance = self.balance+amount 

    def debit(self, amount):
        self.balance = self.balance-amount

    def get_balance(self):
        return self.balance

obj1 = Account(1000, "1")
print(obj1.credit(1000))
print(obj1.get_balance())


obj2 = Account(10,"2")
print(obj2.credit(1000))
print(obj2.get_balance())