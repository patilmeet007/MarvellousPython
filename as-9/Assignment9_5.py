import sys

def FileFreq(f1,f2):
    count = 0
    fobj = open(f1,"r")
    data = fobj.read()

    for word in data.split():
        if word == f2:
            count = count + 1
    print("WORD COUNT IS",+count)
def main():
    print("-------Created by Amit Patil---------")
    print ("Script Name:", sys.argv[0])
    file = input("Enter filename: ")
    str = input("Enter word: ")
    try:
        FileFreq(file,str)

    except Exception:
        print("Exception")

if __name__ == "__main__":
    main()