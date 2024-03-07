# stringler

name="gamze"
surname="şirin"
age=36
grreting="my name is "+name+" "+surname+" and  \n I am "+str(age)+" years old" # \n alt satıra geçirir
print(grreting)

# format fonksiyonu
name="gamze"
surname="şirin"
age=20
print("my name is {} {} and I am {} years old".format(name,surname,age)) # format fonksiyonu ile değişkenleri yerleştirir 

# format fonksiyonu ile sıralı yerleştirme
name="gamze"
surname="şirin"
age=20
print("my name is {1} {0} and I am {2} years old".format(name,surname,age)) # format fonksiyonu ile değişkenleri sıralı yerleştirir

# format fonksiyonu ile isimlendirilmiş yerleştirme
name="gamze"
surname="şirin"
age=20
print("my name is {n} {s} and I am {a} years old".format(n=name,s=surname,a=age)) # format fonksiyonu ile değişkenleri isimlendirilmiş yerleştirir
print('My name is {s} {n}'.format(n=name, s=surname)) # değişkenleri isimlendirilmiş yerleştirme


print("My name is {} {} and I'm {} years old.".format(name, surname, age))

# formatı bir list gibi düşünebiliriz

print("My name is {0} {0} and I'm {0} years old.".format(name))


sehirler = ['ankara', 'istanbul', 'izmir']
plakalar = [6, 34, 35]
print(plakalar[sehirler.index('istanbul')])
print(sehirler.index('istanbul'))

#f-string ile formatlama

print(f"My name is {name} {surname} and I'm {age} years old.")

grreting="my name is "+name+" "+surname+" and  \n I am "+str(age)+" years old." # \n alt satıra geçirir
result1=grreting[0] # stringin ilk karakterini alır
result2=grreting[17] # stringin 17. karakterini alır
result3=grreting[-1] # stringin son karakterini alır
result4=grreting[-2] # stringin son karakterini alır

print(result1)
print(result2)
print(result3)
print(result4)

#len fonksiyonu
result=len(grreting) # stringin uzunluğunu alır karakter sayısı
print(result)


result=grreting[len(grreting)-1] # stringin son karakterini alır
print(result)

# string slicing
result=grreting[2:16] # 2. karakterden başla 5. karaktere kadar al
print(result)

result=grreting[:10] # baştan başla 10. karaktere kadar al
print(result)

result=grreting[5:] # 5. karakterden başla sona kadar al
print(result)

result=grreting[0:10:1] # 0. karakterden başla 10. karaktere kadar 1 karakter atlayarak al
print(result)

result=grreting[0:10:2] # 0. karakterden başla 10. karaktere kadar 2 karakter atlayarak al
print(result)

result=grreting[::-1] # stringi tersten yazdır
print(result)


# result=grreting[::] # baştan başla sona kadar al
# print(result)

# result=grreting[::2] # baştan başla sona kadar 2 karakter atlayarak al
# print(result)


website = "http://www.mehmetakif.edu.tr" #karakter dizisi
course = "Python Dersi: Baştan Sona Python Programlama Dersi (14 Hafta)" #karakter dizisi
print(website)
print(course)

result1=len(website) #karakter dizisinde kaç karaker olduğunu verir
print(result1)

result2=len(course) #karakter dizisinde kaç karaker olduğunu verir
print(result2)

print("course karakter dizisinde {} adet karakter vardır".format(result2))
print("website karakter dizisinde {} adet karakter vardır".format(len(website)))

length1 = len(course)
length2 = len(website)
print("course karakter dizisinde {} adet karakter vardır".format(len(course)))
print("course karakter dizisinde {} adet karakter vardır".format(length1))

result= website[7:10]
print(result)


result=website[-2:]
print(result)
result1=website[26:28]
print(result1)
result2=website[len(website)-2:len(website)]
print(result2)

result=course[0:15]
print(result)
result=course[:15]
print(result)
result=course[-15:]
print(result)

result = course[::-1]
print(result)

