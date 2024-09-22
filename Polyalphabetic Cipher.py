# Kanvi Panchal -> TYCS - 542
# Substitution Cipher Techniques - Polyalphabetic Cipher
def polyalphabetic_cipher():
    word = input("Enter the plain text: ")
    k = int(input("Enter the key offset: "))
    c = ' '
    for i in word:
        if (i==" "):
            temp = " "
            c+=temp
        else:
                temp = (chr(ord(i)+k))
                c+=temp
                for j in c:
                    if j == temp:
                        temp = (chr(ord(i)+k+1))   
    return c
print(polyalphabetic_cipher())


