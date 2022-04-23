
from math import *
from primeGen import primeGen
from extEuclid import ExtEuclidean

def keyGen():
    #1024 bit Pirme Numbers for p and 1
    p = primeGen()
    print("p = ", p)
    q = primeGen()
    print("q = ", q)

    n = p*q
    print("n= pq =", n)

    phiOfn = (p-1)*(q-1)
    # φ(n) is Euler totient function, which returns the number of positive intergers less than n that are relatively prime to n
    print("phi(n) = ", phiOfn)

    #Select e: gcd(φ(n),e) = 1, 1 < e < φ(n)
    # enc = []
    # print("possible values for e:")
    # #actually need to check from 1 to phiOfn but that takes a long time
    # for e in range(1,100000):
    #               if gcd(e,phiOfn)==1:
    #                   enc.append(e)
                        
    # print(enc)

    # #Taking a random number from enc to be e
    # e = enc[3]
    e = 65537
    print("e=",e)
    # verify that gcd(e,phiOfn) = 1
    if gcd(e,phiOfn) == 1:
        print("Good! e is relatively prime to phi(n)")
    else:
        print("Bad! e is not relatively prime to phi(n)")
        exit()

    # determine d such that de mod phiOfn = 1 and d <  phiOfn

    _,d,_ = ExtEuclidean(e, phiOfn)
    print("d=",d)
    print("Public key = (e,n) = ", (e,n))
    print("Private key = (d,n) = ", (d,n))
    return(e,d,n)

keyGen()