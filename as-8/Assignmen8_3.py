import threading

def Oddlist(n):
    oadd = 0
    for i in n:
        if i % 2 != 0:
            print(i)
            oadd = oadd + i
    print("Odd number Addition:",oadd)



def Evenlist(n):
    Eadd = 0
    for j in n:
        if j % 2 == 0:
            print(j)
            Eadd = Eadd + j
    print("Even number Addition:", Eadd)

def main():
    list = [10,20,32,23,52,54,55,65,85,92,98]

    t1 = threading.Thread(target=Evenlist, args=(list,))
    t2 = threading.Thread(target=Oddlist, args=(list,))
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    
if __name__ == "__main__":
    main()
    print("exit from main")