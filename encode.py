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

def CaesarEncode(plaintext, n):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789\n '
    cipher = ''
    for a in plaintext:
        cipher += alphabet[(alphabet.index(a) + n) % 64]
    return cipher

def rail_fenceEncode(text, rails):
    m = (rails - 1) * 2
    out = ""
    for i in range(rails):
        if i % (rails - 1) == 0:
            out += text[i::m]
        else:
            char_pairs = zip(text[i::m], list(text[m-i::m]) + [''])
            out += ''.join(map(''.join, char_pairs))
    return out


if __name__ == '__main__':
    plaintext = readFile('plaintext.txt')
    plaintext = ''.join(plaintext)
    option = int(input('Moi chon giai thuat encrypt (1-Caesar,2-Rail-fence,3-Mix):'))
    if option ==1:
        key = int(input('Moi nhap key :')) 
        cipher = CaesarEncode(plaintext, key)
        saveFile('ciphertext.txt', cipher)
        key = 'Do dich chuyen Caesar cipher la: %s'%str(key)
        saveFile('key.txt', key)
    elif option ==2:
        key = int(input('Moi nhap key :'))
        cipher = rail_fenceEncode(plaintext, key)
        saveFile('ciphertext.txt', cipher)
        key = 'Key cua Rail-fence la: %s'%str(key)
        saveFile('key.txt', key)
    elif option ==3:
        key = int(input('Moi nhap key :')) 
        cipherofCeasar = CaesarEncode(plaintext, key)
        cipher = rail_fenceEncode(cipherofCeasar, key)
        saveFile('ciphertext.txt', cipher)
        key = 'Key cua ma hoa nhan: %s'%str(key)
        saveFile('key.txt', key)


