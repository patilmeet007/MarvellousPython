if __name__ == '__main__':
    x = int(input("Enter number of elements: "))
    list = []



    for i in range(0,x):
        el=int(input("Enter element: "))
        list.append(el)
    min=min(list)



    print(min)

    print("Min of list is", min)

