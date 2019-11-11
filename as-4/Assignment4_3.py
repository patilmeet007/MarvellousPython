from functools import reduce

def acceptList():
    list = []
    no=int(input("Enter number of list: "))
    for i in range(no):
        el=int(input("Enter the elements of list:"))
        list.append(el)
    return list

def filFun(n):
    return 70 <= n <= 90

def mapFun(n):
    return n+10

def redFun(n1,n2):
    return n1*n2

def main():
    lst=acceptList()
    print("Entered list is: ",lst)
    filtered=list(filter(filFun,lst))
    print("Filtered list:",filtered)
    mapped=list(map(mapFun,filtered))
    print("Mapped data: ",mapped)
    reduced=reduce(redFun,mapped)
    print("Product is: ",reduced)


if __name__ == '__main__':
    main()
