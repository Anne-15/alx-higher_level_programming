#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    number = len(sys.args)
    if number == 1:
        print("{} arguments".format(number - 1))
    elif number == 2:
        print("{} arguments".format(number - 1))
    else:
        print("{} arguments".format(number - 1))

    for i in range(1, number):
        print("{}: {}".fomrat(i, sys.argv[i]))
