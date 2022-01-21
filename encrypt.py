#encrypting using transposition cipher
#from array import *

def encrypt(plainText, key):
  
  rows = round(len(plainText)/key)
  box = [[0 for c in range(key)] for r in range(rows)]
  #print("length:", len(plainText))

  #filling in the matrix 
  i = 0
  for r in range(rows):
    for c in range(key):
      #print("i", i)
      if i < len(plainText):
        box[r][c] = plainText[i:i+1]
      else: 
        box[r][c] = ""
      i = i+1

  #print(box);

  cipherText = ""

  for c in range(key):
    for r in range(rows):
      cipherText = cipherText + box[r][c]

  print(cipherText)

def decrypt(cipherText, key):
  rows = round(len(cipherText)/key)
  box = [[0 for c in range(key)] for r in range(rows)]

  i =0
  for c in range(key):
    for r in range(rows):
      if i < len(cipherText):
        box[r][c] = cipherText[i:i+1]
      else: 
        box[r][c] = ""
      i = i+1
  #print(box)

  plainText = ""
  for r in range(rows):
    for c in range(key):
      plainText = plainText + box[r][c]
  
  print(plainText)


print("Welcome to transposition cipher")
answer = input("Encrypt or Decrypt? (E/D) ")
isFile = input("Do you wanna have input from a file? (Y/N): ")
if(isFile == "N"):
  text = input("Enter text to cipher or decipher: ")
  key = int(input("enter key: "))
elif (isFile == "Y"):
  name = input("Please upload the file and enter name here: ")
  f = open(name, "r")
  text = f.read();
  f.close();
  key = int(input("enter key: "))
else:
  print("Error")

if(answer=="E"):
  encrypt(text, key)
elif(answer == "D"):
  decrypt(text, key)
else:
  print("Sorry, your answer could not be understood.")