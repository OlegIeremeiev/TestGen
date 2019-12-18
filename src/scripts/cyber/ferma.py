import sys
import math


def ferma(val):
    val = int(val)

    root = math.ceil(math.sqrt(val))

    x=root
    while (True):
        y = math.sqrt(x**2-val)
        if y.is_integer():
            break
        x+=1
    return "{0} x {1}".format(int(x-y),int(x+y))


if __name__ == '__main__':
    # print(ferma(3337))
    print(ferma(sys.argv[1]))