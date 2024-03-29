#!/usr/bin/python

# SINGLE BYTE XOR

import string

def doXOR(cipher, char):
    plainText = b""
    for byte in cipher:
        plainText += bytes([byte ^ char])
    return str(plainText)[2:-1]

def display(dct, count, cipher):
    for ch in list(dct)[0:count]:
        s = doXOR(cipher, ord(ch))
        print (ch, ':', str(score(s))[:4] , ':', s )

def score(text):
    fqTable = {
        'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
        'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
        'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
        'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
    }
    score = 0
    for char in text.lower():
        if char in string.ascii_lowercase:
            score+=fqTable.get(char)
    return score

def main(cipherText):
    cipherText = bytes.fromhex(cipherText)
    dct = {}
    for i in range(65, 122):
        if chr(i) in string.ascii_letters:
            xor = doXOR(cipherText, i)
            dct[chr(i)] = [score(xor), xor]
    dct = dict(reversed(sorted(dct.items(), key=lambda el: el[1])))
    display (dct, 6, cipherText)

if __name__ == "__main__":
    main("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
