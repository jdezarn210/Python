from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import utils

# Generate public-private RSA key pair (RSA-4096)
private_key = rsa.generate_private_key(public_exponent=65537, key_size=4096)
public_key = private_key.public_key()

# Save public key to key.pub
with open("key.pub", "wb") as key_pub_file:
    key_pub_file.write(
        public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    )

# Generate an unencrypted text file named 'message.txt'
# NOTE: Insert your string "<First Last> <ID> 4130Lab4" here
message_string = "<First Last> <ID> 4130Lab4"
with open("message.txt", "w") as message_file:
    message_file.write(message_string)

# Read message.txt as bytes
with open("message.txt", "rb") as message_file:
    message = message_file.read()

# Sign the message with the private key and save to signature.sig
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

with open("signature.sig", "wb") as signature_file:
    signature_file.write(signature)

# Encrypt the message with the class public key (from 4130-PublicKey.pem)
# Load the provided class public key
with open("4130-PublicKey.pem", "rb") as class_pub_key_file:
    class_public_key = serialization.load_pem_public_key(class_pub_key_file.read())

ciphertext = class_public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Save encrypted message to message.encr
with open("message.encr", "wb") as encrypted_file:
    encrypted_file.write(ciphertext)

print("All files generated successfully: key.pub, message.txt, signature.sig, message.encr")
