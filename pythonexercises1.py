yorum_birakanlar=["eda melik","deniz eren","sevda selen","derya kuşluk"]

for kullanici in yorum_birakanlar:
    print(kullanici) #her bir indexteki elemana tektek uğrayarak çalışır

kullanici_sayisi =0
for kullanici in yorum_birakanlar:
    kullanici_sayisi=kullanici_sayisi+1
    print(kullanici_sayisi,kullanici)


kullanici_sayisi =0
for kullanici in yorum_birakanlar:
    kullanici_sayisi=kullanici_sayisi+1
    ad,soyad =kullanici.split()[0],kullanici.split()[1]
    print("{0}. kullanıcının adı {1} ve soyadı {2}".format(kullanici_sayisi,ad,soyad))



moderator="deniz eren"
kullanici_sayisi =0
moderator_sayisi=0
for kullanici in yorum_birakanlar:
    ad,soyad =kullanici.split()[0],kullanici.split()[1]
    if(kullanici==moderator):
        moderator_sayisi+=1
        print("{0}. moderatorün adı {1} ve soyadı {2}".format(moderator_sayisi,ad,soyad))
    else:
        kullanici_sayisi+=1
    print("{0}. kullanıcının adı {1} ve soyadı {2}".format(kullanici_sayisi,ad,soyad))


