import threading

def odd():
    counter = 0
    i = 0
    while counter < 10:

        if i % 2 != 0:
            counter = counter +1
            print(i)
        i = i + 1


def even():
    counter = 0
    i = 0
    while counter < 10:

        if i % 2 == 0:
            counter = counter +1
            print(i)
        i = i + 1


def main():
    t1 = threading.Thread(target=even, args=())
    t2 = threading.Thread(target=odd, args=())
    t1.start()
    t2.start()


if __name__ == "__main__":
    main()