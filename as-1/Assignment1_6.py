if __name__ == '__main__':
    def fun():
        print("Enter number")
        a=int(input())
        if a > 0:
            print(a,"is positive")
        elif a < 0:
            print(a,"is negative")
        else:
            print("number is zero")
    fun()
