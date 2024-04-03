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