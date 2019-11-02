def pyramid(x):
    for i in range(1,x+1):
        for j in range(1,i+1,1):
            print(j,end="   ")
        print("")


if __name__ == '__main__':
    print("Enter number")
    x = int(input())
    pyramid(x)