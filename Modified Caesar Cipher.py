# Kanvi Panchal -> TYCS - 542
# Substitution Cipher Techniques - Modified Caesar Cipher
def modified_caesar_cipher():
    word = input("Enter the plain text: ")
    k = int(input("Enter the key offset: "))
    c = ' '
    for i in word:
        if (i==" "):
            c += " "
        else:
            c += (chr(ord(i)+k))
    return c
def modifies_ceacer_cipher_decrpyt():
    word = input("Enter the cipher text: ")
    k = int(input("Enter the key offset: "))
    c = ' '
    for i in word:
        if (i==" "):
            c += " "
        else:
            c += (chr(ord(i)-k))
    return c
print(modified_caesar_cipher())
print(modifies_ceacer_cipher_decrpyt())



