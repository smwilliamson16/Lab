class Account:
    balance = 0

    def __init__(self, name):
        self.__account_name = name
        self.__account_balance = Account.balance
    
    def deposit(self, amount):       
        if amount > 0: 
            self.__account_balance = self.__account_balance + amount
            return True
        else:
            return False
    
    def withdraw(self, amount):        
        if amount <= self.__account_balance and amount > 0:
            self.__account_balance = self.__account_balance - amount
            return True
        else:
            return False
    
    def get_balance(self):
        return self.__account_balance
    
    def get_name(self):
        return self.__account_name

