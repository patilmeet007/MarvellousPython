import threading
i = 1
j = 1
def display():
    global i
    if i <= 50:
        print(i)
        i = i +1
        display()

def rdisplay():
     for i in range(50,0,-1):
        print(i)



def main():


    t1 = threading.Thread(target=display, args=())
    t2 = threading.Thread(target=rdisplay, args=())

    t1.start()
    t1.join()
    t2.start()
    t2.join()



if __name__ == "__main__":
    main()
