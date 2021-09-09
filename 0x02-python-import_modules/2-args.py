#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv) - 1
    print("{:d} ".format(count), end="")
    if count == 0:
        print("argument.")
    else:
        if count == 1:
            print("argument:".format(count))
        else:
            print("arguments:".format(count))
        for i in range(1, len(sys.argv)):
            print("{:d}: {}".format(i, sys.argv[i]))
