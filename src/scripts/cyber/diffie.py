import sys

def diffie(v,n,x,y):
    v = int(v)
    n = int(n)
    x = int(x)
    y = int(y)
    ans = (v**x)**y % n
    return "{}".format(ans)

if __name__ == '__main__':
    print(diffie(5,11,3,4))