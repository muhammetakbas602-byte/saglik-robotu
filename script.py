print("""
Sağlık Robotuna Hoşgeldiniz!
    
      -1 Ateşlenme
      -2 Boğaz Ağrısı
      -3 Soğuk Algınlığı
      -4 Burun Akıntısı
      -5 Mide Bulantısı
      -6 Alerji
      -7 Baş Dönmesi
      -8 Vitamin Eksikliği
      -9 Uykusuzluk
      -10 Diyabet
      -11 İshal
      -12 Kabız
      -13 Tansiyon
      -14 Göz Yanması
      -15 Burun Tıkanıklığı
      -16 Karaciğer Yağlanması
      -17 Nabız
      -18 Mide Yanması  
      -19 Kolestrol
      -20 Demir Eksikliği
""")
secim = input("Hastalığı Seçiniz: ").lower()

if secim == "ateşlenme":
    print("Sizin İçin Gerekli Olan İlaç Calpol")

elif secim == "boğaz ağrısı":
    print("Sizin İçin Gerekli Olan İlaç Majezik")

elif secim == "soğuk algınlığı":
    print("Sizin İçin Gerekli Olan İlaç İburamin Zero")

elif secim == "burun akıntısı":
    print("Size Gerekli Olan İlaç Sterimar Stop & Protect")

elif secim == "mide bulantısı":
    print("Size Gerekli Olan İlaç Buscovan ve Granisetron")

elif secim == "alerji":
    print("Size Gerekli Olan İlaç Zytrec")

elif secim == "baş dönmesi":
    print("Size Gerekli Olan İlaç Dramamine")   

elif secim == "vitamin eksikliği":
    print("Size Gerekli Olan İlaç Feramat")

elif secim == "uykusuzluk":
    print("Size Gerekli Olan İlaç Ambien")

elif secim == "diyabet":
    print("Size Gerekli Olan İlaç Glifor")

elif secim == "ishal":
    print("Size Gerekli Olan İlaç Raxerin")

elif secim == "kabız":
    print("Size Gerekli Olan İlaç DulceSoft")

elif secim == "tansiyon":
    print("Size Gerekli Olan İlaç Benipin")

elif secim == "göz yanması":
    print("Size Gerekli Olan İlaç Tobrex")  

elif secim == "burun tıkanıklığı":
    print("Size Gerekli Olan İlaç Sinomarin")

elif secim == "karaciğer yağlanması":
    print("Size Gerekli Olan İlaç Nutraxin")

elif secim == "nabız":
    print("Size Gerekli Olan İlaç Atropin")            

elif secim == "mide yanması":
    print("Size Gerekli Olan İlaç Acidpass")

elif secim == "kolestrol":
    print("Size Gerekli Olan İlaç Rosuvastatin")

elif secim == "demir eksikliği":
    print("Size Gerekli Olan İlaç Feritin") 

else:
    print("Hata! İlaç bulunuamadı.")   

input("Çıkmak İçin Enter'a basın...")    
