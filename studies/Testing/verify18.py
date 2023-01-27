peranz = input("Wie viele Personen nehmen an der Berfragung Teil?")
count  = 0
persu18 = {}
while(count < int(peranz)):
    alter = input("Wie alt bist du?")
    name = input("Wie ist dein Name?")
    if(int(alter) < 18):
        count = count + 1
        persu18.update({name: int(alter)})
    else:
        count = count + 1
print(persu18)