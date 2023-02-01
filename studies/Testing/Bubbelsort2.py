def Bubbelsort(list):
    n = len(list)
    for i in range(0,n-1):
        for j in range(0,n-1):
            if(list[j] > list[j+1]):
                tmp = list[j]
                list[j] = list[j+1]
                list[j+1] = tmp

    return list

list1 = [2,8,4,1,2,5,6,9,2,1,3]
list2 = Bubbelsort(list1)
print(list2)

stud = {
    321: "Florian",
    123: "Michael",
    999: "Marcus",
    876: "Markus",
    1: "Gudrun"

}
stud2 = {}
sortedkeys = Bubbelsort(list(stud.keys()))
print(sortedkeys)
for i in range(0, len(sortedkeys)-1):
    stud2[sortedkeys[i]] = stud[sortedkeys]
    
