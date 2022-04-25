from math import *
from utils.binstr import *
from utils.moduloExpon import *
from utils.EDbitseq import *
from utils.keyGen import *

e,d,n,p,q,phiOfn = keyGen()
while d<0:
    e,d,n,p,q,phiOfn = keyGen()


# epqnd 11 17 13 221 35
# PU = (11,221)
# PR = (35,221)

PU = (e,n)
PR = (d,n)

M = "Hello what is your name my name is tandin.?!"
M_bins = strToBinStr(M)
M_cipher = rsaEncrypt(PU,M_bins)
print(M_cipher)
M_decryptedBs = rsaDecrypt(PR,M_cipher)
print(M_decryptedBs)
M_decrypted = binStrToStr(M_decryptedBs)
print(M_decrypted)






# test = 
# print(test)
# # test2 = binStrToStr(test)
# # print(test2)

# binary = bstoBinary(test)
# print(binary)
# string = toString(binary)
# print(string)

