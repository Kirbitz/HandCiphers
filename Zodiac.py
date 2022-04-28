# Using z340 for the implementation
# 340 characters (without spaces)

# perhaps use double letters to represent letter combinations
# ex.  'ty' == 'hz'  while 'ts' == 'eb'
# maybe use other symbols

# manually assign all characters, use a rand function?
# if rand was used what would the process of decryption be?

# Using 1,2 decimation with 3 sections of the length(height) 9, 9 , 2

def Z340(text):
  # char assigns to be shifted by value of other paired letter.
  # for example, for 'at'   'a' would be shifted in a direction w/ distance of 't' and vice versa
  alphabet = ['/', '.', '-', '&', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
  'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  i = 0
  l = 0
  k = 0
  firstblock = [['' for l in range(17)] for k in range(9)]
  secondblock = [['' for l in range(17)] for k in range(9)]
  lastblock = [['' for l in range(17)] for k in range(2)]
  for i in range(0, len(text), 2):
    temp1 = text[i]
    temp2 = text[i+1]
    m = alphabet.index(temp1)
    n = alphabet.index(temp2)
    mod = (m - n - 5 )% 30
    temp3 = alphabet[(m - mod) % 30]
    temp4 = alphabet[(n - mod) % 30]
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

    #first 4 should be &n..
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
  print(encrypt)
  #print (firstblock, secondblock, lastblock)
  #write if statement that wraps around 2D array to avoid out of bounds error
    
   
  
  #write loop to output all arrays from left to right and up to down