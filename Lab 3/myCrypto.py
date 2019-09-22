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
