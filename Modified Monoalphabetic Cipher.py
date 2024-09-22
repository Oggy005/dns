# Kanvi Panchal -> TYCS - 542
# Substitution Cipher Techniques - Modified Monoalphabetic Cipher
def modified_monoalphabetic_cipher():
    word = input("Enter the plain text: ")
    k = int(input("Enter the key offset: "))
    c = ' '
    for i in word:
        if (i==" "):
            c += " "
        else:
            c += (chr(ord(i)+k))
    return c
def modified_monoalphabetic_cipher_decrpyt():
    word = input("Enter the cipher text: ")
    k = int(input("Enter the key offset: "))
    c = ' '
    for i in word:
        if (i==" "):
            c += " "
        else:
            c += (chr(ord(i)-k))
    return c
print(modified_monoalphabetic_cipher())
print(modified_monoalphabetic_cipher_decrpyt())



