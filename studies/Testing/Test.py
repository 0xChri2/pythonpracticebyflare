def bubblesort(liste):
        n = len(liste)
        for i in range(0, n-1):
            for j in range(0, n-1):
                if liste[j] > liste[j+1]:
                    tmp = liste[j]
                    liste[j] = liste[j+1]
                    liste[j+1] = tmp
                    print(liste)
        return liste
ls = list(range(20, 0, -2))
ls = bubblesort(ls)
stud = {
 321: "Florian",
 123: "Michael",
 999: "Marcus",
 876: "Markus",
 1: "Gudrun"
}
sorted_keys = bubblesort(list(stud.keys()))
for key in sorted_keys:
    print(key, stud[key])