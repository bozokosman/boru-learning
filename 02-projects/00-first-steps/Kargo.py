import random

mesafeler = {
    "TIVAT": 85,
    "KOTOR": 90,
    "BUDVA": 65,
    "NIKSIC": 50,
    "ULCINJ": 80
}
def kargo_maliyeti_hesapla(mesafe, agirlik, ekspres=False):
    if mesafe <= 0 or agirlik <= 0:
        return "Hata: Geçersiz mesafe veya ağırlık!"
    mesafe_toplam = mesafe * 0.5
    agirlik_toplam = agirlik * 2
    toplam_tutar = mesafe_toplam + agirlik_toplam
    if ekspres == True :
        return toplam_tutar + 15
    return toplam_tutar

def etiket_olustur(alici, sehir, takip_no):
    return f"--- KARGO ETİKETİ --- \n Alıcı: [{alici.strip().upper()}] | Şehir: [{sehir.strip().upper()}] | Takip No: [{takip_no.strip().upper()}]"

def kargo_sistemi_merkezi():
    isim = input("Gönderilen kişinin adını giriniz: ")
    yer = input("Gonderilecek şehiri giriniz: ")
    kilo = float(input("Paket ağırlığı: "))
    hizli = input("Hızlı teslimat ister misiniz? (E/H): ").strip().upper() == "E"
    yolculuk_mesafesi = mesafeler[yer.upper().strip()]

    rastgele = str(random.randint(100000, 999999))
    takip = f"MNE-2026-{rastgele}"
    ucret = kargo_maliyeti_hesapla(mesafe=yolculuk_mesafesi, agirlik=kilo, ekspres=hizli)
    if "Hata" in str(ucret):
        print(ucret)
    else:
        etiket = etiket_olustur(alici=isim, sehir=yer, takip_no=takip)
        print(etiket)
        print(f"Toplam Ödenecek Tutar: {ucret}€")

kargo_sistemi_merkezi()