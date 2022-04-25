from moduloExponentiation import *
from extEuclid import *


def chineseRemainder(c,d,p,q):
    dp = d%(p-1)
    dq = d%(q-1)
    # qinv = q**-1%(p-1)
    qinv = effModuloExp(q,-1,(p-1))
    return crDecrypt(c,dp,dq,p,q)

def crDecrypt(c,dp,dq,p,q):
    # m1 = c**dp%p
    m1 = effModuloExp(c,dp,p)
    # m2=c**dq%q
    m2 = effModuloExp(c,dq,q)
    # h=q**-1*(m1-m2)%p
    h = effModuloExp(q,(-1*(m1-m2)),p)
    m=(m2+h*q)%(p-q)
    return m


c=11
p=11
q=17
e=13
n=p*q
phiOfn = (p-1)*(q-1)
_,d,_ = ExtEuclidean(e, phiOfn)

print(c,p,q,e,n,phiOfn,d)

print(chineseRemainder(c,d,p,q))