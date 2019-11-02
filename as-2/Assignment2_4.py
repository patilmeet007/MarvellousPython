if __name__ == '__main__':
    def fact():
        print("Enter number")
        x=int(input())
        add=0
        for i in range(1,x):
            if x % i == 0:
                add+=i
        print(add)

    fact()
