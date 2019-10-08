import sys


def caesar(cypher):
    # alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    txt = ''
    for x in range(-3, 4):
        for cyr in cypher:
            shift = (ord(cyr)-ord('А') + x) % 32
            txt += chr(ord('А') + shift)
        txt += ' / '
    print(txt)


if __name__ == '__main__':
    caesar(sys.argv[1])
