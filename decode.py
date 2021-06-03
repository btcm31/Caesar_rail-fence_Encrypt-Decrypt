from itertools import cycle
import math
def saveFile(path, data):
    file = open(path, 'a', encoding = 'utf-8')
    file.writelines(data)
    file.writelines('\n')
    file.close()

def readFile(path):
    lines = []
    with open(path,'r') as f:
        lines = f.readlines()
    return lines
def Caesar_Decode(ciphertext, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789\n '
    decrypted = ""
    for a in ciphertext:
        x = (alphabet.index(a)-key)
        decrypted += alphabet[x if (x>=0 and x<64) else (x+64*(math.ceil(abs(x/64))) if x<0 else x%64)]
    return decrypted
def rail_pattern(n):
    r = list(range(n))
    return cycle(r + r[-2:0:-1])
def rail_fenceDecode(ciphertext, key):
    p = rail_pattern(key)
    indexes = sorted(range(len(ciphertext)), key=lambda i: next(p))
    result = [''] * len(ciphertext)
    for i, c in zip(indexes, ciphertext):
        result[i] = c
    return ''.join(result)
def multiEncode(ciphertext):
    for Key in range(1,len(ciphertext)):
        #for caesarKey in range(0,64):
        saveFile('hack_plaintext.txt','==============%s=================='%(str(Key)))
        text = rail_fenceDecode(ciphertext,Key)
        plain = Caesar_Decode(text,Key)
        saveFile('hack_plaintext.txt', plain)
if __name__=='__main__':
    ciphertext = readFile('ciphertext.txt')
    ciphertext = ''.join(ciphertext)
    option = int(input('Chon giai thuat encrypt (1-Caesar,2-Rail-fence,3-Mix):'))
    if option ==1:
        for key in range(64):
            saveFile('hack_plaintext.txt','==============%s=================='%str(key))
            plain = Caesar_Decode(ciphertext, key)
            saveFile('hack_plaintext.txt', plain)
    elif option ==2:
        print(ord(ciphertext[len(ciphertext)-1]))
        for key in range(1,len(ciphertext)):
            saveFile('hack_plaintext.txt','==============%s=================='%str(key))
            plain = rail_fenceDecode(ciphertext[:len(ciphertext)-1], key)
            saveFile('hack_plaintext.txt', plain)
    elif option ==3:
        plain = multiEncode(ciphertext[:len(ciphertext)-1])