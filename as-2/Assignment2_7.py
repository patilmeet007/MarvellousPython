def square(x):
    for i in range(1,x+1):
        for j in range(1,x+1,1):
            print(j,end="   ")
        print("")



if __name__ == '__main__':
    print("Enter number")
    x = int(input())
    square(x)