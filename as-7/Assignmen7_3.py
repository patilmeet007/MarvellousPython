class Numbers:

    def __init__(self,n):
        self.Value = n

    def ChkPrime(self):
        flag=0
        for i in range(2,int(self.Value/2)+1):
            if self.Value % i == 0:
                flag=1
                break
        if flag == 0:
            return True
        else:
            return False

    def ChkPerfect(self):
        sum=self.SumFactors()
        if sum == self.Value:
            return True
        else:
            return False

    def SumFactors(self):
        sum = 0
        for k in Fact:
            sum = sum + k
        return sum

    def Factors(self):
        global Fact
        Fact = []
        for j in range(1,self.Value):
            if self.Value % j == 0:
                Fact.append(j)
        return Fact

def main():
    Obj1 = Numbers(6)
    print(Obj1.ChkPrime())
    f=Obj1.Factors()
    print(f)
    s=Obj1.SumFactors()
    print(s)
    print(Obj1.ChkPerfect())


if __name__ == "__main__" :
    main()
