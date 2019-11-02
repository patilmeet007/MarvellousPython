def number(x):
    add = 0
    for i in x:
        add=add+int(i)
    return add


if __name__ == '__main__':
    print("Enter number")
    x = input()
    print(number(x))