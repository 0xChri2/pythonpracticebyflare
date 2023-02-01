def tauschvalue(a, b):
    return b,a

def tausche_referenz(a, b):
    a[0], b[0] = b[0], a[0]

a = [10] 
b = [12]

#a, b = tausche_value(a,b)
tausche_referenz(a,b)

print("a: ",a)
print("b: ",b)