import threading

def small(str):
    count = 0
    for i in str:
        if i.islower() == True:
            count = count + 1
    print("lower",count)
    print("Thread Name:",threading.currentThread().getName())
    print("Thread t1 id :",threading.get_ident())

def capital(str):
    count = 0
    for i in str:
        if i.isupper() == True:
            count = count + 1
    print("upper",count)
    print("Thread Name:",threading.currentThread().getName())
    print("Thread t2 id :",threading.get_ident())
def digits(str):
    count = 0
    for i in str:
        if i.isdigit() == True:
            count = count + 1

    print("digits",count)
    print("Thread Name:",threading.currentThread().getName())
    print("Thread T3 id :",threading.get_ident())
def main():


    t1 = threading.Thread(target=small, args=("asDFGH123",))
    t2 = threading.Thread(target=capital, args=("asDFGH123",))
    t3 = threading.Thread(target=digits, args=("asDFGH786",))
    t1.start()
    t2.start()
    t3.start()


    t1.join()
    t2.join()
    t3.join()


if __name__ == "__main__":
    main()
