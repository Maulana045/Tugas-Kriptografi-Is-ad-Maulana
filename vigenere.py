def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key_length = len(key)
    key_int = [ord(k.upper()) - 65 for k in key]
    
    for i, char in enumerate(plaintext):
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            shifted = (ord(char) - offset + key_int[i % key_length]) % 26
            ciphertext += chr(shifted + offset)
        else:
            ciphertext += char
    return ciphertext.replace(" ", "")

def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key_length = len(key)
    key_int = [ord(k.upper()) - 65 for k in key]
    
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            shifted = (ord(char) - offset - key_int[i % key_length]) % 26
            plaintext += chr(shifted + offset)
        else:
            plaintext += char
    return plaintext
