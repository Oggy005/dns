# Kanvi Panchal -> TYCS - 542
# Substitution Cipher Techniques - Monoalphabetic Cipher
alpha = {
    "a": "n",
    "b": "b",
    "c": "v",
    "d": "x",
    "e": "z",
    "f": "l",
    "i": "k",
    "j": "j",
    "k": "h",
    "l": "g",
    "m": "f",
    "n": "d",
    "o": "s",
    "p": "a",
    "q": "p",
    "r": "o",
    "s": "i",
    "t": "u",
    "u": "y",
    "v": "t",
    "w": "r",
    "x": "e",
    "y": "w",
    "z": "q",
    " ": " "
    }
message = input("Enter the message: ")
result =" "
for letter in message.lower():
    if letter in alpha:
        result += alpha[letter]
print("Cipher Text: " + result)
