#Calculator v1

number1 = float(input("İlk sayınızı giriniz: "))
number2 = float(input("İkinci sayınızı giriniz: "))
print("Toplama işlemi için: '+'\nÇıkarma işlemi için: '-'\nBölme işlemi için: '/'\nÇarpma işlemi için: '*'\nSeçeneklerini kullanabilirsiniz")
progress = input("Lütfen işleminizi seçiniz: ")

if progress == "+":
    sonuc = number1 + number2
    print(f"Sonuç : {sonuc}")
elif progress == "-":
    sonuc = number1 - number2
    print(f"Sonuç : {sonuc}")
elif progress == "/":
    if number2 == 0:
        print("Hata: Bir sayı sıfıra bölünemez. Lütfen 0'dan farklı bir sayı giriniz.")
    else:
        sonuc = number1 / number2
        print(f"Sonuç : {sonuc}")
elif progress == "*":
    sonuc = number1 * number2
    print(f"Sonuç : {sonuc}")
else:
    print("Bir yanlışlık yapmış olmalısınız. Lütfen tekrar deneyiniz.")