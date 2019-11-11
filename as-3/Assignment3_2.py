if __name__ == '__main__':
    x = int(input("Enter number of elements: "))
    list = []
    max=0
    for i in range(0,x):
        el=int(input("Enter element: "))
        list.append(el)
        if list[i] > max:
            max=list[i]

    print("Max of list is", max)

