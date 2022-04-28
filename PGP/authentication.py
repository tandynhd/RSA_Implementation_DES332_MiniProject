from encodings import utf_8
# from utils.sha1 import *
from rsa_main import *
import hashlib
# Authentication
# Sender
#1) Creates a clear text message
def sendS(message):
    print("==========================================")
    print("Authentication")
    #2) The sender creates a SHA-1 message digest of the clear-text message.
    digest = hashlib.sha1(bytes(message, 'utf-8')).hexdigest()
    # print(digest)
    #3) Encrypt the SHA-1 message digest using senders private key (RSA)
    cipher = RSAEpr(digest,Sender)
    # print(cipher)
    return(receiveS(cipher,message))

#Receiver
def receiveS(cipher,message):
    #4) Decrypt the RSA encrypted SHA-1 message digest using senders public key (RSA)
    decrypted = RSADpu(cipher,Sender)
    digest = hashlib.sha1(bytes(message, 'utf-8')).hexdigest()
    
    #5) The receiver dSHA-1 message digest of the clear-text message and matches it with the one decrypted
    if decrypted == digest:
        print("Digital signature true")
        print("Authentication Completed ")
        print("==========================================")    
        return(True,decrypted)
    else:
        print("Digital signature not true")
        return(False)

# sent = sendS("Hi i am tandin")
# bo,d=sent
# print(bo,d)