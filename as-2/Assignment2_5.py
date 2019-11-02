def prime(x):
    flag=0

    for i in range(2,x):
        if x % i == 0:
            flag=1
            break
    return flag


if __name__ == '__main__':
    print("Enter number")
    x = int(input())

    if prime(x) == 1:
        print(x,"is not prime")
    elif x == 1:
        print("Enter valid number")
    else:
        print(x,"is prime number")

