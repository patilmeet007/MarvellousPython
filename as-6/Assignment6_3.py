class Arithmetic:
    PI=3.14
    def __init__(self):
        self.Value1=0
        self.Value2=0


    def Accept(self):
        print("Enter 1st number : ")
        self.Value1=int(input())
        print("Enter 2nd number : ")
        self.Value2 = int(input())

    def Addition(self):
        return self.Value1+self.Value2

    def Subtraction(self):
        return self.Value1-self.Value2

    def Multiplication(self):
        return self.Value1*self.Value2

    def Division(self):
        return self.Value1/self.Value2


def main():
    obj=Arithmetic()
    print(obj.Accept())
    print(obj.Addition())
    print(obj.Subtraction())
    print(obj.Multiplication())
    print(obj.Division())

if __name__ == "__main__" :
    main()
