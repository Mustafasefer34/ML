class Otomobil:
    klima="yok"
    teker_sayisi=4
    def __init__(self, marka, model, yil, kilometre):
        self.marka = marka
        self.model = model
        self.yil = yil
        self.kilometre = kilometre
        
    def km_degis(self,yeni_kilometre):#Kilometre güncelleme fonk
        self.kilometre=yeni_kilometre

# Sınıfın örneği bu şekilde oluşturulabilir:
audi_oto = Otomobil("Audi", "A3", 2017, 20000)
tofas_oto =Otomobil("Tofas", "Sahin", 2001, 300000)
# Sınıfın özelliklerine erişebilirsin:
print(audi_oto.marka," ",audi_oto.model," ",audi_oto.yil," ",audi_oto.kilometre," ",audi_oto.klima)   # Audi
print(tofas_oto.marka," ",tofas_oto.model," ",tofas_oto.yil," ",tofas_oto.kilometre," ",tofas_oto.klima)   # Audi

audi_oto.kilometre=audi_oto.kilometre + 3000
tofas_oto.kilometre=tofas_oto.kilometre + 15000

print("1 Yıl sonra\n")

print(audi_oto.marka," ",audi_oto.model," ",audi_oto.yil," ",audi_oto.kilometre," ",audi_oto.klima)   # Audi
print(tofas_oto.marka," ",tofas_oto.model," ",tofas_oto.yil," ",tofas_oto.kilometre," ",tofas_oto.klima)   # Audi
audi_oto.km_degis(40000)

print(audi_oto.marka," ",audi_oto.model," ",audi_oto.yil," ",audi_oto.kilometre," ",audi_oto.klima)   # Audi