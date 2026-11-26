arabalar = {
    "Yaris": 30,
    "Golf": 45,
    "Passat": 60,
    "Tucson": 80
}
def fiyat_hesapla(secilen_araba, kiralama_gunu):
    gunluk_fiyat = arabalar[secilen_araba]
    toplam = gunluk_fiyat * kiralama_gunu
    if kiralama_gunu > 7:
        toplam *= 0.85
    return toplam

secilen_arac = ""
gun_sayisi = 0
soru = input("Hoşgeldiniz... \nAraç listesini gormek ister misiniz? (e/h): ").lower()

if soru == "e":
    print("\n--- Araç Listemiz ---")
    for arac, fiyat in arabalar.items():
        print(f"{arac}: {fiyat}€")
    while True:
        secim = input("\nLütfen istediğiniz arabayı seçiniz (Çıkış için 0): ").title()
        if secim == "0":
            break
        if secim in arabalar:
            secilen_arac = secim
            print(f"-> {secim} elimizde mevcut ve sizin için hazırlanacak.")
            while True:
                gun = input("Lütfen kaç gün kiralamak istediğinizi belirtiniz: ")
                if gun.isdigit() and int(gun) > 0:
                    gun_sayisi = int(gun)
                    break
                else:
                    print("Hata! Lütfen geçerli bir gün sayısı giriniz.")
            break
        else:
            print("Maalesef şuan kullanılabilir bir araç değildir. Tekrar deneyin.")
    if secilen_arac != "":
        print(f"\nSeçilen Araç: {secilen_arac} | Kiralanan Gün: {gun_sayisi}")
        ucret = fiyat_hesapla(secilen_arac, gun_sayisi)
        print(f"Toplam ücretiniz: {ucret:.2f}€")
    else:
        print("\nHerhangi bir araç seçilmedi.")
else:
    print("Bir kiralama işlemi yapmadınız. İyi günler dileriz!")