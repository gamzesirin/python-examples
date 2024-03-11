liste=["banana","grape","apple"]
liste.append("strawberry")#en sına ekler
print(liste)

liste=["banana","grape","apple"]
liste.insert(2,"cherry")#istenilen indise ekler
print(liste)



liste=["banana","grape","apple"]
liste.remove("apple")#istenilen elemanı siler
print(liste)


liste=["banana","grape","apple"]
liste.pop(1) #istenilen indisteki elemanı siler , index no verilmezse son elemanı siler
print(liste)


liste=["banana","grape","apple"]
del liste[2] #istenilen indisteki elemanı siler , index no verilmezse tamamen siler
print(liste)

# liste=["banana","grape","apple"]
# del liste
# print(liste)

liste=["banana","grape","apple"]
liste.clear() #liste temizler
print(liste)


# liste kopyalamak

a=["banana","grape","apple"]
b=["GARLIC","ONION","POTATO"]
a=b #  bellekteki adresleri aynı olmuş oldu , yani a ve b aynı listeyi gösterir , birinde yapılan değişiklik diğerini de etkiler bu işlem referans atama işlemidir bu işlmede başlangıç adresi ve uzunluk gider
print(a)
print(b)
b[0]="strawberry"
print(a,b)

a=["banana","grape","apple"]
b=["GARLIC","ONION","POTATO"]
a=b.copy() #b listesini a ya kopyalar
print(a)
print(b)
b[0]="strawberry"
print(a,b)

a=["banana","grape","apple"]
b=["GARLIC","ONION","POTATO"]
a=list(b) #b listesini a ya kopyalar ama liste yerine başka bir veri tipi kopyalanmak istenirse bu yöntem kullanılır onu da listeye çevirir
b[0]="strawberry"
print(a,b)

# sort komutu küçükten büyüğe sıralar
nummbers=[1,4,3,2,5,7,6,9,8]
nummbers.sort()
print(nummbers)
letters=["a","c","b","e","d","g","f"]
letters.sort()
print(letters)

# sort(reverse=True) komutu büyükten küçüğe sıralar
nummbers=[1,4,3,2,5,7,6,9,8]
nummbers.sort(reverse=True) #büyükten küçüğe sıralar true yerine 1 de yazılabilir
print(nummbers)
letters.sort(reverse=True) #büyükten küçüğe sıralar true yerine 1 de yazılabilir
print(letters)

nummbers=[1,4,3,2,5,7,6,9,8]
letters=["a","c","b","e","d","g","f"]

print(max(nummbers)) #en büyük elemanı verir
print(min(nummbers)) #en küçük elemanı verir
print(min(letters)) #en küçük elemanı verir
print(max(letters)) #en büyük elemanı verir


nummbers=[1,4,3,2,5,7,6,9,8]
letters=["a","c","b","e","d","g","f","a"]
print(nummbers.count(3)) 
print(letters.count("a"))




names = ['Ali','Yağmur','Hakan','Deniz']

years = [1998, 2000, 1998, 1987]

names.append("cenk") #listenin sonuna ekler
print(names)

names.insert(0,"sena") #listenin başına ekler
print(names)

names.insert(-1,"edanur") #listenin sondan bir önceki elemanına ekler
print(names)

names.insert(len(names),"selin") #listenin sonuna ekler
print(names)


names.remove("Deniz") #istenilen elemanı siler
print(names)

names.pop()
print(names)

names.pop(0) #istenilen indisteki elemanı siler , index no verilmezse son elemanı siler
print(names)


print(names.index("Hakan"))#istenilen elemanın index numarasını verir

index=names.index("Hakan")
names.pop(index)
print(names)

result = "Ali" in names
print(result)

result2 =names.index("Ali")
print(result2)

names.reverse()
print(names)


names = ['Ali','Yağmur','Hakan','Deniz']

years = [1998, 2000, 1998, 1987]

names.sort()
print(names)

years.sort()
print(years)


# sınav
str="Cheery,Apple,Banana"
str2=str.split(",") #virgülle ayırarak listeye çevirir
print(str2)
type(str2)


print(min(years))
print(max(years))

# iç içe olan min max bulma ------------------sınav

years = [1998, 2000, 1998, 1987]
print(years.count(1998))

years = [1998, 2000, 1998, 1987]
years.clear()
print(years)

# marka1=input("enter a brandname :")
# marka2=input("enter a brandname :")
# marka3=input("enter a brandname :")

# markalar=[marka1,marka2,marka3]
# print(markalar)




# markalar=[]
# marka=input("enter a brandname :")
# markalar.append(marka)
# print(markalar)




# sayi1=int(input("enter a number :"))
# sayi2=int(input("enter a number :"))
# sayi3=int(input("enter a number :"))

# sayilar=[]
# sayilar.append(sayi1)
# sayilar.append(sayi2)
# sayilar.append(sayi3)
# print(min(sayilar))
# print(max(sayilar))
# # ortalama=(sayi1+sayi2+sayi3)/3
# ortalama=(sayilar[0]+sayilar[1]+sayilar[2])/len(sayilar)
# print(ortalama)


a=10
b=20
if a<b:
    print("a küçüktür b")

a=10
b=10
if a>b:
    print("a büyüktür b")
elif a==b:
    print("a eşittir b")




a=20
b=10
if a>b:
    print("a büyüktür b")
elif a==b:
    print("a eşittir b")
elif a<b:
    print("a küçüktür b")


# a=int(input("enter a number :"))
# b=int(input("enter b number :"))
# if a>b:
#     print("a büyüktür b")
# elif a==b:
#     print("a eşittir b")
# elif a<b:
#     print("a küçüktür b")



# a=int(input("enter a number :"))
# if a>0:
#     print("sayı pozitif")
# elif a<0:
#     print("sayı negatif")
# else:
#     print("sayı sıfır")


# username="aliKara"
# password="12345"
# if(username=="aliKara"):
#     if(password=="12345"):
#         print("hoşgeldiniz")
#     else:
#         print("parola yanlış")
# else:
#     print("kullanıcı adı yanlış")


username1= input("enter username :")
password1= input("enter password :")
username="aliKara"
password="12345"
if(username==username1):
    if(password==password1):
        print("hoşgeldiniz")
    else:
        print("parola yanlış")
else:
    print("kullanıcı adı yanlış")


username="aliKara"
password="12345"
if(username=="aliKara" and password=="12345"):
    print("hoşgeldiniz")


if(username==username1 and password==password1):
    print("hoşgeldiniz")
else:
    print("kullanıcı adı veya parola yanlış")


