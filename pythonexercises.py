havadurumu = "karlı"
if havadurumu == "yağışlı":
    print("şemsiye almalısın")
elif havadurumu == "karlı":
    print("kayak yapmalısın")
else:
    print("şemsiye alma")





yas=35
if yas<18:
    print("çocuk")
elif yas<65:
    print("yetişkin")
else:
    print("emekli")




liste=["a","b","c","d","e"]

hedef_harf="k"

if hedef_harf in liste:
    print("hedef harf listede var")
else:
    liste.append(hedef_harf)
    print("hedef harf listede yoktu eklendi artık var")
    print("Güncel liste {}".format(liste))




if hedef_harf in liste  and hedef_harf==liste[0]:
    print("buldum ve ilk konumda")
elif  hedef_harf in liste:
    print( "buldum ama ilk konumda değil")
else:
    liste.append(hedef_harf)
    print("hedef harf listede yoktu eklendi artık var")
    print("Güncel liste {}".format(liste))



