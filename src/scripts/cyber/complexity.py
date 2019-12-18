
def complexity(str):
    U=0

    ln = len(str)
    if (ln >= 5 and ln <=7):
        U+=6
    elif (ln >= 8 and ln <=15):
        U+=12
    elif (ln > 16):
        U+=18

    up = 0
    down = 0
    number = 0
    spec = 0
    for symbol in str:
        if symbol.isnumeric():
            number+=1
        elif symbol in "#$%@":
            spec+=1
        elif symbol.isupper():
            up +=1
        elif symbol.islower():
            down+=1

    if up > 0 and down > 0:
        U+=7
    elif up > 0 or down > 0:
        U+=5

    if number in range(1,2):
        U+=5
    elif number >=3:
        U+=7

    if spec == 1:
        U+=5
    elif spec > 1:
        U+=10

    sm = 0
    for x in (up,down,number,spec):
        if x > 0:
            sm+=1

    if sm == 4:
        U+=6
    elif sm == 3:
        U+=4


    return U

if __name__ == '__main__':
    print(complexity("1234"))

