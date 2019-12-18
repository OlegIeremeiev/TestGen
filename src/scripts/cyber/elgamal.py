import sys

def elgamal(N, g, y, k, a, y2):
    N=int(N)
    g=int(g)
    y=int(y)
    k=int(k)
    a=int(a)
    y2=int(y2)

    y1 = g**k % N
    M = (y1**a % N) ^ y2
    return "M={0} & y1={1}".format(M,y1)

if __name__ == '__main__':
    # print(elgamal(13,7,5,3,3,13))
    print(elgamal(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],))