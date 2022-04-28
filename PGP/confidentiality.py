from encodings import utf_8
from utils.AESED import *
from rsa_main import *
import os

# Confidentiality
# Sender
def sendM(message, digitalSign,Receiver):
    print("==========================================")
    print("Confidentiality Checking")
    #1) The sender generates a random128-bit (16 bytes) number to be used as SSSK
    sssk = os.urandom (16)
    #2) The sender encrypts the clear-text message, and appended digital signature,using a symmetric encryption algorithm (AES) with the SSSK
    # message = bytes(message, 'utf-8')
    aesE = AESE(message,sssk)
    blackString = aesE+"|"+digitalSign
    # key,plaintext = sha1E
    sssks = str(sssk)
    # print(sha1E)
    #3) Encrypt the SSSK using RSA with each recipient’s public key(s) & append each uniquely encrypted copy of the SSSK to the black-text message
    cipher = RSAEpu(sssks,Receiver)
    blackString = blackString + "|"+cipher
    # print(cipher)
    return(receiveM(blackString,sssk,Receiver))

#Receiver

def receiveM(blackstring,sssk,Receiver):
    aesE,digitalsign,cipher = blackstring.split("|")
    #4) Decrypt the RSA encrypted SSSK using their private key (RSA)
    decrypted = RSADpr(cipher,Receiver)
    # print(decrypted)
    # print(sssk)
    #5) The receiver recovers the clear text message using SSSK
    if decrypted == str(sssk):
        message = AESD(aesE,sssk)
        print("Email Integrity Maintained")
        print("Confidentialty Check Completed ")
        print("==========================================")
        print("Email Sent and Received Successfully")
        message = str(message)[2:-1]
        return(message)  
    else:
        print("Email Integrity not maintained")
        return("Email has been tampered")
    

# sent = sendM("Hi i am tandin", "3cd013da8e848fc2bab3d805ed9df6b1f006d0fd")
# print(sent)