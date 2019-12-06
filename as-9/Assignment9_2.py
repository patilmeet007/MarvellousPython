import sys


def FileDisplay(filename):
    fobj = open(filename,"r")
    print(fobj.read())

def main():
    print("-------Created by Amit Patil---------")
    print("Script Name:", sys.argv[0])
    print("Enter file name:")
    FileName = input()

    try:
        FileDisplay(FileName)

    except Exception:
        print("Exception")

if __name__ == "__main__":
    main()