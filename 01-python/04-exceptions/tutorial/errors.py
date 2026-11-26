def get_positive_number():
    while True:
        try:
            number = int(input("Lütfen pozitif bir sayı giriniz: "))
            if number > 0 :
                return number
            else:
                print("Lütfen 0'dan büyük bir sayı giriniz")
        except ValueError:
            print("Lütfen bir sayı giriniz!")

result = get_positive_number()
print(f"Başarılı! Sayınız: {result}")