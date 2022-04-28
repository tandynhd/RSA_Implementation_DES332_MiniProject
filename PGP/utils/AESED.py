# https://www.pycryptodome.org/en/latest/src/introduction.html

from pydoc import plain
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

# encryption
def AESE(plaintext,key):
    plaintext = bytes(plaintext, 'utf-8')
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, digest = cipher.encrypt_and_digest(plaintext)

    file_out = open("encrypted.bin", "wb")
    [ file_out.write(x) for x in (cipher.nonce, digest, ciphertext) ]
    file_out.close()
    aesE = "encrypted.bin"
    return(aesE)

    # return(key,plaintext)

# decryption
def AESD(aesE,key):
    file_in = open(aesE, "rb")
    nonce, digest, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]
    # let's assume that the key is somehow available again
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    decrypted = cipher.decrypt_and_verify(ciphertext, digest)
    # print(decrypted)
    return(decrypted)

# key = os.urandom (16)
# plaintext="hello world"+key
# aesE = AESE(plaintext,key)
# print(key,plaintext)
# print(AESD(aesE,key))