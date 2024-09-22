# Kanvi Panchal -> TYCS - 542
# Diffie-Hellman Key Agreement algorithm 
p = 23  # Prime number
g = 5   # Primitive root modulo p
a = 2 # Alice's private key
b = 8  # Bob's private key
A = pow(g, a, p)  # Alice's public key
B = pow(g, b, p)  # Bob's public key
shared_secret_alice = pow(B, a, p)  
shared_secret_bob = pow(A, b, p)    

print(f"Alice's private key: {a}")
print(f"Bob's private key: {b}")
print(f"Alice's public key: {A}")
print(f"Bob's public key: {B}")
print(f"Shared secret (Alice's computation): {shared_secret_alice}")
print(f"Shared secret (Bob's computation): {shared_secret_bob}")

assert shared_secret_alice == shared_secret_bob, "Shared secrets do not match!"
print(f"The shared secret is: {shared_secret_alice}")


