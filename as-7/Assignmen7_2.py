class BankAccount:
    ROI=10.5
    def __init__(self,n,a):
        self.Name=n
        self.Amount=a


    def Display(self):
        print("Book Name: ",self.Name)
        print("Book Amount: ",self.Amount)



    def Deposit(self,a):
        self.Amount =self.Amount + a

    def Withdraw(self,a):
        self.Amount = self.Amount - a

    def CalculateIntrest(self):
        self.Amount = self.Amount + (self.Amount*BankAccount.ROI/100)


def main():
    Obj1 = BankAccount("Amit",5000)
    Obj1.Deposit(1000)
    Obj1.Withdraw(500)
    Obj1.CalculateIntrest()
    Obj1.Display()
    Obj2 = BankAccount("Sayali", 5000)
    Obj2.Deposit(1000)
    Obj2.Withdraw(500)
    Obj2.CalculateIntrest()
    Obj2.Display()

if __name__ == "__main__" :
    main()
