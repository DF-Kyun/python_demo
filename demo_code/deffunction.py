import math
def quadratic(a, b, c):
    d=math.sqrt(b*b-4*a*c)
    a1=(-b+d)/(2*a)
    a2=(-b-d)/(2*a)
    return a1,a2
print(quadratic(2,3,1))
print(quadratic(1,3,-4))
    
