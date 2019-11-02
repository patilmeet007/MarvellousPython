def pattern(x):
    for i in range(0,x):
        for j in range(x,i,-1):
            print("*",end="   ")
        print("")



if __name__ == '__main__':
    print("Enter number")
    x = int(input())
    pattern(x)