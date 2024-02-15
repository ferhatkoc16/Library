def menu_goster():
    print("\n** MENU **")
    print("1. Kitap Sırası")
    print("2. Kitap Ekleme")
    print("3. Kitap Silme")
    print("4. Degisiklik Yap")
    print("5. Çıkış")

def kitap_sirasi_goster():
    try:
        with open("book.txt", "r") as dosya:
            print("\n-- Kitap Sırası --")
            kitaplar = dosya.readlines()
            if not kitaplar:
                print("Henüz bir kitap eklenmemiş.")
            else:
                for kitap in kitaplar:
                    print(kitap.strip())
    except FileNotFoundError:
        print("Kitap bulunamadı! Lütfen bir kitap ekleyin.")

def kitap_ekle():
    kitap_adi = input("Eklemek istediğiniz kitabın adını girin: ")
    with open("book.txt", "a+") as dosya:
        kitaplar = dosya.readlines()
        for i in range(0, len(kitaplar), 5): 
            if kitaplar[i].strip() == f"Kitap Adı: {kitap_adi}":
                print(f"{kitap_adi} adlı kitap zaten mevcut!")
                return

    yazar_adi = input("Yazarın adını girin: ")
    while True:
        try:
            sayfa_sayisi = int(input("Kitabın sayfa sayısını girin: "))
            break
        except ValueError:
            print("Lütfen sayi degeri giriniz !")
    while True:
        try:
            basim_tarihi = int(input("Basım tarihini girin: "))
            break
        except ValueError:
            print("Lütfen sayi degeri giriniz !")
                        
    
    
    

    with open("book.txt", "a+") as dosya:
        dosya.write(f"Kitap Adı: {kitap_adi}\n")
        dosya.write(f"Yazar Adı: {yazar_adi}\n")
        dosya.write(f"Basım Tarihi: {basim_tarihi}\n")
        dosya.write(f"Sayfa Sayısı: {sayfa_sayisi}\n")
        dosya.write("-" * 20 + "\n")

    print(f"{kitap_adi} başarıyla eklendi.")


def kitap_sil():
    silinecek_kitap = input("Silmek istediğiniz kitabın adını girin: ")
    try:
        with open("book.txt", "r") as dosya:
            kitaplar = dosya.readlines()

        with open("book.txt", "w") as dosya:
            silindi_mi = False
            i = 0
            while i < len(kitaplar):
                if kitaplar[i].strip() == f"Kitap Adı: {silinecek_kitap}":
                    print(f"{silinecek_kitap} başarıyla silindi.")
                    silindi_mi = True
                    i += 5  
                else:
                    
                    for j in range(5):
                        if i + j < len(kitaplar):
                            dosya.write(kitaplar[i + j])
                    i += 5  

            
            if not silindi_mi:
                print(f"{silinecek_kitap} adlı kitap bulunamadı.")
    except FileNotFoundError:
        print("Dosya bulunamadı.")


def degisiklik_yap():
    print("\nHangi bilgiyi değiştirmek istersiniz?")
    print("1. Kitap Adı")
    print("2. Yazar Adı")
    print("3. Basım Tarihi")
    print("4. Sayfa Sayısı")
    secim = input("Numaralandırılmış menülerden istediğiniz menüye gidin: ")

    if secim == '1':
        kitap_adi_degistir()
    elif secim == '2':
        yazar_adi_degistir()
    elif secim == '3':
        basim_tarihi_degistir()
    elif secim == '4':
        sayfa_sayisi_degistir()
    else:
        print("Geçersiz seçenek, lütfen tekrar deneyin.")

def kitap_adi_degistir():
    eski_kitap_adi = input("Değiştirmek istediğiniz kitabın eski adını girin: ")
    yeni_kitap_adi = input("Yeni kitap adını girin: ")
    
    try:
        with open("book.txt", "r") as dosya:
            kitaplar = dosya.readlines()

        with open("book.txt", "w") as dosya:
            degistirildi_mi = False
            for i in range(0, len(kitaplar), 5):
                if kitaplar[i].strip()== f"Kitap Adı: {eski_kitap_adi}":
                    kitaplar[i] = f"Kitap Adı: {yeni_kitap_adi}\n"
                    degistirildi_mi = True
                for j in range(5):
                    dosya.write(kitaplar[i + j])

            if degistirildi_mi:
                print(f"{eski_kitap_adi} başarıyla {yeni_kitap_adi} ile değiştirildi.")
            else:
                print(f"{eski_kitap_adi} adlı kitap bulunamadı.")
    except FileNotFoundError:
        print("Dosya bulunamadı.")


