#Calculator v3

def addition(n1,n2):
    return f"Sonuç: {n1 + n2}"

def subtraction(n1,n2):
    return f"Sonuç: {n1 - n2}"

def multiplication(n1,n2):
    return f"Sonuç: {n1 * n2}"

def division(n1,n2):
    while True:
        if n2 == 0:
            print("Hata: Bir sayı sıfıra bölünemez. Lütfen 0'dan farklı bir sayı giriniz.")
            n2 = float(input("İkinci sayınızı giriniz: "))
        else:
            return f"Sonuç: {n1 / n2}"

def show_menu():
    print("Toplama işlemi için: '+'\nÇıkarma işlemi için: '-'\nBölme işlemi için: '/'\nÇarpma işlemi için: '*'\nÇıkmak için: '0'\nSeçeneklerini kullanabilirsiniz")

def get_number(prompt):
    return float(input(prompt))

def main():
    while True:
        show_menu()
        progress = input("Lütfen işleminizi seçiniz: ")
        if progress == "0":
            print("Hoşçakalın.")
            break
        elif progress in ["+", "-", "*", "/"]:
            number1 = get_number("İlk sayınızı giriniz: ")
            number2 = get_number("İkinci sayıyı giriniz: ")

            if progress == "+":
                print(addition(number1, number2))
            elif progress == "-":
                print(subtraction(number1, number2))
            elif progress == "*":
                print(multiplication(number1, number2))
            elif progress == "/":
                print(division(number1, number2))
        else:
            print("Bir yanlışlık olmuş olmalı. Lütfen baştan başlayınız.")

if __name__ == "__main__": main()
main()
