class Customer:
    bankName="Durga Bank"
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Deposited SucessFully")
        print("Balance After Deposit =",self.balance)
    def withdraw(self,amount):
        if(amount>self.balance):
            print("Insufficient Fund ,Please deposit First:Balance=",self.balance)
        else:
            self.balance=self.balance-amount
            print("Withdraw SuccessFully")
            print("Balance After Withdraw In Your Account is:",self.balance)
print("Welcome To ",Customer.bankName)
name=input("Enter Name:")
C=Customer(name)
while True:
    print("D=Deposit\nW=Withdraw\nE=Exit")
    option=input("Enter Your Choice:From Above Menu:")
    if(option.lower()=='d'):
        amount=float(input("Enter Amount To Deposit:"))
        C.deposit(amount)
    elif(option.lower()=='w'):
        amount=float(input("Enter Amount To Withdraw:"))
        C.withdraw(amount)
    elif(option=='e'):
        print("Thanks For Banking With Us ,Have A Great Day:")
        break
    else:
        print("Invalid Option,Please Choose Valid Option")    
        