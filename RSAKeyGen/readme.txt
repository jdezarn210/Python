Implements a simple RSA keygen generator. 
“keygen” will take a key size as an input and generate a (public, private) key pair. 

Steps Taken:
1. Prime Number Generation
The first step in the RSA key generation process was to generate two large prime numbers. the key size chosen for this implementation was 1024 bits, so both were chosen to be around 512 bits each. To generate these prime numbers, the Miller-Rabin primality test was used to ensure that the selected numbers were prime. Python's sympy library was utilized to facilitate the generation of random prime numbers.
2. Computen=p×q
After generating the prime numbers, the next step was to compute the product. This value is part of both the public and private keys.
3. Compute Euler's Totient Function φ(n)
The totient function was then calculated. This function is crucial for determining the number of integers less than that are coprime with
4. Choose Public Exponent e
The public exponent was chosen as 65537, which is a commonly used value due to its efficiency and security properties.
5. Compute the Private Exponent d
The private exponent was calculated as the modular inverse of with respect to φ(n). The
mod_inverse function from the sympy library was used to compute this value. Output the Public and Private Keys
Finally, the public key and private key were outputted. The public key consists of the pair (n,e) , while the private key consists of the pair (n,d) .
