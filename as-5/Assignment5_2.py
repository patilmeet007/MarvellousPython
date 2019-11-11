i=1
def rec(x):
    global i
    if i <= x:
        print(i,end="  ")
        i=i+1
        rec(x)

def main():

    print("Enter the number")
    x = int(input())
    rec(x)


if __name__ == "__main__":
    main()
