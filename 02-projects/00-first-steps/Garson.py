menu = {
    "Cevapi": 7.50,
    "Njeguski Prsut": 12.00,
    "Sopska Salata": 3.50,
    "Niksicko Pivo": 2.50
}
def hesap_hesapla(siparis_listesi):
    toplam = 0
    for yemek in siparis_listesi:
        toplam = toplam + menu[yemek]
    if toplam > 50 :
        toplam = toplam * 0.90
    kalite = input("Servisimiz nasıldı? (i/o/k):" ).lower()
    if kalite == "i":
        toplam = toplam * 1.15
    elif kalite == "o":
        toplam = toplam * 1.10
    else:
        print("Bahşiş eklenmedi.")
    return toplam

siparisler = []
sip = input("Sipariş vermek ister misiniz? (e/h): ").lower()
if sip == "e":
    print("--- KONOBA MENÜSÜ ---")
    for yemek, fiyat in menu.items():
        print(f"{yemek}: {fiyat}€")
    while True:
        secim = input("Yemek adı giriniz: ").title()
        if secim == "0":
            break
        if secim in menu:
            siparisler.append(secim)
            print(f"{secim} sepete eklendi.")
        else:
            print("Maalesef menümüzde böyle bir yemek yok, lütfen tekrar deneyin.")

    if len(siparisler) > 0:
        toplam_hesap = hesap_hesapla(siparisler)
        print(f"Toplam Tutar: {toplam_hesap:.2f}€")
    else:
        print("Hiç sipariş vermediniz.")
else:
    print("İyi günler dileriz")
