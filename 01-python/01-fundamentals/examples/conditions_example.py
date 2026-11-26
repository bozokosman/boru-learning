# if

age = 25

if age >= 18:
    print("Yetişkinsiniz.")


# if + else

age = 16

if age >= 18:
    print("Giriş yapabilirsiniz.")
else:
    print("Giriş yapamazsınız.")


# if + elif + else

score = 75

if score >= 90:
    print("A")
elif score >= 70:
    print("B")
elif score >= 50:
    print("C")
else:
    print("F")


# Comparison operators with conditions

age = 32

if age == 32:
    print("Yaş 32.")

if age != 20:
    print("Yaş 20 değil.")

if age > 18:
    print("Yaş 18'den büyük.")

if age >= 18:
    print("Yetişkin.")


# and

age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("Giriş yapabilirsiniz.")
else:
    print("Giriş yapamazsınız.")


# or

has_cash = False
has_card = True

if has_cash or has_card:
    print("Ödeme yapabilirsiniz.")
else:
    print("Ödeme yapılamaz.")


# not

is_closed = False

if not is_closed:
    print("Açık.")


# Nested conditions

age = 25
has_ticket = True

if age >= 18:
    if has_ticket:
        print("Giriş yapabilirsiniz.")
    else:
        print("Biletiniz yok.")
else:
    print("Yaşınız yeterli değil.")


# Nested conditions with and

if age >= 18 and has_ticket:
    print("Giriş yapabilirsiniz.")


# User input

user_age = int(input("Yaşınızı giriniz: "))

if user_age >= 18:
    print("Giriş yapabilirsiniz.")
else:
    print("Giriş yapamazsınız.")


# Multiple conditions

score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")


# Practical example: library

book_available = True
member = True

if book_available and member:
    print("Kitabı ödünç alabilirsiniz.")
elif not book_available:
    print("Kitap mevcut değil.")
else:
    print("Üyelik gereklidir.")