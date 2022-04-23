#Patsaphon Chandhakanond 6222782375 SIIT DE
#DES332 Section1 

#compute the multiplicative inverse
#of e modulo phi(p*q) efficiently,
#where p, q are two prime numbers and e is some integer small than phi(p*q)
#so that gcd(e, phi(p*q)) = 1

# Purpose: given integer e, two prime numbers p and q such that gcd(e, phi(p*q)) = 1,
#return d such that d*e = 1 mod phi(n)

# note:



#multiplicative inverse
def multiplicative_inverse(e, p, q):
    if isinstance(e, int) and isinstance(p, int) and isinstance(q, int):#check that e p q are integer or not
        checkp=True
        checkq=True
        checke=False
        if p>1 and q>1:
            for i in range(2,p):#check p is prime number or not
                if p%i==0:
                    checkp=False
                    print("invalid input. p must be a prime number")
                    break
            for i in range(2,q):#check q is prime number or not
                if q%i==0:
                    checkq=False
                    print("invalid input. q must be a prime number")
                    break
            if checkp==True and checkq==True:
                #gcd calculation
                x=e # x is the gcd(e,(p-1)*(q-1)) or gcd(e, phi(p*q))
                y=(p-1)*(q-1) #y=phi(n)
                while(y):
                   x, y = y, x % y
                #print(x) # x is the gcd(e,(p-1)*(q-1)) or gcd(e, phi(p*q))
                if e<(p-1)*(q-1):#check condition of e that e is some integer small than phi(p*q)
                    if x==1:#check condition of e that gcd(e, phi(p*q)) = 1
                        checke=True
                    else:
                       print("invalid input. gcd(e, phi(p*q)) must be equal to 1 or e must be relatively prime to phi(n)")
                else:
                    print("invalid input. e must smaller than phi(p*q)")
                
                if checke==True:
                    for d in range(1, (p-1)*(q-1)):#Calculate the multiplicative inverse of e modulo phi(p*q)
                        if d*e % ((p-1)*(q-1)) == 1:
                            print("e =",e)
                            print("p =",p)
                            print("q =",q)
                            break
                else:
                    d=None
            else:
                d=None
        else:
            print("invalid input. p and q must be a prime number (Cannot smaller than 1)")
            d=None
    else:
        print("e, p, q must be integer")
        d=None
    return d

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
        elif(i == "|"):
            x.append(str(401))
        elif(i == "}"):
            x.append(str(402))
        elif(i == "]"):
            x.append(str(403))
        elif(i == "{"):
            x.append(str(404))
        elif(i == "["):
            x.append(str(405))
        elif(i == "'"):
            x.append(str(406))
        elif(i == ";"):
            x.append(str(407))
        elif(i == ":"):
            x.append(str(408))
        elif(i == "?"):
            x.append(str(409))
        elif(i == "/"):
            x.append(str(410))
        elif(i == "."):
            x.append(str(411))
        elif(i == ">"):
            x.append(str(412))
        elif(i == ","):
            x.append(str(413))
        elif(i == "<"):
            x.append(str(414))
        elif(i == "!"):
            x.append(str(415))
        elif(i == "@"):
            x.append(str(416))
        elif(i == "#"):
            x.append(str(417))
        elif(i == "$"):
            x.append(str(418))
        elif(i == "%"):
            x.append(str(419))
        elif(i == "^"):
            x.append(str(420))
        elif(i == "&"):
            x.append(str(421))
        elif(i == "*"):
            x.append(str(422))
        elif(i == "("):
            x.append(str(423))
        elif(i == ")"):
            x.append(str(424))
        elif(i == "-"):
            x.append(str(425))
        elif(i == "_"):
            x.append(str(426))
        elif(i == "="):
            x.append(str(427))
        elif(i == "+"):
            x.append(str(428))
    return x

# Problem symbols - > \ , " , 
 
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
            x+="|"
        elif(i=='402'):
            x+="}"
        elif(i=='403'):
            x+="]"
        elif(i=='404'):
            x+="{"
        elif(i=='405'):
            x+="["
        elif(i=='406'):
            x+="'"
        elif(i=='407'):
            x+=";"
        elif(i=='408'):
            x+=":"
        elif(i=='409'):
            x+="?"
        elif(i=='410'):
            x+="/"
        elif(i=='411'):
            x+="."
        elif(i=='412'):
            x+=">"
        elif(i=='413'):
            x+=","
        elif(i=='414'):
            x+="<"
        elif(i=='415'):
            x+="!"
        elif(i=='416'):
            x+="@"
        elif(i=='417'):
            x+="#"
        elif(i=='418'):
            x+="$"
        elif(i=='419'):
            x+="%"
        elif(i=='420'):
            x+="^"
        elif(i=='421'):
            x+="&"
        elif(i=='422'):
            x+="*"
        elif(i=='423'):
            x+="("
        elif(i=='424'):
            x+=")"
        elif(i=='425'):
            x+="-"
        elif(i=='426'):
            x+="_"
        elif(i=='427'):
            x+="="
        elif(i=='428'):
            x+="+"

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

e=11
p=17
q=13
n=p*q
d=multiplicative_inverse(e,p,q)
message="Hello My name is Tandin Dorji. What is yours? | } ] ' ; : / ? . > , <"

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







