from functools import reduce

def acceptList():
    list = []
    no=int(input("Enter number of list: "))
    for i in range(no):
        el=int(input("Enter the elements of list:"))
        list.append(el)
    return list

def main():
    lst=acceptList()
    print("Entered list is: ",lst)
    filtered=list(filter(lambda n:not(n%2),lst))
    print("Filtered Even no list:",filtered)
    mapped=list(map(lambda no:no*no,filtered))
    print("Mapped data: ",mapped)
    reduced=reduce(lambda no1,no2:no1+no2,mapped)
    print("Addition is: ",reduced)


if __name__ == '__main__':
    main()
