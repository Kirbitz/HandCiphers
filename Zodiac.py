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
  textEx = "dabadb"
  alphabet = ['/', '.', '-', '&', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
  'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  i = 0
  for i in textEx:
    temp1 = textEx[i]
    temp2 = textEx[i+1]
    i+2
    # m = find location of temp1 in alphabet array
    # n = find location of temp2 in alphabet array
    temp3 = alphabet[(m + n) % 30]
    temp4 = alphabet[(m - n) % 30]

  l = 0
  k = 0
  firstblock = [['' for l in range(17)] for k in range(9)]
  #write if statement that wraps around 2D array to avoid out of bounds error
  firstblock[l+2][k+1] = temp3
  l+2
  k+1
  firstblock[l+2][k+1] = temp4
  #write loop to output all arrays from left to right and up to down