def drucke_dict(dictt):
    for key in dictt:
        print("Schlüssel ", key," ",type(key)," Wert", dictt[key], " ", type(dictt[key]))
        dictt.update({key:"Napolie"})
    return dictt
    
dict_test = {1:"a ́Suppe",2:"Canneloni",3:"Pizza"}
test = drucke_dict(dict_test)
print(test)
print(dict_test)