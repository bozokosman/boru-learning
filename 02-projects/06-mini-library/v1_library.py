def kitap_ekle(ekleme):
    ad = input("Lütfen eklemek istediğiniz kitabın adını giriniz: ")
    yazar = input("Lütfen eklemek istediğiniz kitabın yazarını giriniz: ")
    yil = input("Lütfen eklemek istediğiniz kitabın yılını giriniz: ")
    yeni_kitap = {"ad": ad, "yazar": yazar, "yıl": yil}
    ekleme.append(yeni_kitap)
    print("Kitabınız, kitaplığa eklenmiştir.")

def kitap_listele(kitaplar):
    for kitap in kitaplar:
        print(kitap)

def kitap_ara(kitaplar):
    arama = input("Lütfen aradığınız kitabın adını giriniz: ")
    for kitap in kitaplar:
        if kitap["ad"] == arama:
            print(f"{arama} isimli kitap bulunmuştur: {kitap}")
            break
        else:
            print(f"{arama} isimli kitap kitaplıkta yoktur.")

def kitap_sil(silinecek):
    silme = input("Kitaplıktan kaldırmak istediğiniz kitabın adını yazınız: ")
    for kitap in silinecek:
        if kitap["ad"] == silme:
            silinecek.remove(kitap)
            print("Kitap başarıyla silinmiştir.")
            break
        else:
            print(f"{silme} isimli kitap, kitaplıkta bulunamadı.")

kitaplik = []
while True:
    print("""
    ===== KÜTÜPHANE =====
    1 - Kitap Ekle
    2 - Kitapları Listele
    3 - Kitap Ara
    4 - Kitap Sil
    5 - Çıkış
    """)
    secim = input("Lütfen yapmak istediğiniz işlemin numarasını seçiniz: ")
    if secim == "1":
        kitap_ekle(kitaplik)
    elif secim == "2":
        kitap_listele(kitaplik)
    elif secim == "3":
        kitap_ara(kitaplik)
    elif secim == "4":
        kitap_sil(kitaplik)
    elif secim == "5":
        print("Hoşçakalın")
        break