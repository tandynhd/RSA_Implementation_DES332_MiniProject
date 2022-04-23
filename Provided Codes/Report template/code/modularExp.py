
def decimalToBinary(m):
    return "{0:b}".format(int(m))


# Purpose: to compute a**m mod n efficiently
# where: a, m, n are integers

# Example: effModuloExp(2, 10, 15) returns 2**10%15 = 4


def effModuloExp(a, m, n):
    # convert m into binary
    bits = decimalToBinary(m)
    
    d = 1
    for bi in bits:
        d = d*d % n
        if bi != "0":
            d = (d*a) % n      
    return d

# tests:
#print("(1000000000000**1000000)%100 = ", effModuloExp(1000000000000, 1000000, 100))


print("Try this expression directly?", (1000000000000**1000000)%100)
