import sys

def nod(x,y):
    a = max(int(x),int(y))
    b = min(int(x),int(y))

    while(True):
        r = a//b
        c = a % b

        if c == 0:
            break

        a = b
        b = c

    return "{0}".format(b)

if __name__ == '__main__':
    # print(nod(81161,43657))
    print(nod(sys.argv[1],sys.argv[2]))