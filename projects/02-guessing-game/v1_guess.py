import random

target = random.randint(1,100)
move = 5
print("Oyun için 5(beş) hakkınız bulunmaktadır.")

while move > 0 :
    guess = input("Lütfen tahmin ettiğiniz sayıyı giriniz: ")
    guess = int(guess)
    if guess > target:
        print("Tahmininiz büyüktür.")
        move -= 1
        print(f"Kalan hakkınız: {move}")
    elif guess < target:
        print("Tahmininiz küçüktür.")
        move -= 1
        print(f"Kalan hakkınız: {move}")
    elif guess == target:
        print("Tebrikler! Doğru bildiniz.")
        break
else:
    print(f"Üzgünüm, hakkınız bitti. Sayı {target} idi.")