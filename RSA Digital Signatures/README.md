# RSA DIGITAL SIGNATURES
Running the script sign.py asks the user for the name of the file that is going to be signed, and outputs three quantities, N (the semiprime used in RSA), e (the public key used in RSA) and the digital signature of the file (in hex).
Running verifier.py asks the user for the name fo the file, the semiprime N, the public exponent e and the digital signature (in hex) and verifies whether the signature is correct or not and returns 'accept' or 'reject' correspondingly.
