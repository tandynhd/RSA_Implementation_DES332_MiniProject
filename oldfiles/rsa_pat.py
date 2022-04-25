#Patsaphon Chandhakanond 6222782375 SIIT DE
#DES332 Section1 

#compute the multiplicative inverse
#of e modulo phi(p*q) efficiently,
#where p, q are two prime numbers and e is some integer small than phi(p*q)
#so that gcd(e, phi(p*q)) = 1

# Purpose: given integer e, two prime numbers p and q such that gcd(e, phi(p*q)) = 1,
#return d such that d*e = 1 mod phi(n)

# note:

from keyGen import keyGen

#Encryption
def encrypt(pub_key,plaintext):
    e,n=pub_key
    x=[]
    m=0
    for i in plaintext:
        if(i.isupper()):
            m = ord(i)-65+1
            c=(m**e)%n
            c=str(c)
            x.append(c)
        elif(i.islower()):               
            m= ord(i)-97+1
            c=(m**e)%n
            c=str(-1*c)
            x.append(c)
        elif(i.isspace()):
            spc=400
            x.append(str(400))
        elif(i == "."):
            x.append(str(401))
        elif(i == "!"):
            x.append(str(402))
    return x
     
 
#Decryption
def decrypt(priv_key,ciphertext):
    d,n=priv_key
    txt=ciphertext.split(',')
    print(txt)
    x=''
    m=0
    for i in txt:
        if(i=='400'):
            x+=' '
        elif(i=='401'):
            x+="."
        elif(i=='401'):
            x+="!"
        elif (int(i)<0):
            i=-1*int(i)
            m=(int(i)**d)%n-1
            m+=97
            c=chr(m)
            x+=c
        elif (int(i)>0):
            m=(int(i)**d)%n-1
            m+=65
            c=chr(m)
            x+=c
        
    return x


e,d,n = keyGen()

message="Hello World."

print("ANS --> The multiplicative inverse of e modulo phi(p*q) is",d)
print("Public key = (e,n) = ", (e,n))
print("Private key = (d,n) = ", (d,n))

publickey = (e,n)
privatekey = (d,n)

enc_msg=encrypt(publickey,message)

print("Your message is:",message)
print("Your encrypted message is:",enc_msg)

ciphertext=""
for num in range(0,len(enc_msg)):
    ciphertext=ciphertext+enc_msg[num]
    if num < len(enc_msg)-1:
        ciphertext=ciphertext+","
#print(ciphertext)
#print(ciphertext.split(','))
print("Your decrypted message is:",decrypt(privatekey,ciphertext))
#print(ord('A'))
#print(ord('a'))


e,n
d,n


e,n
d,n






