from functools import reduce

def acceptList():
    list = []
    no=int(input("Enter number of list: "))
    for i in range(no):
        el=int(input("Enter the elements of list:"))
        list.append(el)
    return list

def isPrime(x):
    flag=0
    for i in range(2,(x//2)+1):
        if x % i == 0:
            flag=1
            break

    if flag != 1:
        return x

def redFun(no1,no2):
    if no1>no2:
        return no1
    else:
        return no2

def main():
    lst=acceptList()
    print("Entered list is: ",lst)
    filtered=list(filter(isPrime,lst))
    print("Filtered Prime no list:",filtered)
    mapped=list(map(lambda no:no*2,filtered))
    print("Mapped data: ",mapped)
    reduced=reduce(redFun,mapped)
    print("Max is: ",reduced)


if __name__ == '__main__':
    main()
