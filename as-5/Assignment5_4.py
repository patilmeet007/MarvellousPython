
def addRec(x):
    add=0
    for i in x:
        add=add+int(i)
    print(add)

def main():
    print("Enter the number")
    x = input()
    addRec(x)


if __name__ == "__main__":
    main()
