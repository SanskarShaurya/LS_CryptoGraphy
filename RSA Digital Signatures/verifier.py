import hashlib
import os

def sha256_hash(filename):
    with open(filename, 'rb') as file:
        data = file.read()
        sha256 = hashlib.sha256(data)
        return sha256.digest()

def RSA_verify(sha256_hash, N, e, signature_hex):
    signature = int(signature_hex, 16)
    decrypted_signature = pow(signature, e, N)
    original_hash = int.from_bytes(sha256_hash, byteorder='big')
    return decrypted_signature == original_hash

def main():
    filename = input("Input the name of the text file: ")
    if not os.path.isfile(filename):
        print("Invalid filename")
        return

    N = int(input("Input N (semiprime): "))
    e = int(input("Input e (public exponent): "))
    signature_hex = input("Input the signature (hex): ")

    hash_value = sha256_hash(filename)
    if RSA_verify(hash_value, N, e, signature_hex):
        print("accept")
    else:
        print("reject")

if __name__ == "__main__":
    main()
