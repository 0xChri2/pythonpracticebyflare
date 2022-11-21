import math
def atan_f(x, eps):
    summe = x
    vorzeichen = 1
    zaehler = x
    nenner = 1
    while True:
        alt = summe
        vorzeichen *= -1
        zaehler *= x * x
        nenner += 2
        summe += vorzeichen * zaehler / nenner
        if abs(alt - summe) >= eps:
            continue
        else:
            break
    return summe
x= 0.4
eps = 0.00000000000000001
print("x",x,"eps", eps, "atan_f(x,eps)",atan_f(x,eps),
"atan(x)",math.atan(x))