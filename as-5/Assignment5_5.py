f=1
def fact(x):
    global f
    if x > 0:
        f=f*x
        x=x-1
        fact(x)
    return f
def main():
    print("Enter the number")
    x = int(input())
    print(fact(x))


if __name__ == "__main__":
    main()
