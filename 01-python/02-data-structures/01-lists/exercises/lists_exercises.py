books = ["Python101", "Clean Code", "Computer Science"]
books[0] = "Python Advanced"
books.append("Developer101")
print(books)

books2 = []
books2.append("Python101")
books2.append("Crime and Punishment")
books2.append("Les Misérables")
books2.append("The Outsider")
print(books2)

books2.remove("Crime and Punishment")
for book in books2:
    print(book)
    
books3 = ["Python101", "Clean Code", "Computer Science"]
print(f"Çıkarılan kitap: {books3.pop()}")
print(books3)

books4 = [
    "Python101",
    "Crime and Punishment",
    "Les Misérables",
    "The Outsider"]

search_name = input("Aradığınız kitabı giriniz: ")
if search_name in books4:
    print("Kitap bulundu.")
else:
    print("Kitap bulunamadı.")
    
numbers = [3, 8, 11, 20, 25, 32, 41, 50]
for number in numbers:
    if number % 2 == 0:
        print(number)
        
numbers2 = [10, 20, 30, 40, 50]
total = 0
for number in numbers2:
    total += number
print(total)

books5 = []
while True:
    islem = input("""Kitap eklemek için '1',
Çıkmak için '0' Tuşlayınız,
""")
    if islem == "1":
        add = input("Lütfen eklemek istediğiniz kitabın adını giriniz: ")
        books5.append(add)
        print("Kitap eklendi")
    else:
        print("Hoşçakalın")
        break
print("Kütüphaneye eklenen kitaplar")
for book in books5:
    print(book)
    
search_name2 = input("Kaldırmak istrediğiniz kitabın adını yazınız: ")
for book in books5:
    if search_name2 == book:
        print("Kitap bulundu ve listeden kaldırılıyor.")
        books5.remove(search_name2)
        break
else:
    print("Kitap bulunamadı.")

    
    
        