def CaesarCipherChar(c, k):
    if 'A' <= c <= 'Z':
        return chr((ord(c) - ord('A') + k) % 26 + ord('A'))
    if 'a' <= c <= 'z':
        return chr((ord(c) - ord('a') + k) % 26 + ord('a'))
    else:
        return c

def CaesarCipher(s, k):
    res = []
    for el in s:
        res.append(CaesarCipherChar(el, k))
        
    return ''.join(res)
