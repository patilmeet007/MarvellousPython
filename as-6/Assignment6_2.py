class Circle:
    PI=3.14
    def __init__(self):
        self.Radius=0
        self.Area=0
        self.Circum=0

    def Accept(self):
        print("Enter Redius : ")
        self.Radius=float(input())


    def CalculateArea(self):
        self.Area=Circle.PI*(self.Radius**2)

    def CalculateCircumference(self):
        self.Circum = 2*Circle.PI*self.Radius

    def Display(self):
        print(self.Radius)
        print(self.Area)
        print("%.2f"%self.Circum)



def main():
    obj=Circle()
    obj.Accept()
    obj.CalculateArea()
    obj.CalculateCircumference()
    obj.Display()

if __name__ == "__main__" :
    main()
