import os, sys

def onetime_note(message):

    mess_bytes = message.encode("utf-8")
    # one-time note generation
    key = os.urandom(len(mess_bytes))
    # encryption stage
    cypher_bytes = bytearray(len(mess_bytes))
    for i in range(len(mess_bytes)):
        cypher_bytes[i] = mess_bytes[i] ^ key[i]

    # decryption stage
    decrypt = bytearray()
    for i in range(len(mess_bytes)):
        decrypt.append( cypher_bytes[i] ^ key[i] )
    message_d = decrypt.decode("utf-8")
    return message_d

def onetime_note_printed(message):

    mess_bytes = message.encode("utf-8")
    print('message is:\n{}'.format(message))

    # one-time note generation
    key = os.urandom(len(mess_bytes))
    print('generated key: {}\nor as string:'.format(key))
    sys.stdout.buffer.write(key)

    # encryption stage
    cypher_bytes = bytearray(len(mess_bytes))
    for i in range(len(mess_bytes)):
        cypher_bytes[i] = mess_bytes[i] ^ key[i]
    print()
    print('cypher is:')
    print()
    sys.stdout.buffer.write(cypher_bytes)

    # decryption stage
    decode = bytearray(len(mess_bytes))
    for i in range(len(mess_bytes)):
        decode[i] = cypher_bytes[i] ^ key[i]

    print('\ndecrypted message is:\n{}'.format(decode.decode("utf-8")))


if __name__ == '__main__':
    res = onetime_note_printed('some Custom StRiNg')
    # res = onetime_note_printed('одна слуЧайНая строка')
    # print('Result: ' + res)
