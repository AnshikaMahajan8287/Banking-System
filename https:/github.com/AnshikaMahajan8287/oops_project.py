from bankingsystem import *



Dave=BankAccount(1000,"Dave")

Sara=BankAccount(2000,"Sara")

Dave.getBalance()
Dave.deposit(1000)
Dave.withdraw(10000)

Dave.transfer(10000,Sara)


Jim=IntersetRewardsAcc(1000,"Jim")

Jim.getBalance()
Jim.deposit(100)
Jim.transfer(100,Dave)


Blaze=SavingsAcc(1000,"Blaze")


Blaze.getBalance
Blaze.deposit(100)
Blaze.withdraw(1000)
Blaze.transfer(1000,Sara)





