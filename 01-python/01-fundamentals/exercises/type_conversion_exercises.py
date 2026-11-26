age = int(input("Yaşınızı giriniz: "))
age5 = age + 5
print(f"5 Yıl sonraki yaşınız: {age5}")

numb1 = int(input("1. Sayıyı giriniz: "))
numb2 = int(input("2. Sayıyı giriniz: "))
print("Toplamı: ", numb1 + numb2)
print("Farkı: " ,numb1 - numb2)
print("Çarpımı: ", numb1 * numb2)
print("Bölümü: ", numb1 / numb2)

name = input("Adınız: ")
age2 = int(input("Yaşınız: "))
height = float(input("Boyunuz: "))
print(f"Ben {name}, {age2} yaşındayım ve boyum {height} cm.")


book = input("Kitap adı: ")
author = input("Yazar adı: ")
page = input("Sayfa sayısı: ")
page = int(page)
print(f"Kitap: {book}\nYazar: {author}\nSayfa : {page}")

number = input("Bir sayı giriniz: ")
print(number, type(number))
number = int(number)
print(number, type(number))
number = float(number)
print(number, type(number))
number = bool(number)
print(number, type(number))