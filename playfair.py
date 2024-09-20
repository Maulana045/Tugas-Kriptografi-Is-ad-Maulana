def preprocess(text):
    text = text.upper().replace('J', 'I')
    processed = ""
    for char in text:
        if char.isalpha():
            processed += char
            
    i = 0
    pairs = []
    while i < len(processed):
        a = processed[i]
        b = 'X' if (i + 1 == len(processed)) else processed[i + 1]
        if a == b:
            pairs.append(a + 'X')
            i += 1
        else:
            pairs.append(a + b)
            i += 2
    return pairs

def generate_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = ''.join(sorted(set(key.upper().replace('J', 'I')), key=key.upper().replace('J', 'I').index))
    matrix = key + ''.join([c for c in alphabet if c not in key])
    return [list(matrix[i:i+5]) for i in range(0, 25, 5)]

def find_position(matrix, char):
    for row in matrix:
        if char in row:
            return matrix.index(row), row.index(char)
    return None

def playfair_encrypt(plaintext, key):
    pairs = preprocess(plaintext)
    matrix = generate_matrix(key)
    ciphertext = ""
    for pair in pairs:
        row1, col1 = find_position(matrix, pair[0])
        row2, col2 = find_position(matrix, pair[1])
        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5]
            ciphertext += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1]
            ciphertext += matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]
    return ciphertext

def playfair_decrypt(ciphertext, key):
    pairs = preprocess(ciphertext)
    matrix = generate_matrix(key)
    plaintext = ""
    for pair in pairs:
        row1, col1 = find_position(matrix, pair[0])
        row2, col2 = find_position(matrix, pair[1])
        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5]
            plaintext += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1]
            plaintext += matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2]
            plaintext += matrix[row2][col1]
    return plaintext.replace('X', '')
