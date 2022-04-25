# https://www.pycryptodome.org/en/latest/src/introduction.html

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import hashlib

#Check license
def check_license(Oneway_hash,digital_signature):
    if Oneway_hash==digital_signature:
        print("Digital signature true")
    else:
        print("Digital signature not true")
        

#hash_object = hashlib.sha1(b'HelWorld')
#pbHash = hash_object.hexdigest()
#print(pbHash)
print("-------------------------------------------------------")
message = b'secret data'
print("message = ",message)
print("-------------------------------------------------------")
h = hashlib.new("sha1",message)
sha1text = h.hexdigest()
sha1text = str(sha1text)
print("sha1 digest message = ",sha1text)
print("-------------------------------------------------------")

#We need to provide AES for generate symmetric key to protect sha1text as a digital signature

# encryption
plaintext=sha1text.encode('utf_8')

#print(plaintext)
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, digest = cipher.encrypt_and_digest(plaintext)
print("AES key= ",key)
print("AES cipher= ",cipher)
print("AES encryption result = ",ciphertext)
print("AES digest = ",digest)
print("-------------------------------------------------------")

file_out = open("encrypted.bin", "wb")
[ file_out.write(x) for x in (cipher.nonce, digest, ciphertext) ]
file_out.close()


# decryption
file_in = open("encrypted.bin", "rb")
nonce, digest, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]
# let's assume that the key is somehow available again
cipher = AES.new(key, AES.MODE_EAX, nonce)
decrypted = cipher.decrypt_and_verify(ciphertext, digest)
print("AES cipher= ",cipher)
print("AES decryption result = ",decrypted)
print("-------------------------------------------------------")
print("Check license of digital signature")
check_license(plaintext,decrypted)
