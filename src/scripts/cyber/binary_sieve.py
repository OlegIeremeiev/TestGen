import sys, math

def binary_sieve(val):
    N = int(val)

    root = math.floor(math.sqrt(N))

    easy=(2,3,5,7,11,13)
    M = 2
    i=0
    while (M<N):
        i+=1
        M*=easy[i]

    # x
    # while(True)
    #
    # z =



if __name__ == '__main__':
    print(binary_sieve(377))
    # print(binary_sieve(sys.argv[1]))