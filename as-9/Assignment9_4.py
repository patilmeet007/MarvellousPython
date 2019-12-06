import sys
import filecmp


def FileCom(f1,f2):
    print(f1)
    print(f2)
    print(filecmp.cmp(f1,f2))

def main():
    print("-------Created by Amit Patil---------")
    print ("Script Name:", sys.argv[0])
    f1 = sys.argv[1]
    f2 = sys.argv[2]
    try:
        FileCom(f1,f2)

    except Exception:
        print("Exception")

if __name__ == "__main__":
    main()