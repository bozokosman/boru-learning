#Number-Guess-Game v3
import random
import json
import os
from datetime import datetime


def get_guess(prompt):
    return int(input(prompt))

def check_guess(guess, target):
    if guess > target:
        return "buyuk"
    elif guess < target:
        return "kuçuk"
    elif guess == target:
        return "dogru"

def load_data():
    if os.path.exists("data_guess.json"):
        with open("data_guess.json", "r", encoding= "utf-8") as data:
            loaded_data = json.load(data)
            return loaded_data
    else:
        default_data = {"high_scores": [], "history": []}
        with open("data_guess.json", "w", encoding= "utf-8") as data:
            json.dump(default_data, data, indent=4, ensure_ascii=False)
        return default_data

def save_data(data):
    with open("data_guess.json", "w", encoding= "utf-8") as jdata:
        json.dump(data, jdata, indent=4, ensure_ascii=False)

def play():
    target = random.randint(1,100)
    attempts = 0
    move = 5
    print("Oyun için 5(beş) hakkınız bulunmaktadır.")
    player = input("Enter your name: ")
    start = datetime.now()
    while move > 0:
        guess = get_guess("Tahminizi yazınız:")
        attempts += 1
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
            end = datetime.now()
            break
    else:
        print(f"Üzgünüm, hakkınız bitti. Sayı {target} idi.")
        end = datetime.now()
    duration = (end - start).total_seconds()
    return {
        "player": player,
        "target": target,
        "attempts": attempts,
        "duration": duration,
        "result": "win" if move > 0 else "lose",
        "date": end.strftime("%Y-%m-%d %H:%M:%S")
    }

def sort_key(score):
    return (score["attempts"], score["duration"])

def add_score(data, score):
    data["history"].append(score)
    if score["result"] == "win":
        data["high_scores"].append(score)
        data["high_scores"] = sorted(data["high_scores"], key=sort_key)
        data["high_scores"] = data["high_scores"][:5]

def show_high_scores(data):
    if not data["high_scores"]:
        return "No high scores yet."
    else:
        output = "--- High Scores ---\n"
        for i, score in enumerate(data["high_scores"], 1):
            output += f"{i}. {score['player']} - {score['attempts']} attempts - {score['duration']:.2f} sec - {score['date']}\n"
        return output

def show_history(data):
    if not data["history"]:
        return "No history yet."
    else:
        output = "--- History ---\n"
        for i, score in enumerate(data["history"], 1):
            output += f"{i}. {score['player']} - target: {score['target']} - {score['attempts']} attempts - {score['duration']:.2f} sec - {score['result']} - {score['date']}\n"
        return output

def main():
    data = load_data()
    print("Sayı tahmin oyununa hoşgeldiniz!")
    while True:
        print("""
1- Oyun Oyna
2- Yüksek Skor Göster
3- Geçmişi Göster
4- Çık
""")
        choose = input("Seçiminizi yapınız: ")
        if choose == "1":
            score = play()
            add_score(data, score)
            save_data(data)
            print("Skor kaydedildi!")
        elif choose == "2":
            print(show_high_scores(data))
        elif choose == "3":
            print(show_history(data))
        elif choose == "4":
            save_data(data)
            print("Hoşçakalın!")
            break
        else:
            print("Yanlış seçim. Lütfen tekrar deneyiniz.")

if __name__ == "__main__": main()