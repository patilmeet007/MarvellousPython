import threading

def factor(n):
    fact= []
    for i in range(1,n):
        if n % i == 0:
            fact.append(i)
    return fact


def oddfactor(n):
    ofact= []
    ofact=factor(n)
    print("Factors",ofact)

    add = 0
    for i in ofact:
        if i % 2 != 0:
            print(i)
            add = add + i
    print("Addition of odd is:",add)


def evenfactor(n):
    efact= []
    efact=factor(n)
    print("Factors:",efact)

    eadd = 0
    for j in efact:
        if j % 2 == 0:
            print(j)
            eadd = eadd + j
    print("Addition of even is:",eadd)


def main():
    t1 = threading.Thread(target=evenfactor, args=(18,))
    t2 = threading.Thread(target=oddfactor, args=(21,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == "__main__":
    main()
    print("exit from main")