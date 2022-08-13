#RSA

from cryptography.hazmat.backends import default_backent
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


with open('private_key.pem', 'rb') as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )

public_key= private_key.public_key.public_key()

message= b"THE SECRET KEY IS VERY SECRET1"

ciphertext= public_key.encrypt(
    message,
    padding.OAEP(
        mgf=paddding.MGF1(algorithm=hashes.SHA1()),
        algorithm=hashes.SHA1(),
        label=None
    )
 )
print(ciphertext)

plaintext=private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA1()),
        algorithm=hashes.SHA1(),
        label=None
     )
 )
print(plaintext)

