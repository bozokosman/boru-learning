#Calculator v4
import json
import os
from datetime import datetime

def addition(n1,n2):
    result = n1 + n2
    return result

def subtraction(n1,n2):
    result = n1 - n2
    return result

def multiplication(n1,n2):
    result = n1 * n2
    return result

def division(n1,n2):
    while True:
        if n2 == 0:
            print("Hata: Bir sayı sıfıra bölünemez. Lütfen 0'dan farklı bir sayı giriniz.")
            n2 = float(input("İkinci sayınızı giriniz: "))
        else:
            result = n1 / n2
            return result

def show_menu():
    print("Toplama işlemi için: '+'\nÇıkarma işlemi için: '-'\nBölme işlemi için: '/'\nÇarpma işlemi için: '*'\nÇıkmak için: '0'\nGeçmişi görmek için: 'h'\nSeçeneklerini kullanabilirsiniz")

def get_number(prompt):
    return float(input(prompt))

def load_data():
    if os.path.exists("data_calc.json"):
        with open("data_calc.json", "r", encoding="utf-8") as jdata:
            loaded_data = json.load(jdata)
            return loaded_data
    else:
        default_data = {"history": []}
        with open("data_calc.json", "w", encoding= "utf-8") as jdata:
            json.dump(default_data, jdata, indent=4, ensure_ascii=False)
        return default_data

def save_data(data):
    with open("data_calc.json", "w", encoding="utf-8") as jdata:
        json.dump(data, jdata, indent=4, ensure_ascii=False)

def add_history(data, num1, num2, operation, result):
    record = {
        "num1": num1,
        "num2": num2,
        "operation": operation,
        "result": result,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    data["history"].append(record)

def show_history(data):
    if not data["history"]:
        return "No history yet."
    else:
        output = "--- History ---\n"
        for i, progress in enumerate(data["history"], 1):
            output += f"{i} - {progress['num1']} {progress['operation']} {progress['num2']} = {progress['result']} - {progress['date']}\n"
        return output

def main():
    data = load_data()
    while True:
        show_menu()
        progress = input("Lütfen işleminizi seçiniz: ")
        if progress == "0":
            save_data(data)
            print("Hoşçakalın.")
            break
        elif progress in ["+", "-", "*", "/"]:
            number1 = get_number("İlk sayınızı giriniz: ")
            number2 = get_number("İkinci sayıyı giriniz: ")
            if progress == "+":
                result = addition(number1, number2)
            elif progress == "-":
                result = subtraction(number1, number2)
            elif progress == "*":
                result = multiplication(number1, number2)
            elif progress == "/":
                result = division(number1, number2)
            print(f"Sonuç: {result}")
            add_history(data , number1, number2, progress, result)
        elif progress == "h":
            print(show_history(data))
        else:
            print("Bir yanlışlık olmuş olmalı. Lütfen baştan başlayınız.")

if __name__ == "__main__": main()