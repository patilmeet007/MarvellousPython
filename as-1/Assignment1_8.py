if __name__ == '__main__':
    def fun():
        print("Enter number")
        x=int(input())
        while x > 0:
            print("*", end=' ')
            x-=1
    fun()