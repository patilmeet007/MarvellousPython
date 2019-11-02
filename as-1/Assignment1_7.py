if __name__ == '__main__':
    def fun():
        print("Enter number")
        x = int(input())
        if x % 5 == 0:
            return True
        else:
            return False
    print(fun())