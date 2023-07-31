import os
import hashlib
import random
import math
from sympy import nextprime
from Crypto.Util import number

def sha256_hash(filename):
    with open(filename, 'rb') as file:
        data = file.read()
        sha256 = hashlib.sha256(data)
        return sha256.digest()

def generate_random_semiprime(bits=512):
    while True:
        p = nextprime(random.getrandbits(bits))
        q = nextprime(random.getrandbits(bits))
        if p != q:
            return p*q,(p-1)*(q-1)

def RSA(sha256_hash, N, phi, e=65537):
    d = pow(e,-1,phi)
    signature = pow(int.from_bytes(sha256_hash, byteorder='big'), d, N)
    return hex(signature)

def main():
    filename = input("Input the name of the file: ")
    if not os.path.isfile(filename):
        print("Invalid filename")
        return

    N,phi = generate_random_semiprime()
    hash_value = sha256_hash(filename)
    sign_hex = RSA(hash_value,N,phi)

    print("N:", N)
    print("e:", 65537)
    print("Signature (hex):", sign_hex)

if __name__ == "__main__":
    main()
