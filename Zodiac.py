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
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
  'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] #also might add /, ., -, @, &, *

  #i = 0
  #j = 0
  #firstblock = [['' for i in range(17)] for j in range(9)]
  #firstblock[i+2][j+1] = 'j'
  #print(firstblock[2][1])