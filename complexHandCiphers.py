import re

'''Double Transposition'''
def double_transposition_encrypt(plaintext, key1, key2):
    # Converts plaintext and keys to lowercase letters only
    plaintext = re.sub("[^a-z]", "", plaintext.lower())
    key1 = re.sub("[^a-z]", "", key1.lower())
    key2 = re.sub("[^a-z]", "", key2.lower())

    # Initializes ciphertext and keylength for the alg
    ciphertext = ""
    key_length = len(key1)

    # Chunks plaintext into blocks to be manipulated into ciphertext
    blocks = [plaintext[i:i+key_length] for i in range(0, len(plaintext), key_length)]

    # Sorts key in order to compare position placement and converts original key into a list
    sorted_key = sorted(key1)
    key1 = list(key1)
    for i in range(key_length):
        # Finds position of the current letter and changes letter to ? in key to account for duplicates
        position = key1.index(sorted_key[i])
        key1[position] = "?"
        # Iterates through each block in blocks and appends the char at position to the ciphertext
        for block in blocks:
            if(len(block) > position):
                ciphertext += block[position]

    # Reinitialize key for the next transposition
    key_length = len(key2)
    # Chunks ciphertext into blocks again for the double transposition
    blocks = [ciphertext[i:i+key_length] for i in range(0, len(ciphertext), key_length)]

    # Reset ciphertext for final result
    ciphertext = ""

    # Sorts key in order to compare position placement and converts original key into a list
    sorted_key = sorted(key2)
    key2 = list(key2)
    for i in range(key_length):
        # Finds position of the current letter and changes letter to ? in key to account for duplicates
        position = key2.index(sorted_key[i])
        key2[position] = "?"
        # Iterates through each block in blocks and appends the char at position to the ciphertext
        for block in blocks:
            if(len(block) > position):
                ciphertext += block[position]
    
    return ciphertext

def double_transposition_decrypt(ciphertext, key1, key2):
    # Converts ciphertext and keys to lowercase letters only
    ciphertext = re.sub("[^a-z]", "", ciphertext.lower())
    key1 = re.sub("[^a-z]", "", key1.lower())
    key2 = re.sub("[^a-z]", "", key2.lower())

    # Initializes plaintext and keylength for the alg
    # Initializes row_size for matrix and how many overflow rows there are
    plaintext = ""
    key_length = len(key2)
    row_size = (len(ciphertext)//key_length)+1
    overflow_rows = len(ciphertext)%key_length

    # Creates a matrix to decrypt the ciphertext
    matrix = [['' for j in range(key_length)] for i in range(row_size)]

    # Sorts key in order to compare position placement and converts original key into a list
    sorted_key = sorted(key2)
    key2 = list(key2)
    for i in range(key_length):
        # Finds position of the current letter and changes letter to ? in key to account for duplicates
        position = key2.index(sorted_key[i])
        key2[position] = "?"
        # Puts either row_size or row_size - 1 number of ciphertext chars into the matrix
        for j in range(row_size if overflow_rows > position else row_size - 1):
            matrix[j][position] = ciphertext[j]
        # Removes the first j characters from the ciphertext
        ciphertext = ciphertext[j+1:]
    # Appends all chars in matrix to plaintext
    for row in matrix:
        plaintext += "".join(row)

    # Initializes keylength for second pass
    # Initializes row_size for matrix and how many overflow rows there are
    key_length = len(key1)
    row_size = (len(plaintext)//key_length)+1
    overflow_rows = len(plaintext)%key_length

    # Creates a matrix to decrypt the ciphertext
    matrix = [['' for j in range(key_length)] for i in range(row_size)]

    # Sorts key in order to compare position placement and converts original key into a list
    sorted_key = sorted(key1)
    key1 = list(key1)
    for i in range(key_length):
        # Finds position of the current letter and changes letter to ? in key to account for duplicates
        position = key1.index(sorted_key[i])
        key1[position] = "?"
        # Puts either row_size or row_size - 1 number of plaintext chars into the matrix
        for j in range(row_size if overflow_rows > position else row_size - 1):
            matrix[j][position] = plaintext[j]
        # Removes the first j characters from the ciphertext
        plaintext = plaintext[j+1:]
    
    # Sets plaintext back to empty string to append final result to it
    plaintext = ""
    for row in matrix:
        plaintext += "".join(row)
    
    return plaintext
'''Double Transposition'''

'''Distupted Transpositions'''
'''Distupted Transpositions'''

'''Fractionation'''
'''Fractionation'''

'''The Straddling Checkerboard'''
'''The Straddling Checkerboard'''

'''Extending The Straddling Checkerboard'''
'''Extending The Straddling Checkerboard'''

'''More Fractionation'''
'''More Fractionation'''

'''Digraph Substitution'''
'''Digraph Substitution'''

'''Improving Keywords'''
'''Improving Keywords'''

'''Generating random digits'''
'''Generating random digits'''

'''Super-encryption'''
'''Super-encryption'''

'''Knock-Knock'''
'''Knock-Knock'''