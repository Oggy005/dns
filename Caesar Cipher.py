# Kanvi Panchal -> TYCS - 542
# Substitution Cipher Techniques - Caesar Cipher
import string
alpha = string.ascii_lowercase
no_of_shifts = 3
message = str(input("Enter you message: "))
result = " "
for letter in message.lower():
    if letter in alpha:
        alpha_index = alpha.index(letter) + no_of_shifts
        try:
            result += alpha[alpha_index]
        except IndexError:
            if alpha_index > 26:
                result += alpha[alpha_index-26]
    else:
        result += letter
print("Cipher Text: " + result)

