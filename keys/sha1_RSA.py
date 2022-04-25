import hashlib
# Code from https://www.geeksforgeeks.org/how-to-generate-large-prime-numbers-for-rsa-algorithm/

# Large Prime Generation for RSA
import random

# Pre generated primes
first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
     31, 37, 41, 43, 47, 53, 59, 61, 67,
     71, 73, 79, 83, 89, 97, 101, 103,
     107, 109, 113, 127, 131, 137, 139,
     149, 151, 157, 163, 167, 173, 179,
     181, 191, 193, 197, 199, 211, 223,
     227, 229, 233, 239, 241, 251, 257,
     263, 269, 271, 277, 281, 283, 293,
     307, 311, 313, 317, 331, 337, 347, 349]

def nBitRandom(n):
 return random.randrange(2**(n-1)+1, 2**n - 1)

def getLowLevelPrime(n):
 '''Generate a prime candidate divisible
 by first primes'''
 while True:
  # Obtain a random number
  pc = nBitRandom(n)

  # Test divisibility by pre-generated
  # primes
  for divisor in first_primes_list:
   if pc % divisor == 0 and divisor**2 <= pc:
    break
  else: return pc

def isMillerRabinPassed(mrc):
 '''Run 20 iterations of Rabin Miller Primality test'''
 maxDivisionsByTwo = 0
 ec = mrc-1
 while ec % 2 == 0:
  ec >>= 1
  maxDivisionsByTwo += 1
 assert(2**maxDivisionsByTwo * ec == mrc-1)

 def trialComposite(round_tester):
  if pow(round_tester, ec, mrc) == 1:
   return False
  for i in range(maxDivisionsByTwo):
   if pow(round_tester, 2**i * ec, mrc) == mrc-1:
    return False
  return True

 # Set number of trials here
 numberOfRabinTrials = 20
 for i in range(numberOfRabinTrials):
  round_tester = random.randrange(2, mrc)
  if trialComposite(round_tester):
   return False
 return True

def primeGen():
 while True:
  n = 1024
  prime_candidate = getLowLevelPrime(n)
  if not isMillerRabinPassed(prime_candidate):
   continue
  else:
   # print(n, "bit prime is: \n", prime_candidate)
   return(prime_candidate)

def ExtEuclidean(a, b):
 
    # in case one of the two input values are 0, the gcd is the other number and a is 1
    if b == 0 : 
        return a, 1, 0

    # otherwise we have a recursve function ExtEuclidean(b, a%b)
    c1, x1, y1 = ExtEuclidean(b, a%b)
    
    # we then update x and y using results of recursion
    c = c1
    x = y1 
    y = x1- (a//b) * y1
    
    return (c, x, y)

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

#Encryption
def encrypt(pub_key,plaintext):
    e,n=pub_key
    x=[]
    m=0
    for i in plaintext:
        if(i.isupper()):
            m = ord(i)-65
            c=(m**e)%n
            c+=600
            c=str(c)
            x.append(c)
        elif(i.islower()):               
            m= ord(i)-97
            c=(m**e)%n
            c=str(c)
            x.append(c)
        elif(i.isspace()):
            spc=400
            x.append(str(400))
        elif(i.isnumeric()):
            m= ord(i)
            c=500+m
            c=str(c)
            x.append(c)
    return x
     
 
#Decryption
def decrypt(priv_key,ciphertext):
    d,n=priv_key
    txt=ciphertext.split(',')
    #print(txt)
    x=''
    m=0
    for i in txt:
        if(i=='400'):
            x+=' '
        elif(int(i)>=548 and int(i)<=557):#numeric
            m=int(i)-548
            #print(m)
            c=str(m)
            #print(c)
            x+=c
        elif(int(i)>=600):#Upper case
            int_i=int(i)-600
            m=(int_i**d)%n
            m+=65
            c=chr(m)
            x+=c
        else:#lower case
            m=(int(i)**d)%n
            m+=97
            c=chr(m)
            x+=c
    return x

#Check license
def check_license(Oneway_hash,digital_signature):
    if Oneway_hash==digital_signature:
        print("Digital signature true")
    else:
        print("Digital signature not true")

#p=primeGen()
#q=primeGen()
p=11
q=17
e=13
n=p*q
phiOfn = (p-1)*(q-1)
_,d,_ = ExtEuclidean(e, phiOfn)
print("------------------------------------------------------------------------------")
print("d=",d)
print("------------------------------------------------------------------------------")
print("Public key = (e,n) = ", (e,n))
print("------------------------------------------------------------------------------")
print("Private key = (d,n) = ", (d,n))
print("------------------------------------------------------------------------------")


message=b"abc"
h = hashlib.new("sha1",message)
sha1text = h.hexdigest()
sha1text = str(sha1text)


# Test:
PR = (e,n)
PU = (d,n)

M=sha1text
#M="abcdefg0123456789A"
enc_msg = encrypt(PR,M)
print("message = ",M)
print("------------------------------------------------------------------------------")

ciphertext=""
for num in range(0,len(enc_msg)):
    ciphertext=ciphertext+enc_msg[num]
    if num < len(enc_msg)-1:
        ciphertext=ciphertext+","
C=ciphertext

print("Encryption result: C=", encrypt(PR,M))
print("------------------------------------------------------------------------------")
Mdash = decrypt(PU, C)


print("Decrypt C got:", Mdash)
print("------------------------------------------------------------------------------")

check_license(M,Mdash)

#print(ord('0'))
#print(ord('1'))
#print(ord('2'))

