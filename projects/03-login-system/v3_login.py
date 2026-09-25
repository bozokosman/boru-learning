#Login-System v3
import json
import os

def get_username(prompt):
    return input(prompt).lower()

def get_password(prompt):
    return input(prompt)

def load_data():
    if os.path.exists("data_login.json"):
        with open("data_login.json", "r", encoding="utf-8") as login_data:
            loaded_data = json.load(login_data)
            return loaded_data
    else:
        default_data = {"users": {}}
        with open("data_login.json", "w", encoding="utf-8") as login_data:
            json.dump(default_data, login_data, indent=4 , ensure_ascii=False)
        return default_data

def save_data(data):
    with open("data_login.json", "w", encoding="utf-8") as login_data:
        json.dump(data, login_data, indent=4, ensure_ascii=False)

def register(data, username, password):
    if username in data["users"]:
        return "exists"
    else:
        data["users"][username] = password
        return "created"

def login(data):
    move = 3
    while move > 0:
        username = get_username("Username: ")
        password = get_password("Password: ")
        if username not in data["users"]:
            return "not_found"
        elif data["users"][username] != password:
            move -= 1
            print(f"Hatalı şifre! Kalan hak: {move}")
        else:
            return "success"
    return "blocked"

def main():
    data = load_data()
    while True:
        print("""
1- Giriş yap
2- Kayıt Ol
3- Çıkış
""")
        choose = input("Seçiminizi yapınız: ")
        if choose == "1":
            result = login(data)
            if result == "success":
                print("Giriş Başarılı!")
            elif result == "not_found":
                print("Kullanıcı adı bulunamadı.")
            elif result == "blocked":
                print("Hesabınız bloke oldu! Lütfen yöneticiniz ile görüşün.")
        elif choose == "2":
            username = get_username("Kullanıcı adınızı giriniz: ")
            password = get_password("Şifrenizi giriniz: ")
            result = register(data, username, password)
            if result == "created":
                save_data(data)
                print(f"Kayıt başarı ile oluşturuldu '{username}'.")
            else:
                print(f"{username} isimli bir kullanıcı zaten var.")
        elif choose == "3":
            print("Hoşçakalın")
            break
        else:
            print("Yanlış seçim yaptınız. Lütfen tekrar deneyiniz.")

if __name__ == "__main__": main()