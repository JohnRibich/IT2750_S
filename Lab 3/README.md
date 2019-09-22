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
  
  
