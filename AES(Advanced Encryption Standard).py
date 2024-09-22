# Kanvi Panchal -> TYCS - 542
# AES(Advanced Encryption Standard)
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes
key = b'mysecretpassword'  # Example key (16 bytes)
# Generate a random initialization vector (IV)
iv = get_random_bytes(AES.block_size)
# Create AES cipher object
cipher = AES.new(key, AES.MODE_CBC, iv)
# Encrypt a message
message = "Hello, AES encryption!".encode()
cipher_text = cipher.encrypt(pad(message, AES.block_size))
print("Encrypted:", cipher_text)
# Decrypt the message
decrypt_cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted_text = unpad(decrypt_cipher.decrypt(cipher_text), AES.block_size)
print("Decrypted:", decrypted_text.decode())
