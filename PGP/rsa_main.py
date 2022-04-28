from math import *
from utils.binstr import *
from utils.moduloExpon import *
from utils.EDbitseq import *
from utils.keyGen import *
def keys():
    e,d,n,p,q,phiOfn = keyGen()
    while d<0:
        e,d,n,p,q,phiOfn = keyGen()
    
    return (e,n),(d,n)

def RSAEpu(M,K):
    PU,PR = K
    M_bins = strToBinStr(M)
    M_cipher = rsaEncrypt(PU,M_bins)
    # print(M_cipher)
    return(M_cipher)

def RSADpr(M_cipher, K):
    PU,PR = K
    M_decryptedBs = rsaDecrypt(PR,M_cipher)
    # print(M_decryptedBs)
    M_decrypted = binStrToStr(M_decryptedBs)
    # print(M_decrypted)
    return(M_decrypted)

def RSAEpr(M,K):
    PU,PR = K
    M_bins = strToBinStr(M)
    M_cipher = rsaEncrypt(PR,M_bins)
    # print(M_cipher)
    return(M_cipher)

def RSADpu(M_cipher, K):
    PU,PR = K
    M_decryptedBs = rsaDecrypt(PU,M_cipher)
    # print(M_decryptedBs)
    M_decrypted = binStrToStr(M_decryptedBs)
    # print(M_decrypted)
    return(M_decrypted)

# M = "Hello what is your name my name is tandin.?!"
# cipher = RSAEpu(M,Sender)
# decrypted = RSADpr(cipher,Sender)
# print(decrypted)




