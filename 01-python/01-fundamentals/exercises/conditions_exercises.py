age = int(input("Lütfen yaşınızı belirtiniz: "))
if age >= 18:
    print("Giriş yapabilirsiniz.")
else:
    print("Giriş yapamazsınız")
    
point = int(input("Lütfen aldığınız puanı giriniz: "))
if point >= 90 and point <= 100:
    print("A")
elif point >= 80:
    print("B")
elif point >= 70:
    print("C")
elif point >= 60:
    print("D")
else:
    print("F")

book_available = False 
member = False 

if book_available and member:
    print("Kitabı ödünç alabilirsiniz.")
elif not book_available and member:
    print("Kitap mevcut değil")
elif book_available and not member:
    print("Üyelik gereklidir.")
else:
    print("Burada ne işin var? ve kesinlikle aradığın kitap burada değil")

    
numb1 = int(input("1. Sayınızı giriniz: "))
numb2 = int(input("2. sayınızı giriniz: "))

if numb1 > numb2:
    print("Birinci sayı daha büyüktür")
elif numb1 < numb2:
    print("İkinci sayı daha büyüktür.")
elif numb1 == numb2:
    print("Sayılar eşittir.")

age2 = int(input("Lütfen yaşınızı giriniz: "))
is_ticket = input("Biletiniz varmı? E/H: ").lower()
if is_ticket == "e":
    is_ticket = True
else:
    is_ticket = False
    
if age2 < 18:
    print("Yaşınız yeterli değil.")
elif age2 >= 18 and is_ticket:
    print("Giriş yapabilirsiniz.")
elif age2 >= 18 and not is_ticket:
    print("Bilet gerekli")
    
    
#Bonus
sayi = int(input("Sayınızı giriniz: "))
if sayi == 0 :
    print("Sayı SIFIR")
elif sayi > 0 :
    print("Sayı POZİTİF")
else:
    print("Sayı NEGATİF")