n = input("Geben Sie eine Zahl ein: ")
sum = 0
n = int(n)
for i in range(n):
    sum = pow(i,n)
    print(sum)
    
j = 0
sum = 0
while(j< 10):
    print
    j = j + 1
    sum = pow(j,n)
    print(sum)