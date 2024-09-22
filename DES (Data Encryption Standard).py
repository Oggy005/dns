# Kanvi Panchal -> TYCS - 542
# DES (Data Encryption Standard)

from Cryptodome.Cipher import DES
from Cryptodome import Random

# Generate a random IV
iv = Random.get_random_bytes(8)

# Encode the key and IV as byte strings
key = b'01234567'
iv = iv

desl = DES.new(key, DES.MODE_CFB, iv)
des2 = DES.new(key, DES.MODE_CFB, iv)

text = 'KEYBOARD'
cipher_text = desl.encrypt(text.encode('utf-8'))

print("Encrypted message:", cipher_text)

# Decrypt and decode the result
decrypted_text = des2.decrypt(cipher_text).decode('utf-8')
print("Decrypted message:", decrypted_text)

