from keyGen import keyGen
# test: rsaEncrypt((77,143),88)

e,d,n = keyGen()

def rsaEncrypt(key, M):
       (e,n) = key
       # plainNum in [0,n-1], 
       C = M**e % n
       return C


def rsaDecrypt(key, C):
       (d,n) = key
       M = C**d % n
       return M     
       

# one function for both encryption and descryption

def rsaED(key,Input):
       (n,ed)=key
       Out = Input**ed % n
       return Out

# Test:
 
PR = (e,n)
PU = (d,n)


M = 90
print("M=", M)
C = rsaEncrypt(PR,M)
print("Encryption result: C=", rsaEncrypt(PR,M))
Mdash = rsaDecrypt(PU, C)

print("Decrypt C got:", Mdash)


