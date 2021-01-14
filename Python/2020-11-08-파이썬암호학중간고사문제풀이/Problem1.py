import re
import os

ENC = 0
DEC = 1
BASEDIR = os.path.realpath(os.path.dirname(__file__))

def makeDisk(k1, k2):
   
    enc_disk = {}
    dec_disk = {}

    for i in range(26):
        enc_i = (k1*i+k2)%26
        enc_ascii = enc_i + 65
        enc_disk[chr(i+65)] = chr(enc_ascii)
        dec_disk[chr(enc_ascii)] = chr(i+65)

    return enc_disk, dec_disk

def affine(msg, k1, k2, mode):

    ret = ''
    msg = msg.upper()
    enc_disk, dec_disk = makeDisk(k1, k2)

    if enc_disk is None:
        return ret

    if mode is ENC:
        disk = enc_disk
    if mode is DEC:
        disk = dec_disk

    for c in msg:
        if c in disk:
            ret += disk[c]
        else:
            ret += c
    return ret

def readFile(filename):
    f = open(os.path.join(BASEDIR, filename), mode="r", encoding="utf-8")
    contents = f.read()
    f.close
    return contents

def writeFile(contents, filename):
    f = open(os.path.join(BASEDIR, filename), mode="w", encoding="utf-8")
    f.write(contents)
    f.close()

def main():
    k1, k2 = 3, 10
    msg = readFile("plaintext.txt")
    msg = re.sub('[-=.#/?:$}]', '', msg)
    msg = msg.replace(' ', '').replace('’', '')
    msg = affine(msg, k1, k2, ENC)
    writeFile(msg, "encryption.txt")

    msg = affine(msg, k1, k2, DEC)
    writeFile(msg, "decryption.txt")
    
if __name__ == '__main__':
    main()