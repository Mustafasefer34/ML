
#Regex Kullanım


import re

cumle = "Girintilere dayalı basit söz dizimi, dilin öğrenilmesini ve akılda kalmasını kolaylaştırır. Bu da ona söz diziminin ayrıntıları ile vakit yitirmeden programlama yapılmaya başlanabilen bir dil olma özelliği kazandırır."

patern = "dil"
count=0


#sonuc=re.search(patern, cumle) #ilk bulduğu yerde durur search


#print(sonuc.start()," ",sonuc.end())

for bulunan in re.finditer(patern, cumle):
  #  print(bulunan.span(),bulunan.group())
    count=count+1


#print(count)
    

#Desen Eşleştirme

cumle2="Merhaba benim cep numaram 532-1112233 beni öğleden sonra arayabilirsiniz"

#Rakamlar için  \d
#harfler için \r
#boşluk için \s
#...

patern2="\d\d\d-\d\d\d\d\d\d\d"
print(re.search(patern2, cumle2))
