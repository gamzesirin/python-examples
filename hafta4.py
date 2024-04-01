# num = int(input("sayı: "))
# if num >0:
#     print("sayı pozitif")
# elif num <0:
#     print("sayı negatif")
# else:
#     print("sayı sıfır")

#devrek123.A => doğuş teknoloji şifre
    
# isim = input("isim giriniz : ")
# yas= int(input("yaşınızı giriniz : "))
# egitim =input("eğitim bilgilerininizi giriniz : ")

# # if(yas>=18) and (egitim=="lise") or (egitim == "üniversite"):
# #     print("ehliyet alabilirsiniz")
# # else:
# #     print("ehliyet alamazsınız")

# if(yas>=18):
#     if(egitim=="lise") or (egitim == "üniversite"):
#         print(f"{isim} ehliyet alabilirsiniz")
#     else:
#         print(f"{isim} ehliyet alamazsın çünkü eğitim durumu yetersiz")
# else:
#     print(f"{isim} ehliyet alamazsınız yaşın tutmuyor")


# yaz1=float(input("yazılı 1 notunu girin : "))
# yaz2=float(input("yazılı 2 notunu girin : "))
# söz1=float(input("sözlü 1 notunu girin : "))
# ortalama = float((yaz1+yaz2+söz1)/3)
# print(ortalama,"ortalama")
# if(ortalama>=0) and (ortalama<=24):
#     print("notunuz 0")
# elif(ortalama>=25)and (ortalama<=44):
#     print("notunuz 1")
# elif(ortalama>=45)and (ortalama<=54):
#     print("notunuz 2")
# elif(ortalama>=55)and (ortalama<=69):
#     print("notunuz 3")
# elif(ortalama>=70)and (ortalama<=84):
#     print("notunuz 4")
# elif(ortalama>=85)and (ortalama<=100):
#     print(f" ortalamanız {ortalama} notunuz 5")


# import datetime

# tarih=input("aracınız hangi tarihte trafiğe çıktı ( 2020/10/10 ) : ")
# tarih=tarih.split("/")
# trafige_cikis=datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))

# simdi=datetime.datetime.now()
# fark=simdi-trafige_cikis
# days=fark.days

# if(days<=365):
#     print("1. servis aralığı")
# elif(days >365) and (days<=365*2):
#     print("2. servis aralığı")
# elif(days >365*2) and (days<=365*3):
#     print("2. servis aralığı")
# else:
#     print("servis dışı")




# sayi= int(input("sayı giriniz : "))

# if(sayi>0):
#     if(sayi%2==0):
#         print(f"{sayi} pozitif ve çift sayıdır")
#     else:
#         print(f"{sayi} pozitif ve tek sayıdır")
# elif(sayi==0):
#     print(f"{sayi} nötr sayıdır")
# else:
#     print(f"{sayi} pozitif değildir")


# sayi1= int(input("sayı 1 giriniz : "))
# sayi2= int(input("sayı 2 giriniz : "))
# sayi3= int(input("sayı 3 giriniz : "))

# if(sayi1>sayi2) and (sayi1>sayi3):
#     print(f"{sayi1} en büyük sayıdır")
# elif(sayi2>sayi1) and (sayi2>sayi3):
#     print(f"{sayi2} en büyük sayıdır")
# elif(sayi3>sayi2) and (sayi3>sayi1):
#     print(f"{sayi3} en büyük sayıdır")


# yaz1=float(input("yazılı 1 notunu girin : "))
# yaz2=float(input("yazılı 2 notunu girin : "))
# final=float(input("final notunu girin : "))
# ortalama = float(((yaz1+yaz2)*40/100+final*60/100))
# print(ortalama,"ortalama")
# if(ortalama>=50) and (final>=50):
#     print("öğrenci geçti")
# elif(final>=70):
#     print("öğrenci geçti")
# else:
#     print("öğrenci geçemedi")



# isim = input("isim giriniz : ")
# kilo= float(input("kilonuuz giriniz : "))
# boy =float(input("boyunuzu giriniz : "))

# vki = kilo/(boy**2)

# if(vki >=0) and (vki<=18.4):
#     print(f"{isim} zayıftır")
# elif(vki>18.4) and (vki<=24.9):
#     print(f"{isim} normaldir")
# elif(vki>=25.0) and (vki<=29.9):
#     print(f"{isim} fazla kilolu")
# elif(vki>=30.0) and (vki<=34.9):
#     print(f"{isim} şişman (obez)")



sayilar=[1,2,3,4,5]
for sayi in sayilar:
    print(sayi)

isimler=["ali","veli","ayşe"]
for isim in isimler:
    print(f"my name is {isim}")

tuple=[(1,2),(3,4),(9,8)]
for a,b in tuple:
    print(a,b)

name="ali"
for n in name:
    print(n)

d={"k1":1,"k2":2,"k3":3}
for key,value in d.items():
    print(key,value)

result = list(range(50))
print(result)

for i in range(5):
    print("merhaba") #print(i)

for i in range(50,100):
    print(i)

for i in range(50,100,2):
    print(i)


sayilar=[1,3,5,7,9,12,19,21]

for i in sayilar:
    if(i%3==0):
        print(f"{i} sayısı 3 ün katıdır")



toplam=0
for i in sayilar:
    toplam+=i
print(toplam)


liste=[]
for i in sayilar:
    if(i%2!=0):
        a=i**2
        print(a)
        liste.append(a)
        print(liste)


        
sehirler=["kocaeli","istanbul","ankara","izmir","rize"]
for i in sehirler:
    if(len(i)<=5):
        print(i)


urunler = [
  {'name':'samsung S6', 'price': '3000' },
  {'name':'samsung S7', 'price': '4000' },
  {'name':'samsung S8', 'price': '5000' },
  {'name':'samsung S9', 'price': '6000' },
  {'name':'samsung S10', 'price': '7000' }
]

toplam=0

for urun in urunler:
    fiyat=int(urun["price"])
    toplam+=fiyat
print("toplam ürün fiyatı",toplam)


for urun in urunler:
    fiyat=int(urun["price"])
    if(fiyat<=5000):
        print(urun["name"])


