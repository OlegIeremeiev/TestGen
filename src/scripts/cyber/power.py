import sys

def power(val1, val2, val3):

    c1 = counter(int(val1))
    c2 = counter(int(val2))
    c3 = counter(int(val3))

    return "{0}, {1}, {2}".format(c1,c2,c3)

def counter(value):

    str = bin(value)[2:]
    ones = str.count('1')
    zeros = str.count('0')

    return max(ones-1,0)*2+zeros

if __name__ == '__main__':
    print(power(43,52,62))
    # print(power(sys.argv[1],sys.argv[2],sys.argv[3]))