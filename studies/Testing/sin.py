import math 

def fak(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

def sin_f(x,n):
    i = 0
    sin = 0.0
    for i in range(i, n):
        sin = sin + (pow(-1,i)*pow(x,2*i+1)/fak(2*i+1))
    return sin
    
n = 20
x = 0.88
print("sinus(", x ," , ",n,") = ", sin_f(x,n))
print("sinus-math.h(",x,") = ",math.sin(x))