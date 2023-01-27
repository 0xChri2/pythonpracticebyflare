def Bubbelsort(list):
    n = list.lenght
    for i in range(0,n-1):
        for j in range(0,n-2):
            if(list[j] > list[j+1]):
                tmp = list[j]
                list[j] = list[j+1]
                list[j+1] = tmp

    return list