# Computes the modulo exponentiation
# a**m mod n efficiently
# where a,n are integers adn m is a binary number
# def efficientModuloExponentiation()


# eg a = 2, n = 16, m = 44 = 101110
# eME(2, "101110", 16)
def effModuloExp(a,m,n):
    # if input m is an integer, need to convert into binary
    m = bin(m)[2:]
    d = 1
    for bi in m:
        d = (d*d)%n
        if bi != "0":
            d = (d*a)%n
    return d


# # tests:
# print("(1000000000000**1000000)%100 calculated directly using  effModuloExp is: ")
# print("(1000000000000**1000000)%100 = ",effModuloExp(1000000000000, 1000000, 100))

# print("(1000000000000**1000000)%100 calculated directly is: ")
# print("(1000000000000**1000000)%100 = ",(1000000000000**1000000)%100)
