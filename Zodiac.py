import re
from random import choice
# Using z340 for the implementation
# Using 1,2 decimation with 3 sections of the length(height) 9, 9 , 2

#encryption function
def Z340(text):

  #converts all text passed in to lowercase and removes spaces
  text = re.sub("[^a-z/.\-&]", "", text.lower())

  # char assigns to be shifted by value of other paired letter plus a constant.
  alphabet = ['/', '.', '-', '&', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
  'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

  #adds random characters to text if message is less than 340 characters
  if len(text) < 340:
    for i in range(340 - len(text)):
      text += choice(alphabet)

  #creates empty blocks for charcters to be passed into in 9, 9, 2 row format
  i = 0
  l = 0
  k = 0
  firstblock = [['' for l in range(17)] for k in range(9)]
  secondblock = [['' for l in range(17)] for k in range(9)]
  lastblock = [['' for l in range(17)] for k in range(2)]

  #increments through each pair of characters in text and has the characters modify each other
  for i in range(0, len(text), 2):
    temp1 = text[i]
    temp2 = text[i+1]
    m = alphabet.index(temp1)
    n = alphabet.index(temp2)
    mod = (m - n - 5 )% 30
    temp3 = alphabet[(m - mod) % 30]
    temp4 = alphabet[(n - mod) % 30]

    #puts first character of pair into its appropriate block
    if firstblock[k][l] == '':
      firstblock[k][l] = temp3
      l = (l + 2) % 17
      k = (k + 1) % 9
    elif len(text) > 153 and secondblock[k][l] == '' and firstblock[k][l] != '':
      secondblock[k][l] = temp3
      l = (l + 2) % 17
      k = (k + 1) % 9
    elif len(text) > 306 and secondblock != '':
      lastblock[k][l] = temp3
      l = (l + 2) % 17
      k = (k + 1) % 2

    ##puts second character of pair into its appropriate block
    if firstblock[k][l] == '':
      firstblock[k][l] = temp4
      l = (l + 2) % 17
      k = (k + 1) % 9
    elif len(text) > 153 and secondblock[k][l] == '' and firstblock[k][l] != '':
      secondblock[k][l] = temp4
      l = (l + 2) % 17
      k = (k + 1) % 9
    elif len(text) > 306 and secondblock != '':
      lastblock[k][l] = temp4
      l = (l + 2) % 17
      k = (k + 1) % 2

  #collects the new order of charcters into a string to output
  encrypt = ""
  for r in range(9):
    for q in range(17):
      encrypt += firstblock[r][q]
  for t in range(9):
    for s in range(17):
      encrypt += secondblock[t][s]
  for v in range(2):
    for u in range(17):
      encrypt += lastblock[v][u]
  return(encrypt)

#decrypts the encrypted message passed in
def decrypt(message):
  alphabet = ['/', '.', '-', '&', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
  'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  i = 0
  l = 0
  k = 0
  m = 0
  n = 0
  count = 0

  #creates empty blocks for temporal storage and final character storage
  tempblock1 = [['' for m in range(17)] for n in range(9)]
  tempblock2 = [['' for m in range(17)] for n in range(9)]
  tempblock3 = [['' for m in range(17)] for n in range(2)]
  firstblock = [['' for l in range(17)] for k in range(9)]
  secondblock = [['' for l in range(17)] for k in range(9)]
  lastblock = [['' for l in range(17)] for k in range(2)]

  #puts individual characters into temporary block to be rearranged
  for i in range(0, len(message), 1):
    if tempblock1[n][m] == '':
      tempblock1[n][m] = message[i]
      if m == 16:
        m = 0
        if n == 8:
          n = 0
        else:
          n += 1
      else:
        m += 1
      if tempblock1[8][16] != '':
        m = 0
        n = 0
    elif tempblock2[n][m] == '' and tempblock1[n][m] != '':
      tempblock2[n][m] = message[i]
      if m == 16:
        m = 0
        if n == 8:
          n = 0
        else:
          n += 1
      else:
        m += 1
      if tempblock2[8][16] != '':
        m = 0
        n = 0
    elif tempblock3[n][m] == '' and tempblock2[n][m] != '':
      tempblock3[n][m] = message[i]
      if m == 16:
        m = 0
        if n == 1:
          n = 0
        else:
          n += 1
      else: 
        m += 1
      if tempblock3[1][16] != '':
        m = 0
        n = 0
  
  #characters are unscrambled from the 1,2 decimation temporary block to final character block
  while lastblock[1][16] == '':
    if firstblock[8][16] == '' and count < 153:
        firstblock[n][m] = tempblock1[k][l]
        l = (l + 2) % 17
        k = (k + 1) % 9
        if m == 16:
          m = 0
          if n == 8:
            n = 0
          else:
            n += 1
        else: 
          m += 1
        count += 1
        if count == 153:
          m = 0
          n = 0
    elif secondblock[8][16] == '' and count > 152 and count < 306:
        secondblock[n][m] = tempblock2[k][l]
        l = (l + 2) % 17
        k = (k + 1) % 9
        if m == 16:
          m = 0
          if n == 8:
            n = 0
          else:
            n += 1
        else:
          m += 1
        count += 1
        if count == 306:
          m = 0
          n = 0
    elif lastblock[1][16] == '' and count > 305:
        lastblock[n][m] = tempblock3[k][l]
        l = (l + 2) % 17
        k = (k + 1) % 2
        if m == 16:
          m = 0
          if n == 1:
            n = 0
          else:
            n += 1
        else:
          m += 1
          count += 1
  
  #puts the correctly ordered characters into a string to be decrypted
  encrypted = ""
  for r in range(9):
    for q in range(17):
      encrypted += firstblock[r][q]
  for t in range(9):
    for s in range(17):
      encrypted += secondblock[t][s]
  for v in range(2):
    for u in range(17):
      encrypted += lastblock[v][u]

  #decrypts the pair of charcters that are next to each other and then appended to a final string
  decrypted = ""
  for j in range(0, len(encrypted), 2):
    temp1 = encrypted[j]
    temp2 = encrypted[j+1]
    enc1 = alphabet.index(temp1)
    enc2 = alphabet.index(temp2)
    dec2 = alphabet[(enc1 - 5) % 30]
    dec1 = alphabet[((2 * alphabet.index(dec2) - (enc2 - 5 )) % 30)]
    decrypted += dec1
    decrypted += dec2
  print(decrypted)
  
