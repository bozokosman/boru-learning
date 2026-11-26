# String -> Integer
age = "32"
age = int(age)

print(age)
print(type(age))


# String -> Float
height = "95.5"
height = float(height)

print(height)
print(type(height))


# Integer -> String
number = 100
number = str(number)

print(number)
print(type(number))


# Integer -> Float
number2 = 50
number2 = float(number2)

print(number2)
print(type(number2))


# Integer -> Boolean
number3 = 1

print(bool(number3))


# Input -> Integer
user_age = int(input("Yaşınızı giriniz: "))

print(user_age)
print(type(user_age))


# Input -> Float
user_height = float(input("Boyunuzu giriniz: "))

print(user_height)
print(type(user_height))


# Input ile matematiksel işlem
number1 = int(input("Birinci sayıyı giriniz: "))
number2 = int(input("İkinci sayıyı giriniz: "))

print(number1 + number2)