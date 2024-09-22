# Kanvi Panchal -> TYCS - 542
# Transposition Cipher Techniques - Rail Fence Cipher
def main():
    layers = int(input("Enter the number of  layers: "))
    plain_text = input("enter the plain text: ")
    cipher_text = encrypt(layers, plain_text)
    print("Encrypted text: " + cipher_text)
def encrypt(layers, plain_text):
    plain_text = plain_text.replace(" ", "")
    plain_text = plain_text.upper()
    rail = [""] * layers
    layer = 0
    for char in plain_text:
        rail[layer] += char
        if layer >= layers - 1:
            layer = 0
        else:
            layer += 1
    cipher = " ".join(rail)
    return cipher
if __name__ == '__main__':
    main()


    
