name = input("Adınızı giriniz: ")
age = int(input("Yaşınızı giriniz: "))
city = str(input("Yaşadığınız şehrinizi giriniz: "))
height = float(input("Boyunuzu giriniz: "))

print(type(name), end=" - ")
print(type(age), end=" - ")
print(type(city), end=" - ")
print(type(height))

print(f"Merhaba, ben {name}. {age} yaşındayım, {city} şehrinde yaşıyorum. Boyum {height} cm.")