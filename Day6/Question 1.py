class bank_account():
    def __init__(self,ownerName,Balance):
        self.ownerName = ownerName
        self.Balance = Balance

    def deposit(self):
        print("Hello ", self.ownerName)
        
        deposit_amount = int(input("Enter amount to be deposited: ")) 
        self.Balance += deposit_amount
        print("\n Amount deposited ",self.Balance) 

    def withdraw(self):
        withdraw_amount = int(input("Enter amount to be withdraw: ")) 
        if self.Balance >= withdraw_amount:
            self.Balance -= withdraw_amount
            print("\n Amount creadited ", withdraw_amount)  
        else:
            print("\n Insufficient balance")    


obj = bank_account("vivek",10000)
obj.deposit()
obj.withdraw()