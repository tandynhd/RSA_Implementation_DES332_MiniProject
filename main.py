from rsaMain import *
from keyGen import *

es,ds,ns,ps,qs=keyGen()

# er,dr,nr,pr,qr=keyGen()

test = clearTextBin("W")
print(test)
print("Encryption")
cipher = rsaEncrypt((ds, ns), test)
print(cipher)

print("Decryption")

decryptedClearText = rsaDecrypt((es,ns),cipher)

# decryptedClearText = chineseRemainder(cipher,ds,ps,qs)
print(decryptedClearText)
# print(binStrToStr(decryptedClearText))
