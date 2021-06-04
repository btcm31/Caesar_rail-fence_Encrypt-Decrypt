from itertools import cycle
import math
def saveFile(path, data):
    file = open(path, 'a', encoding = 'utf-8')
    file.writelines(data)
    file.writelines('\n')
    file.close()
def readVocab():
    lines = []
    with open('common_words_list.txt','r') as f:
        lines = f.readlines()
    return (" ".join(lines).replace('\n', '')).split()
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
        text = rail_fenceDecode(ciphertext,Key)
        plain = Caesar_Decode(text,Key)
        test = plain.split()
        i = [j for j in test if j in readVocab()]
        if len(i) >= 10:
            saveFile('hack_plaintext.txt', plain)
            saveFile('hack_key.txt','key : %s'%str(Key))
if __name__=='__main__':
    ciphertext = readFile('ciphertext.txt')
    ciphertext = ''.join(ciphertext)
    option = int(input('Chon giai thuat encrypt (1-Caesar,2-Rail-fence,3-Mix):'))
    if option ==1:
        for key in range(64):
            plain = Caesar_Decode(ciphertext, key)
            test = plain.split()
            i = [j for j in test if j in readVocab()]
            if len(i) >= 10:
                saveFile('hack_plaintext.txt', plain)
                saveFile('hack_key.txt','key : %s'%str(key))
    elif option ==2:
        for key in range(1,len(ciphertext)):
            plain = rail_fenceDecode(ciphertext[:len(ciphertext)-1], key)
            test = plain.split()
            i = [j for j in test if j in readVocab()]
            if len(i) >= 10:
                saveFile('hack_plaintext.txt', plain)
                saveFile('hack_key.txt','key : %s'%str(key))
    elif option ==3:
        plain = multiEncode(ciphertext[:len(ciphertext)-1])