name="gamze"
surname="şirin"
age=20
job="yazılım mühendisi"
result=print(f"benim adım {name} {surname}, {age} yaşındayım ve mesleğim {job}")
result=print("benim adım {} {}, {} yaşındayım ve mesleğim {}".format(name,surname,age,job))
result=print("benim adım {n} {s}, {a} yaşındayım ve mesleğim {j}".format(n=name,s=surname,a=age,j=job))
result=print("benim adım {0} {1}, {2} yaşındayım ve mesleğim {3}".format(name,surname,age,job))
result1 = "Benim adim "+ name+ " " + surname+ ", Yaşim "+ str(age) + " ve mesleğim "+ job

x="abc"
result=print(x*3) # stringi 3 kere yazdırır

# split metodu

message="Hello there. My name is Gamze Şirin. I am 20 years old."
result=message.split() # stringi boşluklardan ayırır ve listeye çevirir
print(result)
print(result[0])
print(message[0])

result=message.split('.') # stringi noktalardan ayırır ve listeye çevirir
print(result)

result=message.split(' ') # stringi boşluklardan ayırır ve listeye çevirir
print(result)

result=message.split('e') # stringi e harfinden ayırır ve listeye çevirir
print(result)

result=message.upper() # stringi büyük harfe çevirir
print(result)

result=message.lower() # stringi küçük harfe çevirir
print(result)

result=message.title() # stringin her kelimesinin ilk harfini büyük yapar
print(result)

result=message.capitalize() # stringin sadece ilk harfini büyük yapar
print(result)

#strip metodu

username="             gamze               "
result=username.strip() # stringin başındaki ve sonundaki boşlukları siler
print(result)
print("my name is {}".format(result))



username="---!!!,,,;;;:::gamze---!!!,,,;;;:::"
result=username.strip('-!;,:') # stringin başındaki ve sonundaki -!;,: karakterlerini siler
print(result)
print("my name is {}".format(result))


#replace metodu

message="Hello there. My name is Gamze Şirin. I am 20 years old."
result=message.replace('G','g') # stringin içindeki G harfini g ile değiştirir
print(result)

message="Hello there. My name is Gamze Şirin. I am 20 years old."
result=message.replace('Gamze','Büşra') # stringin içindeki G harfini g ile değiştirir
print(result)

#find metodu => bulamazsa exception vermez -1 döner
message="Hello there. My name is Gamze Şirin. I am 20 years old."
result=message.find('Gamze') # stringin içindeki Gamze kelimesinin başladığı indexi verir
print(result)

result=message.find('Gamzem') # stringin içindeki Gamze kelimesinin başladığı indexi verir
print(result)

txt="Hello, welcome to my world."
x = txt.find("welcome",0,20) # 0. indexden 5. indexe kadar arar
print(x)


#index metodu => bulamazsa exception verir

message="Hello there. My name is Gamze Şirin. I am 20 years old."
result=message.index('Gamze') # stringin içindeki Gamze kelimesinin başladığı indexi verir
print(result)

# result=message.index('Gamzem') # stringin içindeki Gamze kelimesinin başladığı indexi verir
# print(result)

txt="Hello, welcome to my world."
x = txt.index("welcome",0,20) # 0. indexden 5. indexe kadar arar
print(x)




website = "http://www.mehmetakif.edu.tr"
course = "Python Dersi: Baştan Sona Python Programlama Dersi (14 Hafta)"


deneme="    hello world    "
result=deneme.strip() # stringin başındaki ve sonundaki boşlukları siler
print(result)
result=deneme.lstrip() # stringin başındaki boşlukları siler
print(result)
result=deneme.rstrip() # stringin sonundaki boşlukları siler
print(result)



result = " Hello World1 ".strip()     # baş ve sondaki boşluk karakterleri silinir.
print(result)
result = " Hello World1 ".lstrip()    # baştaki boşluk karakterleri silinir.
print(result)

result = " Hello World1 ".rstrip()    # sondaki boşluk karakterleri silinir.
print(result)

