class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        else:
            self.__balance += amount
            print(f"Deposited ${amount}. Balance {self.__balance}")
    
    def withdraw(self, amount):
        finalBalance = self.__balance - amount
        if finalBalance < 0:
            print("Insufficient funds")
        else:
            self.__balance = finalBalance 
            print(f"Withdrew ${amount}. Balance {self.__balance}")
    
    def get_balance(self):
        return self.__balance


if __name__ == "__main__":
    account = BankAccount("oriol", 6874)
    account.deposit(333)
    account.withdraw(7500)
    account.get_balance()
    account.deposit(600)
    account.withdraw(5555)        
    account.get_balance()

