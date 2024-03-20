#Girilen metni boşluk ve sayılardan ayıran metod

def BSayir(metin):
    yeniMetin=''    
    for i in metin:
        if not (i.isspace() or i.isdigit()):
            yeniMetin+=i
    return yeniMetin  


#Kendisine gönderilen karakterin bir harf olup 
#olmadığını bulan metod

def HarfMi(deger):
    asciDeger=ord(deger)
    if((asciDeger>=65 and asciDeger <=90) 
    or (asciDeger>=97 and asciDeger<=122)):
        return True
    else:
        return False

#Kendisine gelen harfi (büyükse) küçük harfe çeviren 
#(küçükse) büyük harfe çeviren bir metod

def Donusum(deger):
    asciDeger=ord(deger)
    if(asciDeger>=65 and asciDeger <=90):
        return deger.lower()
    elif (asciDeger>=97 and asciDeger<=122):
        return deger.upper()
    else:
        return deger
    
        
# Kendisine gönderilen metinde harflerin 
#kullanım sıklığını (yüzdelik oranını) bulan metod

def frekansYuzdelik(metin):
    sozluk={}
    harfler=''
    for j in metin:
        if j.isalpha():
            harfler+=j
    
    for i in harfler.lower():
        if i not in sozluk.keys():
            sozluk[i]=+1
        else:
            sozluk[i]+=1
    for x,y in sozluk.items():
         print(x,": number of using: ",y," using rate ",(y/len(metin)*100),sep="")        
    
#Girilen metindeki toplam kelime sayısının karakter
#sayısına oranını bulan metod


def kelimeFrekans(metin):
    kelimeler=metin.split(' ')
    kelimeSayi=len(kelimeler)
   
    harfSayi=len(metin)
    print((kelimeSayi/harfSayi)*100)

#bilgilendirme    
def bilgi():
    print('Alper','Kosa','211220007',
          '''Merhaba Dünya! 
Degişmeyen tek şey degişimin kendisidir bu nedenle her yeni gün degişim için bir fırsattır.
          ''',sep=("\n"))
          
    


    

