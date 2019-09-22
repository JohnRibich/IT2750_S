In lesson three, we covered types ciphers, encoding, decoding, keys and method types. 

Three basic string methods:
Upper - Returns a string in all uppercase
Lower - Returns a string in all lowercase
Index - Returns the index of the first occurence of an item in a string or an error if not found

In this lesson the three types of algorithms we learned about were, encoding, decoding and ciphers. Encoding is the process in which messages become unreadable by taking the cipher and using it to encrypt the file. The Cipher or Ciphertext are the unreadable form of the message that are encoded and can be decoded. Decoding is the last algorithm that takes a key to unscramble the unreadable file to make it readable again. 

Identify the type of encryption
def encrypt(plainText ,key):  
  alphabet = "abcdefghijklmnopqrstuvwxyz"  
  plainText = plainText.lower ()  
  cipherText = ""  

  for ch in plainText:  
      idx = alphabet.find(ch)  
      cipherText = cipherText + key[idx]  
  return cipherText 
  
  This is a Substitution Cipher
  
  Identify the type of encryption
  def scramble2Encrypt(plainText):  
  evenChars = ""  
  oddChars = ""  
  charCount = 0  

  for ch in plainText:  
      if charCount % 2 == 0:  
          evenChars = evenChars + ch  
      else:  
          oddChars = oddChars + ch  
    charCount = charCount + 1  
  cipherText = oddChars + evenChars  
  return cipherText  
  
  This is a Transposition Cipher
  
  myCrypto.py
  
  def scramble2Encrypt(plainText):

    evenChars = ""

    oddChars = ""

    charCount = 0

    for ch in plainText:

        if charCount % 2 == 0:

            evenChars = evenChars + ch

        else:

            oddChars = oddChars + ch

        charCount = charCount + 1

    cipherText = oddChars + evenChars

    return cipherText

def scramble2Decrypt(cipherText):
    halfLength = len(cipherText) // 2

    oddChars = cipherText[:halfLength]

    evenChars = cipherText[halfLength:]

    plainText = ""

    for i in range(halfLength):
        plainText = plainText + evenChars[i]

        plainText = plainText + oddChars[i]

    if len(oddChars) < len(evenChars):
        plainText = plainText + evenChars[-1]

    return plainText

print(scramble2Encrypt('Hello'))
print(scramble2Encrypt('My name is'))
print(scramble2Encrypt('John'))

print("\n")

print(scramble2Decrypt(scramble2Encrypt('Hello')))
print(scramble2Decrypt(scramble2Encrypt('My name is')))
print(scramble2Decrypt(scramble2Encrypt('John')))
  
  
