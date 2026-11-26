# print()

print("Hello World")

name = "Osman"
age = 32

print(name)
print(age)
print(name, age)


# input()

name = input("Adınızı giriniz: ")

print(name)
print(type(name))


# input() + int()

age = int(input("Yaşınızı giriniz: "))

print(age)
print(type(age))


# input() + float()

height = float(input("Boyunuzu giriniz: "))

print(height)
print(type(height))


# sep

name = "Osman"
age = 32
city = "Podgorica"

print(name, age, city, sep=" - ")


# end

print("Hello", end=" ")
print("World")


# f-string

name = "Osman"
age = 32

print(f"My name is {name}. I am {age} years old.")


# Combining input, type conversion and f-string

name = input("Adınız: ")
age = int(input("Yaşınız: "))

print(f"Merhaba {name}. Gelecek yıl {age + 1} yaşında olacaksınız.")