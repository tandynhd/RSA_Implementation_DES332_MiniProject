from rsaMain import *
from keyGen import *

es,ds,ns=keyGen()

er,dr,nr=keyGen()

test = clearTextBin("W")
print(test)
print("Encryption")
cipher = rsaEncrypt((ds, ns), test)
print(cipher)

print("Decryption")

decryptedClearText = rsaDecrypt((es,ns),cipher)
print(decryptedClearText)
# print(binStrToStr(decryptedClearText))

if decryptedClearText == test:
    print (9)