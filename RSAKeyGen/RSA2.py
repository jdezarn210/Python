from sympy import randprime, mod_inverse
import math

# Choose Two Large Prime Numbers p and q
def generate_prime(bits):
    return randprime(2**(bits - 1), 2**bits)

def keygen(key_size):
    # Generate two large prime numbers p and q
    p = generate_prime(key_size // 2)
    q = generate_prime(key_size // 2)

    # Compute n = p * q
    n = p * q

    # Compute Euler's Totient Function φ(n) = (p - 1) * (q - 1)
    phi = (p - 1) * (q - 1)

    # Choose Public Exponent e
    e = 65537

    # Compute the Private Exponent d
    d = mod_inverse(e, phi)

    # Output the Public and Private Keys
    public_key = (n, e)
    private_key = (n, d)

    print("Public Key: (n, e) =", public_key)
    print("Private Key: (n, d) =", private_key)

# Example usage
key_size = 1024
keygen(key_size)