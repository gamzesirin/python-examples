# fonksiyonlar

def hello():
    print("Hello World")

hello()
# hello()
# hello()
# hello()
# hello()

# aldığı veya dışarı gönderdiği değerler yok

def hello(name):
    print("HELLO", name)

hello("GAMZE")

# aldığı değerler olabilir ama dışarıya gönderdiği değerler yok VOİD METHOD


def hello(name):
    return"Hello "+ name
a=hello("elif")
print(a)


def toplama(sayi1,sayi2):
    return sayi1+sayi2
    # toplam = sayi1+sayi2
    # return toplam

a=toplama(3,4)
print(a)



def carpma(sayi1,sayi2):
    return sayi1*sayi2
    # carpim = sayi1*sayi2
    # return carpim

a=carpma(3,4)
print(a)

def bolme(sayi1,sayi2):
    return sayi1/sayi2
    # bolum = sayi1/sayi2
    # return bolum

a=bolme(3,4)
print(a)

# MOD ALMA

def mod(sayi1,sayi2):
    return sayi1%sayi2
    # mod = sayi1%sayi2
    # return mod
x=mod(13,4)
print(x)



def yasHesaplama(dogum_yili):
    return 2019-dogum_yili

age_cinar=yasHesaplama(2017)
age_ada=yasHesaplama(2010)
age_ege=yasHesaplama(1999)
print(age_cinar,age_ada,age_ege)

def emeklilikHesaplama(dogum_yili,isim):
    yas=yasHesaplama(dogum_yili) #yasHesaplama fonksiyonu çağrıldı / fonksiyon içinde fonksiyon çağırıldı
    emeklilik=65-yas
    if emeklilik>0:
        print(f"{isim} , emekliliğinize {emeklilik} yıl kaldı")
    else:
        print(f"{isim} Zaten emeklisiniz")


emeklilikHesaplama(1990,"gamze")
emeklilikHesaplama(1950,"eda")
emeklilikHesaplama(1970,"erdem")


def erkanayaz(kelime , adet=5):
     for i in range(adet):
        print(kelime)


erkanayaz("merhaba")


def erkanayaz(kelime , adet):
    print(kelime * adet)


erkanayaz("merhaba \n",5)



#girilen iki sayı arasıda asal sayıları bulma => vize sınav soru tipi bu tarz soru gelecek

# def asalBul (sayi1,sayi2):
#     for sayi in range(sayi1,sayi2+1

#     ):
#         if (sayi>1):
#             for i in range(2,sayi):
#                 if (sayi%i==0):
#                     break
#             else:
#                 print(sayi)


# sayi1=int(input("1. sayıyı giriniz: "))
# sayi2=int(input("2. sayıyı giriniz: "))
# asalBul(sayi1,sayi2)


# SINAV SORUSU ÖRNEĞİ 2  =>


# def tambolenbul(sayi):
#     tam_bolenler=[]
#     for i in range(2,sayi):
#         if (sayi%i==0):
#             tam_bolenler.append(i)
#     return tam_bolenler

# sayi=int(input("sayı giriniz: "))
# print(tambolenbul(sayi))






# isimsiz tanımlanan fonksiyonlara lambda fonksiyonu denir


square = lambda x: x**2
print(square(4))


a=lambda a,b,c: a+b+c
print(a(3,4,5))



def math(n):
    return lambda x: x**n

square=math(2)
cube=math(3)
print(square(4))
print(cube(4))




numbers=[1,3,5,9]
def square(num):
    return num**2

result= list(map(square,numbers))
print(result)


# map ve filter  fonksiyonu önemli
# map fonksiyonu her bir elemanı alır ve işleme sokar
# filter fonksiyonu ise sadece true olanları alır


numbers=[1,3,5,9,10]
result = list (filter(lambda x: x%2==0,numbers))
print(result)


NUMBERS = [1,3,5,9,10]
CHECK_EVEN = lambda x: x%2==0
result = CHECK_EVEN(NUMBERS[2])
print(result)






X="global X"
def myfunc():
    X="local X"
    print(X)

myfunc()
print(X)





X="global X"
def myfunc():
    print(X)

myfunc()
print(X)



# sonraki isimle ilgili olan örnek ile ilgili ekran çıktısı sınav  sorussu olabilir

# KAPSAMA ALANALRINDAN BİR SORU  GELEBİLİR DEDİ



name ="GLOBAL STRİNG"

def greet():
    name="GAMZE"
    def hello():

        print("Hello "+name)


    hello()

greet()




def CtoF():
    celsius = eval(input("Enter the temperature in Celsius: "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")

CtoF()




def Ctof(celcius):
    return celcius*(9/5)+32

derece=int(input("derece giriniz: "))
print(Ctof(derece))


# banka hesap uygulma örneği