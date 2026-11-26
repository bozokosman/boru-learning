#Number-Guess-Game v2
import random

def get_guess(prompt):
    return int(input(prompt))

def check_guess(guess, target):
    if guess > target:
        return "buyuk"
    elif guess < target:
        return "kuçuk"
    elif guess == target:
        return "dogru"

def play():
    target = random.randint(1,100)
    move = 5
    print("Oyun için 5(beş) hakkınız bulunmaktadır.")
    while move > 0:
        guess = get_guess("Tahminizi yazınız:")
        result = check_guess(guess, target)
        if result == "buyuk":
            print("Tahmininiz büyüktür.")
            move -= 1
            print(f"Kalan hakkınız: {move}")
        elif result == "kucuk":
            print("Tahmininiz küçüktür.")
            move -= 1
            print(f"Kalan hakkınız: {move}")
        elif result == "dogru":
            print("Tebrikler! Doğru bildiniz.")
            break
    else:
        print(f"Üzgünüm, hakkınız bitti. Sayı {target} idi.")

def main():
    play()

if __name__ == "__main__": main()
main()