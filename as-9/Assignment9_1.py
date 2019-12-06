import sys
import os

def FileExists(filename):
    return os.path.isfile(filename)


def main():
    print("-------Created by Amit Patil---------")
    print("Script Name:", sys.argv[0])
    print("Enter file name:")
    FileName = str(input())

    try:
        RetVal = FileExists(FileName)
        if RetVal == True:
            print(FileName,"is Exist")
        else:
            print(FileName, "is not Exist")
    except Exception:
        print("Exception")



if __name__ == "__main__":
    main()