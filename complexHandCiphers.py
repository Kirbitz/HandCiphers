import re
from random import choice

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
def fraction_encryption(plaintext):
    # First makes ciphertext into all lowercase letters
    plaintext = re.sub("[^a-z]", "", plaintext.lower())

    # Dictionary for all letter combinations
    frac_dict = {'a': '11', 'b': '12', 'c': '13', 'd': '14', 'e': '15',
                 'f': '21', 'g': '22', 'h': '23', 'i': '24', 'k': '25',
                 'l': '31', 'm': '32', 'n': '33', 'o': '34', 'p': '35',
                 'q': '41', 'r': '42', 's': '43', 't': '44', 'u': '45',
                 'v': '51', 'w': '52', 'x': '53', 'y': '54', 'z': '55'}

    ciphertext = ""
    # Loops through plaintext and appends dictionary at letter as long as letter does not equal j otherwise if is dictionary at char i
    for letter in plaintext:
        ciphertext += frac_dict['i'] if letter == 'j' else frac_dict[letter]
    
    return ciphertext

def fraction_decryption(ciphertext):
    # First makes ciphertext into all numbers
    ciphertext = re.sub("[^0-9]", "", ciphertext)

    # Dictionary for all letter combinations
    frac_dict = {'1': {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e'},
                 '2': {'1': 'f', '2': 'g', '3': 'h', '4': 'i', '5': 'j'},
                 '3': {'1': 'l', '2': 'm', '3': 'n', '4': 'o', '5': 'p'},
                 '4': {'1': 'q', '2': 'r', '3': 's', '4': 't', '5': 'u'},
                 '5': {'1': 'v', '2': 'w', '3': 'x', '4': 'y', '5': 'z'},}

    plaintext = ""
    # Loops through ciphertext in increments of 2 and appends dictionary at ciphertext[i] and ciphertext[i+1] to plaintext
    for i in range(0, len(ciphertext), 2):
        plaintext += frac_dict[ciphertext[i]][ciphertext[i+1]]
    return plaintext

'''Fractionation'''

'''The Straddling Checkerboard'''
def straddling_encryption(plaintext):
    # First makes plaintext into all lowercase letters, numbers, and period
    plaintext = re.sub("[^a-z0-9.]", "", plaintext.lower())

    # Dictionary for all letter combinations, numbers, and period
    strad_dict = {'a': '0', 't': '1', 'o': '3', 'n': '4', 'e': '5', 's': '7', 'i': '8', 'r': '9',
                 'b': '20', 'c': '21', 'd': '22', 'f': '23', 'g': '24', 'h': '25', 'j': '26', 'k': '27', 'l': '28', 'm': '29',
                 'p': '60', 'q': '61', 'u': '62', 'v': '63', 'w': '64', 'x': '65', 'y': '66', 'z': '67', '.': '68',
                 '0': '690', '1': '691', '2': '692', '3': '693', '4': '694', '5': '695', '6': '696', '7': '697', '8': '698', '9': '699'}

    # Encrypts each letter in plaintext to appropriate number combination and appends it to ciphertext
    ciphertext = ""
    for letter in plaintext:
        ciphertext += strad_dict[letter]
    
    return ciphertext

def straddling_decryption(ciphertext):
    # First makes ciphertext into all numbers
    ciphertext = re.sub("[^0-9]", "", ciphertext)

    # Dictionary for all letter combinations, numbers, and period
    strad_dict = {'0': 'a', '1': 't', '3': 'o', '4': 'n', '5': 'e', '7': 's', '8': 'i', '9': 'r',
                  '2': {'0': 'b', '1': 'c', '2': 'd', '3': 'f', '4': 'g', '5': 'h', '6': 'j', '7': 'k', '8': 'l', '9': 'm'},
                  '6': {'0': 'p', '1': 'q', '2': 'u', '3': 'v', '4': 'w', '5': 'x', '6': 'y', '7': 'z', '8': '.'}}
    
    plaintext = ""
    i = 0
    # Loops through the ciphertext
    while i < len(ciphertext):
        # Checks if position is 2 and then add dictionary at 2 and ciphertext[i] to the plaintext
        if ciphertext[i] == '2':
            plaintext += strad_dict['2'][ciphertext[i+1]]
            i += 1
        # Checks if position is 6 and then add dictionary at 6 and ciphertext[i] to the plaintext
        elif ciphertext[i] == '6':
            # Checks if position is 9 and then add dictionary at 6, 9 and ciphertext[i] to the plaintext
            if ciphertext[i+1] == '9':
                plaintext += ciphertext[i+2]
                i += 1
            else:
                plaintext += strad_dict['6'][ciphertext[i+1]]
            i += 1
        # Add dictionary at ciphertext[i] to plaintext
        else:
            plaintext += strad_dict[ciphertext[i]]
        i+=1
    
    return plaintext

'''The Straddling Checkerboard'''

'''Extending The Straddling Checkerboard'''
def straddling_exten_encryption(plaintext):
    # First makes plaintext into all lowercase letters, numbers, and a few special chars
    plaintext = re.sub("[^a-z0-9.,:?/()\" ]", "", plaintext.lower())

    # Dictionary for all letter combinations, numbers, and special chars
    strad_dict = {'a': '1', 'e': '2', 'i': '3', 'n': '4', 'o': '5', 'r': '6',
                 'b': '70', 'c': '71', 'd': '72', 'f': '73', 'g': '74', 'h': '75', 'j': '76', 'k': '77', 'l': '78', 'm': '79',
                 'p': '80', 'q': '81', 's': '82', 't': '83', 'u': '84', 'v': '85', 'w': '86', 'x': '87', 'y': '88', 'z': '89',
                 ' ': '90', '.': '91', ',': '92', ':': '93', '?': '94', '/': '95', '(': '96', ')': '97', '"': '98',
                 '0': '990', '1': '991', '2': '992', '3': '993', '4': '994', '5': '995', '6': '996', '7': '997', '8': '998', '9': '999'}

    # Encrypts each letter in plaintext to appropriate number combination and appends it to ciphertext
    ciphertext = ""
    for letter in plaintext:
        ciphertext += strad_dict[letter]
    
    return ciphertext

def straddling_exten_decryption(ciphertext):
    # First makes ciphertext into all numbers
    ciphertext = re.sub("[^0-9]", "", ciphertext)
    # Dictionary for all letter combinations, numbers, and special chars
    strad_dict = {'1': 'a', '2': 'e', '3': 'i', '4': 'n', '5': 'o', '6': 'r',
                  '7': {'0': 'b', '1': 'c', '2': 'd', '3': 'f', '4': 'g', '5': 'h', '6': 'j', '7': 'k', '8': 'l', '9': 'm'},
                  '8': {'0': 'p', '1': 'q', '2': 's', '3': 't', '4': 'u', '5': 'v', '6': 'w', '7': 'x', '8': 'y', '9': 'z'},
                  '9': {'0': ' ', '1': '.', '2': ',', '3': ':', '4': '?', '5': '/', '6': '(', '7': ')', '8': '"'}}
    
    plaintext = ""
    i = 0
    # Loops through the ciphertext
    while i < len(ciphertext):
        # Checks if position is 7 and then add dictionary at 7 and ciphertext[i] to the plaintext
        if ciphertext[i] == '7':
            plaintext += strad_dict['7'][ciphertext[i+1]]
            i += 1
        # Checks if position is 8 and then add dictionary at 8 and ciphertext[i] to the plaintext
        elif ciphertext[i] == '8':
            plaintext += strad_dict['8'][ciphertext[i+1]]
            i += 1
        # Checks if position is 9 and then add dictionary at 9 and ciphertext[i] to the plaintext
        elif ciphertext[i] == '9':
            # Checks if position is 9 and then add dictionary at 9, 9 and ciphertext[i] to the plaintext
            if ciphertext[i+1] == '9':
                plaintext += ciphertext[i+2]
                i += 1
            else:
                plaintext += strad_dict['9'][ciphertext[i+1]]
            i += 1
        # Add dictionary at ciphertext[i] to plaintext
        else:
            plaintext += strad_dict[ciphertext[i]]
        i+=1
    
    return plaintext
'''Extending The Straddling Checkerboard'''

'''More Fractionation'''
def fraction_more_encryption(plaintext):
    # First makes plaintext into all lowercase
    plaintext = re.sub("[^a-z.]", "", plaintext.lower())

    # Dictionary for all letter combinations and period
    frac_dict = {'a': '111', 'b': '112', 'c': '113', 'd': '211', 'e': '212', 'f': '213', 'g': '311', 'h': '312', 'i': '313',
                 'j': '121', 'k': '122', 'l': '123', 'm': '221', 'n': '222', 'o': '223', 'p': '321', 'q': '322', 'r': '323',
                 's': '131', 't': '132', 'u': '133', 'v': '231', 'w': '232', 'x': '233', 'y': '331', 'z': '332', '.': '333'}
    letter_mix = {'1': ['a', 'd', 'g', 'j', 'm', 'p', 's', 'v', 'y'],
                  '2': ['b', 'e', 'h', 'k', 'n', 'q', 't', 'w', 'z'],
                  '3': ['c', 'f', 'i', 'l', 'o', 'r', 'u', 'x']}
    
    ciphertext = ""
    # Encrypts each letter based on 3 numbers and random letters from letter mix
    for letter in plaintext:
        for number in frac_dict[letter]:
            ciphertext += choice(letter_mix[number])
    
    return ciphertext


def fraction_more_decryption(ciphertext):
    # First makes ciphertext into all lowercase
    ciphertext = re.sub("[^a-z]", "", ciphertext.lower())
    # Dictionary for all letter combinations and period
    frac_dict = {'1': {'1': {'1': 'a', '2': 'b', '3': 'c'},
                       '2': {'1': 'j', '2': 'k', '3': 'l'},
                       '3': {'1': 's', '2': 't', '3': 'u'}},
                 '2': {'1': {'1': 'd', '2': 'e', '3': 'f'},
                       '2': {'1': 'm', '2': 'n', '3': 'o'},
                       '3': {'1': 'v', '2': 'w', '3': 'x'}},
                 '3': {'1': {'1': 'g', '2': 'h', '3': 'i'},
                       '2': {'1': 'p', '2': 'q', '3': 'r'},
                       '3': {'1': 'y', '2': 'z', '3': '.'}}}
    # dictionary of letters that are mapped to the same number
    letter_mix = dict.fromkeys(['a', 'd', 'g', 'j', 'm', 'p', 's', 'v', 'y'], '1')
    letter_mix.update(dict.fromkeys(['b', 'e', 'h', 'k', 'n', 'q', 't', 'w', 'z'], '2'))
    letter_mix.update(dict.fromkeys(['c', 'f', 'i', 'l', 'o', 'r', 'u', 'x'], '3'))

    # First decrypts letter based on position it is in
    intermediate = ""
    for letter in ciphertext:
        intermediate += letter_mix[letter]
    plaintext = ""
    # Then finds location in dictionary and adds it to the plaintext
    for number in range(0, len(intermediate), 3):
        pos1, pos2, pos3 = intermediate[number], intermediate[number+1], intermediate[number+2]
        plaintext += frac_dict[pos1][pos2][pos3]

    return plaintext
'''More Fractionation'''

'''Digraph Substitution'''
def fix_plaintext(plaintext):
    # First makes plaintext into all lowercase letters then replaces j with iz
    plaintext = re.sub("[^a-z]", "", plaintext.lower())
    plaintext = plaintext.replace('j', 'i')
    # initialize temp for duplicates the i = 0 for loop
    temp = ''
    i = 0
    # Loop through plaintext and adds an x between double letters
    while i < len(plaintext):
        if plaintext[i] == temp:
            plaintext = plaintext[:i] + 'x' + plaintext[i:]
        temp = plaintext[i]
        i+=1
    # Adds an x to the string if it has an odd length
    if len(plaintext) % 2 == 1:
        plaintext += 'x'
    return plaintext

def make_matrix(key):
    # Creates a 5x5 matrix
    matrix = [['' for i in range(5)] for j in range(5)]
    # Loops through key and adds letters from key into the first positions of the matrix
    for i in range(len(key)):
        matrix[(i//5)%5][i%5] = key[i]
    j = len(key)
    # Loops through the 26 letters in the alphabet and adds all letters that were not in the key to the matrix
    for i in range(26):
        letter = chr(ord('a') + i)
        if not any(letter in subl for subl in matrix) and letter != 'j':
            matrix[(j//5)%5][j%5] = letter
            j+=1
    return matrix

def index_2d(matrix, val):
    # Loops through each row in matrix and creates i index
    for i, j in enumerate(matrix):
        # Checks if the value passed in is in row j
        if val in j:
            # returns index of val in matrix
            return i, j.index(val)

def playfair_encryption(plaintext, key):
    # Fixes the plaintext so it will work properly with playfair
    plaintext = fix_plaintext(plaintext)

    # Fixes the key so it will work properly with playfair
    key = re.sub("[^a-z]", "", key.lower())
    key = key.replace('j', 'i')
    key = "".join(dict.fromkeys(key))
    
    # Creates the playfair matrix
    matrix = make_matrix(key)
    
    ciphertext = ""
    # loops through plaintext while taking characters 2 at a time
    for i in range(0, len(plaintext), 2):
        # Gets matrix positions of letter1 and letter2
        letter1_index, letter2_index = index_2d(matrix, plaintext[i]), index_2d(matrix, plaintext[i+1])
        # Checks if letters are in the same row
        if letter1_index[0] == letter2_index[0]:
            ciphertext += matrix[letter1_index[0]][(letter1_index[1]+1) % 5]
            ciphertext += matrix[letter2_index[0]][(letter2_index[1]+1) % 5]
        # Checks if letters are in the same column
        elif letter1_index[1] == letter2_index[1]:
            ciphertext += matrix[(letter1_index[0]+1)%5][letter1_index[1]]
            ciphertext += matrix[(letter2_index[0]+1)%5][letter2_index[1]]
        # Runs if letters are in different rows and columns
        else:
            ciphertext += matrix[letter1_index[0]][letter2_index[1]]
            ciphertext += matrix[letter2_index[0]][letter1_index[1]]

    return ciphertext

def playfair_decryption(ciphertext, key):
    # Fixes the ciphertext so it will work properly with playfair
    ciphertext = re.sub("[^a-z]", "", ciphertext.lower())

    # Fixes the key so it will work properly with playfair
    key = re.sub("[^a-z]", "", key.lower())
    key = key.replace('j', 'i')
    key = "".join(dict.fromkeys(key))

    # Creates the playfair matrix
    matrix = make_matrix(key)

    plaintext = ""
    # loops through ciphertext while taking characters 2 at a time
    for i in range(0, len(ciphertext), 2):
        # Gets matrix positions of letter1 and letter2
        letter1_index, letter2_index = index_2d(matrix, ciphertext[i]), index_2d(matrix, ciphertext[i+1])
        # Checks if letters are in the same row
        if letter1_index[0] == letter2_index[0]:
            plaintext += matrix[letter1_index[0]][(letter1_index[1]-1) % 5]
            plaintext += matrix[letter2_index[0]][(letter2_index[1]-1) % 5]
        # Checks if letters are in the same column
        elif letter1_index[1] == letter2_index[1]:
            plaintext += matrix[(letter1_index[0]-1)%5][letter1_index[1]]
            plaintext += matrix[(letter2_index[0]-1)%5][letter2_index[1]]
        # Runs if letters are in different rows and columns
        else:
            plaintext += matrix[letter1_index[0]][letter2_index[1]]
            plaintext += matrix[letter2_index[0]][letter1_index[1]]
    plaintext = plaintext.replace('x', '')

    return plaintext

'''Digraph Substitution'''

'''Improving Keywords'''
'''Improving Keywords'''

'''Generating random digits'''
'''Generating random digits'''

'''Super-encryption'''
'''Super-encryption'''

'''Knock-Knock'''
'''Knock-Knock'''