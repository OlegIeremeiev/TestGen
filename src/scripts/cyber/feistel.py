import sys

def feistel(x1,x2,k1,k2):
    x1 = int(x1)
    x2 = int(x2)
    k1 = int(k1)
    k2 = int(k2)

    f1 = (x1 * k1) % 256
    x2 = x2 ^ f1

    tmp = x1
    x1 = x2
    x2 = tmp

    f2 = (x1 * k2) % 256
    x2 = x2 ^ f2

    z1 = x2
    z2 = x1
    return "{0} & {1}".format(z1,z2)

if __name__ == '__main__':
    print(feistel(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]))
