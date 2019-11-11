def rec(x):
    if x > 0:
        print(x,end="  ")
        x=x-1
        rec(x)

def main():
    print("Enter the number")
    x = int(input())
    rec(x)


if __name__ == "__main__":
    main()
