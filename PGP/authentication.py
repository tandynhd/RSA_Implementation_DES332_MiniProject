from encodings import utf_8
from utils.sha1 import *
from rsa_main import *
# Authentication
# Sender
#1) Creates a clear text message
def sendS(message):
    #2) The sender creates a SHA-1 message digest of the clear-text message.
    sha1E = sha1DigestE(message)
    key,plaintext = sha1E
    sha1E = str(key)
    print(sha1E)
    #3) Encrypt the SHA-1 message digest using senders public key (RSA)
    cipher = RSAE(sha1E,Sender)
    print(cipher)
    return(receiveS(cipher,sha1E,key,plaintext))

#Receiver
#4) Decrypt the RSA encryptes SHA-1 message digest using senders private key (RSA)
#5) The receiver decodes the SHA-1 message digest and matches it with the one generated by the sender
def receiveS(cipher,sha1E,key,plaintext):
    decrypted = RSAD(cipher,Sender)
    if decrypted == sha1E:
        decrypted = key
        if sha1DigestD(key) == plaintext:
            print("Digital signature true")
            return(True)
        else:
            print("Digital signature not true")

# sent = send("Hi i am tandin")
# cipher,sha1E,key,plaintext = sent
# print(receive(cipher,sha1E,key,plaintext))
# print(sent)