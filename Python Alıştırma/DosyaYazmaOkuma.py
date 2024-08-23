import os 

#print(os.listdir())

#Metin dosyası oluşturacağız
ogrenci_dosya=os.open("ogrenciler.txt",os.O_RDWR|os.O_CREAT) #dosya varsa yaz yoksa oluştur

# text dosyasına öğrenci notu ve sınav notu ekleyelim
os.write(ogrenci_dosya, "FİNAL NOTLARI\n".encode())
os.write(ogrenci_dosya, "Mustafa Sefer Erdoğan, 82\n".encode())
os.write(ogrenci_dosya, "Ahmet Kalafatcı, 81\n".encode())
os.write(ogrenci_dosya, "Ufuk Yiğitaslan, 80\n".encode())
os.write(ogrenci_dosya, "Buğra Mithat Dönmez, 79\n".encode())
os.write(ogrenci_dosya, "Bedirhan Kömürcü, 78\n".encode())


os.close(ogrenci_dosya)


#Öğrenciler text dosyasında bulunan metni okuyacak


ogrenci_dosya=os.open("ogrenciler.txt",os.O_RDONLY)

dosya_uzunluk=os.stat(ogrenci_dosya).st_size
icerik=os.read(ogrenci_dosya, dosya_uzunluk)

print(icerik.decode())
os.close(ogrenci_dosya)