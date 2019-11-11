def searchnum(lst):
    print("Enter number to check frequency")
    y = int(input())
    count = 0
    for i in range(0, x):
        if lst[i] == y:
            count = count + 1
    print("frequency of number is", count)


def acceptlist():
    list = []
    for i in range(0,x):
        el=int(input("Enter elements of list: "))
        list.append(el)
    searchnum(list)




if __name__ == '__main__':
    x = int(input("Enter number of elements: "))
    acceptlist()



