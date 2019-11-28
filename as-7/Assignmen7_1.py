class BookStore:
    NoOfBooks=0
    def __init__(self,n,a):
        self.Name=n
        self.Author=a
        BookStore.NoOfBooks=BookStore.NoOfBooks +1

    def Display(self):
        print("Book Name: ",self.Name)
        print("Book Author: ",self.Author)
        print("No of books is: ",BookStore.NoOfBooks)


def main():
    Obj1 = BookStore("Linux System Programming","Robert Love")
    Obj1.Display()

    Obj2 = BookStore("C Programming","Dennis Ritchie")
    Obj2.Display()

if __name__ == "__main__" :
    main()
