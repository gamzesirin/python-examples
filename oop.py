class Ucus():
    havayolu = "THY"
    def __init__(self, kalkis, varis, sure, yolcu_sayisi):
        self.kalkis = kalkis
        self.varis = varis
        self.sure = sure
        self.yolcu_sayisi = yolcu_sayisi

    def anons(self):#self yapısını kullanarak class içindeki özelliklere ulaşabiliyoruz. Şuan ki durumda self, Ucus sınıfından oluşturduğumuz nesneyi temsil ediyor.
        return f"{self.kalkis}-{self.varis} sefer sayılı uçuşumuz {self.sure} dakika sürecektir."
    def yolcu_artir(self):
        self.yolcu_sayisi += 1
    def yolcu_azalt(self):
        self.yolcu_sayisi -= 1
    def __str__(self):
        return f"{self.kalkis}-{self.varis} sefer sayılı uçuşumuz {self.sure} dakika sürecektir. Yolcu sayısı: {self.yolcu_sayisi}"
    def __len__(self):
        return self.sure
    def __del__(self):
        print("Uçuş silindi.")

ucus1=Ucus("İstanbul","Ankara",60,100) #Ucus sınıfından bir nesne oluşturdum.
print(ucus1.havayolu)
print(ucus1.varis)

#classa özgü özellikleer ile nesneye özgü özellikler arasında fark vardır.
#classa özgü özellikler classın tüm nesneleri için geçerlidir.
#nesneye özgü özellikler ise sadece o nesne için geçerlidir.


# dunder methodlar
# classla beraber otomatik gelen methodlardır.Üstüne yazma işlemi yapılabilir.



# __init__ : Nesne oluşturulduğunda çalışan methoddur.
# __str__ : Nesne print edildiğinde çalışan methoddur.
# __len__ : Nesne len fonksiyonuna sokulduğunda çalışan methoddur.
# __del__ : Nesne silindiğinde çalışan methoddur.
# __add__ : Nesneleri toplamak için kullanılır.
# __sub__ : Nesneleri çıkarmak için kullanılır.
# __mul__ : Nesneleri çarpmak için kullanılır.
# __truediv__ : Nesneleri bölmek için kullanılır.
# __mod__ : Nesnelerin modunu almak için kullanılır.
# __pow__ : Nesnelerin üssünü almak için kullanılır.
# __eq__ : Nesnelerin eşit olup olmadığını kontrol eder.
# __ne__ : Nesnelerin eşit olmadığını kontrol eder.
# __lt__ : Nesnelerin küçük olup olmadığını kontrol eder.
# __gt__ : Nesnelerin büyük olup olmadığını kontrol eder.
# __le__ : Nesnelerin küçük veya eşit olup olmadığını kontrol eder.
# __ge__ : Nesnelerin büyük veya eşit olup olmadığını kontrol eder.
# __contains__ : Nesnenin içinde bir elemanın olup olmadığını kontrol eder.
# __call__ : Nesne fonksiyon gibi çağrılabilir.
# __getitem__ : Nesnenin elemanlarına erişmek için kullanılır.
# __setitem__ : Nesnenin elemanlarına erişmek için kullanılır.
# __delitem__ : Nesnenin elemanlarını silmek için kullanılır.
# __iter__ : Nesneyi iterable yapar.
# __next__ : Nesneyi iterable yapar.
# __reversed__ : Nesneyi ters çevirir.
# __enter__ : Nesne bir bloğa girdiğinde çalışır.
# __exit__ : Nesne bir bloktan çıktığında çalışır.
# __copy__ : Nesneyi kopyalar.
# __deepcopy__ : Nesneyi derinlemesine kopyalar.
# __hash__ : Nesnenin hash değerini döner.
# __bool__ : Nesne bool değerini döner.
# __bytes__ : Nesneyi byte olarak döner.
# __format__ : Nesneyi biçimlendirir.
# __index__ : Nesneyi indexler.
# __int__ : Nesneyi integer yapar.
# __float__ : Nesneyi float yapar.
# __str__ : Nesneyi string yapar.
# __bytes__ : Nesneyi byte yapar.
# __bool__ : Nesneyi bool yapar.
# __complex__ : Nesneyi complex yapar.
# __round__ : Nesneyi yuvarlar.
# __trunc__ : Nesneyi tam sayı yapar.
# __floor__ : Nesneyi alta yuvarlar.
# __ceil__ : Nesneyi üste yuvarlar.
# __abs__ : Nesnenin mutlak değerini alır.
# __neg__ : Nesnenin negatifini alır.
# __dir__ : Nesnenin özelliklerini döner. **
#  __repr__ : Nesnenin temsilini döner.Bellekte objenin yerini gösterir. **
# __setattr__ : Nesneye yeni bir özellik ekler.