def yazar_adi_degistir():
    eski_yazar_adi = input("Değiştirmek istediğiniz kitabın eski yazar adını girin: ")
    yeni_yazar_adi = input("Yeni yazar adını girin: ")
    
    try:
        with open("book.txt", "r") as dosya:
            satirlar = dosya.readlines()

        with open("book.txt", "w") as dosya:
            degistirildi_mi = False
            for satir in satirlar:
                if satir.startswith("Yazar Adı:"):
                    yazar_adi = satir.split(":")[1].strip()
                    if yazar_adi == eski_yazar_adi:
                        satir = f"Yazar Adı: {yeni_yazar_adi}\n"
                        degistirildi_mi = True
                dosya.write(satir)

            if degistirildi_mi:
                print(f"{eski_yazar_adi} başarıyla {yeni_yazar_adi} ile değiştirildi.")
            else:
                print(f"{eski_yazar_adi} adlı yazar bulunamadı.")
    except FileNotFoundError:
        print("Dosya bulunamadı.")

def basim_tarihi_degistir():
    while True:
        try:
            eski_basim_tarihi = input("Değiştirmek istediğiniz kitabın eski basım tarihini girin: ")

            if not eski_basim_tarihi.isdigit():
                raise ValueError("Hata: Basım tarihi sadece sayısal bir değer olmalıdır.")

            yeni_basim_tarihi = input("Yeni basım tarihini girin: ")

            if not yeni_basim_tarihi.isdigit():
                raise ValueError("Hata: Yeni basım tarihi sadece sayısal bir değer olmalıdır.")

            break  

        except ValueError as err:
            print(err)  

    try:
        with open("book.txt", "r") as dosya:
            satirlar = dosya.readlines()

        with open("book.txt", "w") as dosya:
            degistirildi_mi = False
            for satir in satirlar:
                if satir.startswith("Basım Tarihi:"):
                    basim_tarihi = satir.split(":")[1].strip()
                    if basim_tarihi == eski_basim_tarihi:
                        satir = f"Basım Tarihi: {yeni_basim_tarihi}\n"
                        degistirildi_mi = True
                dosya.write(satir)

            if degistirildi_mi:
                print(f"{eski_basim_tarihi} başarıyla {yeni_basim_tarihi} ile değiştirildi.")
            else:
                print(f"{eski_basim_tarihi} adlı basım tarihi bulunamadı.")
    except FileNotFoundError:
        print("Dosya bulunamadı.")

def sayfa_sayisi_degistir():
    while True:  
        try:
            eski_sayfa_sayisi = input("Değiştirmek istediğiniz kitabın eski sayfa sayısını girin: ")

            if not eski_sayfa_sayisi.isdigit():
                raise ValueError("Hata: Sayfa sayısı sadece sayısal bir değer olmalıdır.")

            yeni_sayfa_sayisi = input("Yeni sayfa sayısını girin: ")

            if not yeni_sayfa_sayisi.isdigit():
                raise ValueError("Hata: Yeni sayfa sayısı sadece sayısal bir değer olmalıdır.")

            break  # Doğru formatta giriş yapıldığında döngüden çık

        except ValueError as err:
            print(err)  

    try:
        with open("book.txt", "r") as dosya:
            satirlar = dosya.readlines()

        with open("book.txt", "w") as dosya:
            degistirildi_mi = False
            for satir in satirlar:
                if satir.startswith("Sayfa Sayısı:"):
                    sayfa_sayisi = satir.split(":")[1].strip()
                    if sayfa_sayisi == eski_sayfa_sayisi:
                        satir = f"Sayfa Sayısı: {yeni_sayfa_sayisi}\n"
                        degistirildi_mi = True
                dosya.write(satir)

            if degistirildi_mi:
                print(f"{eski_sayfa_sayisi} başarıyla {yeni_sayfa_sayisi} ile değiştirildi.")
            else:
                print(f"{eski_sayfa_sayisi} adlı sayfa sayısı bulunamadı.")
    except FileNotFoundError:
        print("Dosya bulunamadı.")


def main():
    while True:
        menu_goster()
        secim = input("Numaralandırılmış menülerden istediğiniz menüye gidin: ")

        if secim == '1':
            kitap_sirasi_goster()
        elif secim == '2':
            kitap_ekle()
        elif secim == '3':
            kitap_sil()
        elif secim == '4':
            degisiklik_yap()
        elif secim == '5':
            print("Program sonlandırılıyor...")
            break
        else:
            print("Geçersiz seçenek, lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()

