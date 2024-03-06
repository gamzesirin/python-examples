deger=5
ad="gamze"
print(ad)
print(deger)
a=5
b=3
print(a+b)
# a=5
# b="3"
# print(a+b) # tip hatası veriyor bu işlem yapılamaz
# elif ="güzel" # kullanılamaz
# as="kare" # kullanılamaz

import keyword
print(keyword.kwlist) # değişken adı olarak kullanılmaması gereken kelimelerin listesi pythonın içindeki anahtar kelimler // del type diyerek o tip silinir ve onu kullanabilirsin

x="Merhaba Yazılım Mühendisliği"
print(type(x)) # x değişkeninin tipini verir

# kullanıcı adı ="gamze"  bu yapılamaz arada boşluk olamaz
kullanıcı_adı="gamze şirin"
kullanıcıAdı="gamze şirin"

a=4
b=4
print(a)
print(b)

a=b=4
print(a)
print(b)
#örnek1 => yol masrafı hesaplama uygulaması

#yol1
print(22*(1.5+1.4))

#yol2

günSayisi=22
gidisUcret=1.5
gelisUcreti=1.4
yolMasrafi=günSayisi*(gidisUcret+gelisUcreti)
print(yolMasrafi)

#soru : 1 yılda nasıl hesaplarız
ocak=mart=mayis=temmuz=agustos=ekim=aralik=31
nisan=haziran=eylül=kasim=30
subat=28
print(mayis)

gidisUcret=1.5
gelisUcreti=1.4
yolMasrafi=mayis*(gidisUcret+gelisUcreti)
print(yolMasrafi)


osman="proje genel müdürü"
mehmet="yazılımcı"
print(osman)
print(mehmet)

osman,mehmet=mehmet,osman
print(osman)
print(mehmet)

# floatta nokta kullanılıyor 3.17 gibi

'''paragraf şeklindeki yorum
 satırları için 3 tırnak kullnılır'''


# list = olacaksa köşeli parantez olacak , her türlü veri tipi koyulur , değiştirilebilir ,sabit bir yer ayırır
veri=["gamze","sedat"]
print(veri)

veri1=["gamze","sedat",1234,12.6]
print(veri1)

# range = dizi oluşturmaya yardımcı olur

for i in range(10):
  print(i)

# tuple = parantez olacak

veri =("veri tabanı","algoritma","web programlama")
print(veri)

# küme = süslü parantez ile tanımlanır sıralıdır sıra değişmez kümede sıralama değişir rastgele bellekte yer tutar sabit bir yer ayırmaz

veri1={"audio","toyota","fiat"}
print(veri1)

# set veri tipi => küme ve list için kullanılabilir set sıralama yapar  //değişirilebilir veri kümeleridir

veri=[6,2,3,4]
print(veri)
sirliveri=set(veri)
print(sirliveri)

# sıralı veri içinde 2 yi arıyorum sonuç true ya da false
test=8 in sirliveri
print(test)

# küme içinden silme için remove kullanılır eleman siler index silmez
sirliveri.remove(3) # 3 ü siler

# frozen set veri tipi => //değişirilemez veri kümeleridir

veri =frozenset(["A",1,2,3,4,5])
print(veri)
# veri.remove("A") bu mümkün değil frozensette remove komutu yok

# bytes veri tipi => 

# unicode nedir ?

# 4 bit niple / 8 bit byte

# dictionary veri tipi sözlük oluşturulur normal parantez kullanılır key-value olarak yazılır !!!!!
ogr=dict(adi="gamze",soyadi="şirin",bolumu="Yazılım")
print(ogr) 

#  bu işaret // bölme işlemindeki bölümü verir      ** bu işaret pow ile aynı yani üs alır         divmod işlemi bölme işlemimdem bölüm , kalanı verir tuple olarak   pow(x,y,z)=> x üssü y olur sonucun z ile modu nedir


# kullanıcıdan giriş almak için input kullanılır input a girilen string olur

a=int(input("sayıyı giriniz : "))
toplam=0
for i in range(1,a+1):
   toplam+=i
print(toplam)


# bu soruya bak
a = int(input("sayıyı giriniz: "))
toplam = 0
for i in range(1, a+1):
    if i % 2 == 0: 
        toplam += i
print(toplam)  