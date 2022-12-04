def bubbelsort(listin):
    n = len(listin)
    for i in range(0, n-1):
        for j in range(0, n-1):
            if listin[j] > listin[j+1]:
                listin[j], listin[j+1] = listin[j+1], listin[j]
    return listin


listin = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]
listout = []
for i in range(len(listin)):
    listout.append(listin[i])

bubbelsort(listin)
print(listout)
print(listin)


stud_d = {
    "123550": "Paul Panzer",
    "168980": "Hans Wurst",
    "123456": "Peter Lustig",

}

ausgabe = bubbelsort=list(stud_d.keys())
print([(i,stud_d[i]) for i in ausgabe])