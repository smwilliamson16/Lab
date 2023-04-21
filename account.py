class Account:
    balance = 0

    def __init__(self, name:str) -> None:
        """
        Function to set up object
        :param name: Account name
        """
        self.__account_name = name
        self.__account_balance = Account.balance
        
    
    def deposit(self, amount:float) -> float:
        """
        Function to add deposit amount to account balance
        :param name: amount
        :return: value of (account balance + amount)
        """
        if amount > 0: 
            self.__account_balance = self.__account_balance + amount
            return True
        else:
            return False
    
    def withdraw(self, amount:float) -> float:
        """
        Function to add withdraw amount from account balance
        :param name: amount
        :return: value of (account balance - amount)
        """
        if amount <= self.__account_balance and amount > 0:
            self.__account_balance = self.__account_balance - amount
            return True
        else:
            return False
    
    def get_balance(self) -> float:
        """
        Function to access account balance
        :return: value of account balance
        """
        return self.__account_balance
    
    def get_name(self) -> str:
        """
        Function to access account name
        :return: name of account
        """
        return self.__account_name

