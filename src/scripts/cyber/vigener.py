import sys
def vigener(message,key):
    # message = input('message:')
    # key = input('key:')
    keyindex = 0
    cypher = ''
    for i in range(0,len(message)):
        if keyindex >=len(key):
            keyindex = 0

        val1 = ord(message[i])
        val2 = ord(key[keyindex])
        val3 = ord('A')
        val = (val1 + val2 - 2 * val3) % 26
        cypher += chr(val + ord('A'))
        keyindex += 1
    return cypher

if __name__ == '__main__':
    res = vigener(sys.argv[1],sys.argv[2])
    print('Result: ' + res)