result =   website.lstrip("/:pth")   # baştan itibaren '/:pth' karakterine kadar silinir.
print(result)



# 2-	 “http://www.mehmetakif.edu.tr”  içindeki mehmetakif bilgisi haricindeki her karakteri silin.

result = "http://www.mehmetakif.edu.tr".strip('/:pthw.edu.tr')
print(result)


result=course.upper() # stringi büyük harfe çevirir
print(result)
result=course.lower() # stringi küçük harfe çevirir
print(result)
result=course.title() # stringin her kelimesinin ilk harfini büyük yapar
print(result)
result=course.capitalize() # stringin sadece ilk harfini büyük yapar
print(result)

#COUNT METODU

result=website.count('a') # stringin içindeki a harfinin kaç tane olduğunu verir
print(result)

result=website.count('www') # stringin içindeki www kelimesinin kaç tane olduğunu verir
print(result)

result=website.count('www',0,10) # 0. indexden 10. indexe kadar stringin içindeki www kelimesinin kaç tane olduğunu verir
print(result)

#startswith metodu

result=website.startswith('http') # string http ile başlıyorsa True döner
print(result)

result=website.startswith('www') # string www ile başlıyorsa True döner
print(result)


#endswith metodu

result=website.endswith('tr') # string tr ile bitiyorsa True döner
print(result)

result=website.endswith('com') # string com ile bitiyorsa True döner
print(result)


website = "http://www.mehmetakif.edu.tr"
course = "Python Dersi: Baştan Sona Python Programlama Dersi (14 Hafta)"



# result=website.find("edu") # stringin içindeki edu kelimesinin başladığı indexi verir
# print(result)

# result=website.index("edu") # stringin içindeki edu kelimesinin başladığı indexi verir
# print(result)

# result=website.index("edu",0,10) # 0. indexden 10. indexe kadar stringin içindeki edu kelimesinin başladığı indexi verir
# print(result)


# result=website.rindex("edu") 
# print(result)

# result=website.rfind("edu")
# print(result)

# result=course.rfind("Python")
# print(result)

# result=course.rindex("Python")
# print(result)


result=course.isalpha() # string sadece alfabetik karakterlerden oluşuyorsa True döner
print(result)

course = "Python Dersi: Baştan Sona Python Programlama Dersi (14 Hafta)"
result = course.isalpha()   # tüm karakterler alfabetik mi diye sorar ve False gelir.
result = 'Hello'.isalpha()  # tüm karakterler alfabetik olduğundan True gelir.
result = course.isdigit()   # tüm karakterler rakam mı diye sorar ve False gelir.
result = '123'.isdigit()    # tüm karakterler rakam mı diye sorar ve True gelir.


# center metodu

result="contents".center(50,'*') # stringi 50 karakterlik alanda * karakteri ile ortalar
print(result)

result="contents".ljust(50,'*') # stringi 50 karakterlik alanda * karakteri ile sola yaslar
print(result)

result="contents".rjust(50,'*') # stringi 50 karakterlik alanda * karakteri ile sağa yaslar
print(result)

result=course.replace(' ','-') # stringin içindeki boşlukları - ile değiştirir
print(result)

result="hello world"
result2=result.replace('world','there') # stringin içindeki world kelimesini there ile değiştirir
print(result2)

result3=course.split() # stringi boşluklardan ayırır ve listeye çevirir
print(result3)




'''
ödev =>

istatistiksel özellikleri bulan program yazınız
- metindeki paragraf sayısı
- metindeki cümle sayısı
- metindeki kelime sayısı
- metindeki karakter sayısı
'''

metin =input("bir metin giriniz : ")

kelimesayisi=metin.count(' ') # stringin içindeki boşluğun kaç tane olduğunu verir
print("metinde" ,kelimesayisi+1 ,"tane kelime vardır")
cümlesayisi=metin.count('.')
print("metinde" ,cümlesayisi ,"tane cümle vardır")
