#The ExtEuclidean function give three outputs c,x,y
# where c is the greatest common denominator (gcd)
# and x and y are from the Diophantine equation (ax+by=c)
#Using algorithm1 from the lecture notes

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

