if __name__ == '__main__':
    x = int(input("Enter number of elements: "))
    list = []
    sum=0
    for i in range(0,x):
        el=int(input("Enter element: "))
        list.append(el)
        sum=sum+list[i]
    print("Sum of list is", sum)

