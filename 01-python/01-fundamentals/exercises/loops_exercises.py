for i in range(1,10+1):
    print(i)
    
for i in range(1,20+1):
    if i % 2 == 0:
        print(i)
        
toplam = 0
for i in range(1,100+1):
    toplam = toplam + i
print(toplam)
    
books = [
    "Python101",
    "Crime and Punishment",
    "Les Misérables",
    "The Outsider"
]
for book in books:
    print(f"Kitap: {book}")
search_name = input("Kitap adını giriniz: ")
for book in books:
    if search_name == book:
        print("Kitap bulundu.")
        break
else:
    print("Kitap bulunamadı.")
    
while True:
    number = int(input("Bir sayı giriniz: "))
    print(f"Girdiğiniz sayı: {number}")
    if number == 0:
        print("Program sonlandırılıyor.")
        break
    
while True:
    number2 = int(input("Lütfen sayınızı giriniz: "))
    if number2 > 0:
        print("Pozitif")
    elif number2 < 0:
        print("Negatif")
    else:
        break 