import sys
import shutil
import io
from os.path import realpath


def FileCopy(filename):
    f1 = realpath(filename)
    f2 = open("Demo.txt","r+")
    f2path = realpath("Demo.txt")
    shutil.copy(f1,f2path)
    print("Copied..")
    print(f2.read())
    f2.close()

def main():
    print("-------Created by Amit Patil---------")
    print("Script Name:", sys.argv[0])
    print("Enter file name:")
    FileName = input()

    try:
        FileCopy(FileName)

    except Exception:
        print("Exception")

if __name__ == "__main__":
    main()