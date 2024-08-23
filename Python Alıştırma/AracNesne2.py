class Kara_araci():
    hiz=0
    def _init_(self, beygir_gucu, teker_sayisi):
        self.beygir_gucu=beygir_gucu
        self.teker_sayisi=teker_sayisi
        
    def hizi_ayarla(self,deger):
         self.hiz=deger
         
       

class Otobus(Kara_araci):
    def __init__(self, beygir_gucu, teker_sayisi, mevcut_yolcu_sayisi):
        Kara_araci._init_(self, beygir_gucu, teker_sayisi)
        
        self.mevcut_yolcu_sayisi = mevcut_yolcu_sayisi

# Sınıfın örneğini bu şekilde oluşturabilirsin:
otobus1 = Otobus(200, 8, 50)

# Sınıfın özelliklerine erişebilirsin:
#print(otobus1.beygir_gucu)  # 200
#print(otobus1.teker_sayisi)  # 50
#print(otobus1.mevcut_yolcu_sayisi) # 50

class Otomobil(Kara_araci):
    def __init__(self,beygir_gucu,teker_sayisi, koltuk_sayısı):
        Kara_araci._init_(self, beygir_gucu, teker_sayisi)
        self.koltuk_sayısı = koltuk_sayısı

# Otomobil sınıfından bir nesne oluştururken, parametreyi vermelisin:
otomobil1 = Otomobil(200,4,4)

# Bu parametreye erişebilirsin:
#print(otomobil1.koltuk_sayısı)  # 4
#print(otomobil1.beygir_gucu)  # 200
#print(otomobil1.teker_sayisi)  # 4


class bmw(Kara_araci):
    def __init__(self, beygir_gucu, teker_sayisi, sanruf_sayısı):
        Kara_araci._init_(self, beygir_gucu, teker_sayisi)
        self.sanruf_sayısı=sanruf_sayısı
        
bmw1=bmw(200,4,2)

print("BMW Arabasının beygir gücü: " + str(bmw1.beygir_gucu) + 
      " - BMW Arabasının teker sayısı: " + str(bmw1.teker_sayisi) +
      " - BMW Arabasının sunroof sayısı: " + str(bmw1.sanruf_sayısı))

bmw1.hizi_ayarla(70)

print(bmw1.hiz)






     