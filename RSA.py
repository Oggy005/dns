# Kanvi Panchal -> TYCS - 542
# RSA(Rivest–Shamir–Adleman) - Public-key Cryptosystems
import math
p = int(input("enter a prime first number: "))
q = int(input("enter a prime second number: "))
if (p != q):
    Plaintext = int(input("Enter plaintext no. "))
    n = p*q
    atotion = (p-1) * (q-1)
    temp = math.gcd(p, atotion)
    if (temp ==1 ):
        e = p
        i = 1
        d = pow(e, -1, atotion)
        print("Public Key = {", e, ",",n,"}.")
        print("Private Key = {", d, ",",n,"}.")
        if (Plaintext < n):
            C = (Plaintext ** e) % n
            P = (C**d) % n
            print("Cipher Text in no. : ",C)
            print("Plaintext using decyption key: ", P)
        else:
            print("Plain text cannot be greater then n.")
else:
    print("prime numbers cannot be same.")


    
    
