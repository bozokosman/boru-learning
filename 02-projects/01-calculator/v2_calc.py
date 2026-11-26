#Calculator v2

while True:
    print("Toplama işlemi için: '+'\nÇıkarma işlemi için: '-'\nBölme işlemi için: '/'\nÇarpma işlemi için: '*'\nÇıkmak için: '0'\nSeçeneklerini kullanabilirsiniz")
    progress = input("Lütfen işleminizi seçiniz: ")
    if progress == "0":
        break
    else:
        number1 = float(input("İlk sayınızı giriniz: "))
        number2 = float(input("İkinci sayınızı giriniz: "))
        if progress == "+":
            sonuc = number1 + number2
            print(f"Sonuç : {sonuc}")
        elif progress == "-":
            sonuc = number1 - number2
            print(f"Sonuç : {sonuc}")
        elif progress == "/":
            while True:
                if number2 == 0:
                    print("Hata: Bir sayı sıfıra bölünemez. Lütfen 0'dan farklı bir sayı giriniz.")
                    number2 = float(input("İkinci sayınızı giriniz: "))
                else:
                    sonuc = number1 / number2
                    print(f"Sonuç : {sonuc}")
                    break 
        elif progress == "*":
            sonuc = number1 * number2
            print(f"Sonuç : {sonuc}")
        else:
            print("Bir yanlışlık yapmış olmalısınız. Lütfen tekrar deneyiniz.")