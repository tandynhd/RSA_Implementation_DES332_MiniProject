# https://www.pycryptodome.org/en/latest/src/introduction.html

from pydoc import plain
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# encryption
def sha1DigestE(plaintext):
    plaintext = bytes(plaintext, 'utf-8')
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, digest = cipher.encrypt_and_digest(plaintext)

    file_out = open("encrypted.bin", "wb")
    [ file_out.write(x) for x in (cipher.nonce, digest, ciphertext) ]
    file_out.close()

    return(key,plaintext)

# decryption
def sha1DigestD(key):
    file_in = open("encrypted.bin", "rb")
    nonce, digest, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]
    # let's assume that the key is somehow available again
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    decrypted = cipher.decrypt_and_verify(ciphertext, digest)
    print(decrypted)
    return(decrypted)

# plaintext="hello world"
# key,plaintext = sha1DigestE(plaintext)
# print(key,plaintext)
