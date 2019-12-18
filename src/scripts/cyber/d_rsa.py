import sys

def d_rsa(P,Q,E):
    P = int(P)
    Q = int(Q)
    E = int(E)

    N = P*Q
    f = (P-1)*(Q-1)

    a = f
    b = E

    i=0
    D=0
    aa = []
    while(True):
        r = a//b
        c = a % b

        if c == 0:
            D = aa[len(aa)-1]
            break

        if i==0:
            aa.append(r)
        elif i==1:
            aa.append(aa[0]*r+1)
        else:
            aa.append(aa[i-1]*r+aa[i-2])

        a = b
        b = c
        i+=1

    return "D={0}".format(D)

if __name__ == '__main__':
    print(d_rsa(sys.argv[1],sys.argv[2],sys.argv[3]))
    # print(d_rsa(7,13,25))
