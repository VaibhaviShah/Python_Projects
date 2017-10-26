from abc import ABCMeta, abstractmethod
from random import randint

class Account(metaclass=ABCMeta):

    @abstractmethod
    def createAccount():
        return 0
    @abstractmethod
    def authentication():
        return 0
    @abstractmethod
    def withDraw():
        return 0
    @abstractmethod
    def deposit():
        return 0
    @abstractmethod
    def displayBalance():
        return 0


class SavingsAccount(Account):
    def __init__(self):
        self.savingsAccounts = {}

    def createAccount(self, name, initialDeposit):
        self.accountNumber = randint(10000, 99999)
        self.savingsAccounts[self.accountNumber] = [name, initialDeposit]
        print("Your Account number is: ", self.accountNumber)

    def authentication(self, name, accountNumber):
        if accountNumber in self.savingsAccounts.keys():
            if self.savingsAccounts[accountNumber][0] == name:
                print("Authentication Successful")
                return True
            else:
                print("Authentication Failed")
                return False
        else:
            print("Authentication Failed")
            return False

    def withDraw(self, withdrawalAmount):
        if withdrawalAmount > self.savingsAccounts[self.accountNumber][1]:
            print("Insufficient Balance")
        else:
            self.savingsAccounts[self.accountNumber][1] -= withdrawalAmount
            print("Withdawal successfuk. Available balance: ")
            self.displayBalance()

    def deposit(self, depositAmount):
        self.savingsAccounts[self.accountNumber][1] += depositAmount
        print("Withdrawal successful. Available balance: ")
        self.displayBalance()

    def displayBalance(self):
        print("Availabe balance is: ", self.savingsAccounts[self.accountNumber][1])


savingAccount = SavingsAccount()
while True:
    print("Enter 1 to create a new Account")
    print("Enter 2 to access existing account")
    print("Enter 3 to exit")
    userInput = int(input())
    if userInput is 1:
        name = input("Enter your name: ")
        deposit = int(input("Enter initial deposit amount: "))
        savingAccount.createAccount(name, deposit)
    elif userInput is 2:
        name = input("Enter your name: ")
        account = int(input("Enter your account number: "))
        status = savingAccount.authentication(name, account)
        if status is True:
            while True:
                print("Enter 1 to display balance")
                print("Enter 2 to Withdraw")
                print("Enter 3 to deposit")
                print("Enter 4 to go back to prev menu")
                userChoice = int(input())
                if userChoice is 1:
                    savingAccount.displayBalance()
                elif userChoice is 2:
                    withdraw = int(input("Enter amount to Withdraw: "))
                    savingAccount.withDraw(withdraw)
                elif userChoice is 3:
                    deposit = int(input("Enter amount to Deposit: "))
                    savingAccount.deposit(deposit)
                elif userChoice is 4:
                    break
    elif userInput is 3:
        quit()
