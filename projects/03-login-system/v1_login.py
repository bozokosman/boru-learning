main_id = "admin"
main_pass = "q1w2e3"
move = 3
while move > 0:
    username = input("Lütfen kullanıcı adını giriniz: ").lower()
    password = input("Lütfen şifresinizi giriniz: ").lower()
    if username != main_id and password != main_pass:
        print("Kullanıcı adı ve şifre yanlıştır.")
        move -=1
        print(f"Kalan hakkınız: {move}")
    elif username != main_id and password == main_pass:
        print("Kullanıcı adı yanlıştır.")
        move -=1
        print(f"Kalan hakkınız: {move}")
    elif username == main_id and password != main_pass:
        print("Şifreniz yanlıştır.")
        move -=1
        print(f"Kalan hakkınız: {move}")
    else:
        print(f"Hoşgeldiniz, {main_id}")
        break
else:
    print("Hesabınız bloke oldu! Lütfen yöneticiniz ile iletişime geçiniz.")