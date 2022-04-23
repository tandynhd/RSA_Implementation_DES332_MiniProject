
from math import *

input("1. Choose primes p and q, and calculate n = pq")

p = input("p = ")
if p == "":
       p= "17"
p = int(p)
print("set p = ", p)

q = input("q = ")
if q == "": q = "13"
q = int(q)
print("set q = ", q)

n = p*q



print("n= pq =", n)

phiOfn = (p-1)*(q-1)
# φ(n) is Euler totient function, which returns the number of positive
# intergers less than n that are relatively prime to n

print("phi(n) = ", phiOfn)

print("Select e: gcd(φ(n),e) = 1, 1 < e < φ(n)")

print("possible values for e:")
for e in range(1,phiOfn):
              if gcd(e,phiOfn)==1:
                     print(e, end = ",")

e = input("e = ")
if e == "":
       e = 11
e = int(e)


# verify that gcd(e,phiOfn) = 1

print(gcd(e,phiOfn))

if gcd(e,phiOfn) == 1:
       print("Good! e is relatively prime to phi(n)")
else:
       print("Bad! e is not relatively prime to phi(n)")
       exit()

# determine d such that de mod phiOfn = 1 and d <  phiOfn

for d in range(1, phiOfn):
       if d*e%phiOfn==1:
              print("d = ", d)
              break
       
print("Public key = (e,n) = ", (e,n))
print("Private key = (d,n) = ", (d,n))

