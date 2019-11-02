if __name__ == '__main__':
    def pattern():
        print("Enter number")
        x=int(input())
        for i in range(0,x):
            for j in range(0,x):
                print("*",end=" ")
            print("")

    pattern()
