number1 = int(input("Lütfen bir sayı giriniz: "))
number2 = int(input("Lütfen ikinci sayınızı giriniz: "))

def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(n **0.5)+1):
            if n % i == 0:
                return False
        else:
            return True

while True:
    if number1 < number2:
        for i in range(number1,number2):
            if is_prime(i)== True:
                print(i)
        break
    else:
        print("İlk sayınız, ikinci sayınızdan küçük olamaz. Lütfen tekrar deneyiniz.")
        number1 = int(input("Lütfen ilk sayınızı giriniz: "))
        number2 = int(input("Lütfen ikinci sayınızı giriniz: "))