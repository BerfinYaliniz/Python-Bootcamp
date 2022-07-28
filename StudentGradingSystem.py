import pandas as pd
import csv
x = 0
indeksler = []
isimlist = []
soyadlist = []
okulnolist = []
notelist = []
gecmelist = []
harflist = []

while True:
    isim = input("adiniz: ")
    soyad = input("soyadiniz: ")
    no = input("okul numaraniz: ")
    note = int(input("yapay zeka notunuzu giriniz: "))
    x = x+1
    # 80-100 A
    # 70-79 B
    # 60-69 C
    # 50-59 D
    # 50 F
    
    def harfbelirleyici():
      if (note >= 80):
        print("A ile geçtiniz ")
        harflist.append('A')
        gecmelist.append('gecti')
      elif (note >= 70):
        print("B ile geçtiniz ")
        harflist.append('B')
        gecmelist.append('gecti')
      elif (note >= 60):
        print("C ile geçtiniz ")
        harflist.append('C')
        gecmelist.append('gecti')
      elif (note >= 50):
        print("harf notunuz D sartli basari.")
        harflist.append('D')
        gecmelist.append('sartli')
      else:
        print("F ile gectiniz kaldiniz")
        harflist.append('F')
        gecmelist.append('kaldi')
    
    harfbelirleyici()
    
    isimlist.append(isim)
    soyadlist.append(soyad)
    okulnolist.append(no)
    notelist.append(note)
    
    indeksler.append(x)
    
    karar = input("devam etmek istiyor musunuz ?(Y/N)")
    
   
    
    
    if karar == 'Y':
        print("devam ediliyor")
        continue
    elif karar == 'N':
        ogrdata = {
            'isim': isimlist,
            'soyad': soyadlist,
            'okulno': okulnolist,
            'not': notelist,
            'Harf': harflist,
            'gecme': gecmelist
        }
        
        print(isimlist)
        print(okulnolist)
        print(indeksler)
        
        
        ogrdata = pd.DataFrame(data=ogrdata,index=indeksler)
        ogrdata.to_excel('C:/Users/Emir/Desktop/test2.xlsx')
        break


 