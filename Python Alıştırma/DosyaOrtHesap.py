import os

ogrenci_dosya=os.open("ogrenciler.txt",os.O_RDWR|os.O_CREAT) 

os.write(ogrenci_dosya, "Mustafa Sefer Erdoğan, 82\n".encode())
os.write(ogrenci_dosya, "Ahmet Kalafatcı, 81\n".encode())
os.write(ogrenci_dosya, "Ufuk Yiğitaslan, 80\n".encode())
os.write(ogrenci_dosya, "Buğra Mithat Dönmez, 79\n".encode())
os.write(ogrenci_dosya, "Bedirhan Kömürcü, 78\n".encode())

ogrenci_dosya=os.open("ogrenciler.txt",os.O_RDONLY)
dosya_uzunluk=os.stat(ogrenci_dosya).st_size
icerik=os.read(ogrenci_dosya,dosya_uzunluk)



ogrenciler=icerik.decode()
ogrenciler_list=ogrenciler.split("\n")

#print(ogrenciler_list)

ogrenci_sayisi = len(ogrenciler_list)-1
#print(ogrenci_sayisi)

index=0
toplam_notlar=0
while (index < ogrenci_sayisi):
   # print(ogrenciler_list[index])
   ogrenci_notu=ogrenciler_list[index].split(",") 
   toplam_notlar=toplam_notlar+ int(ogrenci_notu[1])
   
   index=index+1
   
    
print("Öğrencilerin sınav notlarının ortalaması: ",toplam_notlar/ogrenci_sayisi)





os.close(ogrenci_dosya)
