class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self,accountBalance,accName):
        self.accountBalance=accountBalance
        self.accName=accName
        print(f"\n Account'{accName}. created.\nBalance=${self.accountBalance}")

    def getBalance(self):
        print(f"\nAccount'{self.accName}'balance=${self.accountBalance}")   

    def deposit(self,amount):
        self.accountBalance+=amount  
        print(f"\n Deposit complete.")   
        self.getBalance() 

    def viableTransaction(self,amount):
        if self.accountBalance >=amount:
            return
        else:
            raise BalanceException(
                f"\n Sorry ,account'{self.accName}'only has a balance of ${self.accountBalance}"
            )
        
    def withdraw(self,amount):  
        try:
            self.viableTransaction(amount)
            self.accountBalance =self.accountBalance-amount  
            print("\n Withdraw  complete.")  
            self.getBalance()
        except BalanceException as error:
            print(f'\n Withdraw interrupted:{error}')  


    def transfer(self,amount,account):
        try:
            print('\n**********\n\n Beginning Transfer..')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)    
            print('\n Transfer complete! \n\n**********')      

        except BalanceException as error:
            print(f'\n Transfer interrupted.{error}')    


class IntersetRewardsAcc(BankAccount):
    def deposit(self,amount):
        self.accountBalance = self.accountBalance + (amount*1.05)
        print("\nDeposite complete.")
        self.getBalance()


class SavingsAcc(IntersetRewardsAcc):

    def __init__(self,accountBalance,accName):
        super().__init__(accountBalance,accName)
        self.fee= 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount+self.fee)
            self.accountBalance=self.accountBalance -(amount+self.fee)
            print("\n Withdraw completed.")
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted:{error}')    

            