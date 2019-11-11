from MarvellousNum import *

def main():
    x = int(input("Enter number of elements: "))
    list = ListPrime(x)
    prime=chkPrime(list)
    print("Addition of Prime numbers is ",primeAdd(prime))

if __name__ == '__main__':
    main()





