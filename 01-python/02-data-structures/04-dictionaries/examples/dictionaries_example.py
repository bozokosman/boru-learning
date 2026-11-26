# 1. Dictionary oluşturma

book = {
    "name": "Python101",
    "author": "Osman Bozok",
    "page": 5000,
    "category": "Programming"
}

print(book)


# 2. Değerlere erişme

print(book["name"])
print(book["author"])
print(book["page"])
print(book["category"])


# 3. Yeni veri ekleme

book["language"] = "Python"

print(book)


# 4. Mevcut veriyi değiştirme

book["page"] = 6000

print(book)


# 5. get()

print(book.get("name"))
print(book.get("publisher"))
print(book.get("publisher", "Yayıncı bilgisi yok"))


# 6. in

print("name" in book)
print("publisher" in book)


# 7. keys()

print(book.keys())


# 8. values()

print(book.values())


# 9. items()

print(book.items())


# 10. Dictionary üzerinde for

for key in book:
    print(key)


# 11. Key ve value birlikte

for key, value in book.items():
    print(f"{key}: {value}")


# 12. Sadece value'lar

for value in book.values():
    print(value)


# 13. Veri silme

del book["language"]

print(book)


# 14. pop()

page = book.pop("page")

print(f"Çıkarılan sayfa bilgisi: {page}")
print(book)


# 15. Dictionary uzunluğu

print(len(book))


# 16. Dictionary listesi

books = [
    {
        "name": "Python101",
        "author": "Osman Bozok",
        "page": 5000,
        "category": "Programming"
    },
    {
        "name": "Crime and Punishment",
        "author": "Dostoyevski",
        "page": 705,
        "category": "World Classics"
    },
    {
        "name": "Les Misérables",
        "author": "Victor Hugo",
        "page": 1724,
        "category": "World Classics"
    },
    {
        "name": "The Outsider",
        "author": "Albert Camus",
        "page": 128,
        "category": "World Classics"
    }
]


# 17. Dictionary listesi üzerinde dolaşma

for book in books:
    print(book)


# 18. Sadece kitap isimlerini listeleme

for book in books:
    print(book["name"])


# 19. Kitap adı ve yazar

for book in books:
    print(f"{book['name']} - {book['author']}")


# 20. Belirli kategoriye göre filtreleme

for book in books:
    if book["category"] == "World Classics":
        print(book["name"])


# 21. Sayfa sayısına göre kontrol

for book in books:
    if book["page"] > 1000:
        print(f"{book['name']} 1000 sayfadan uzun.")


# 22. Kullanıcıdan kitap arama

search_name = input("Aradığınız kitabın adını giriniz: ")

for book in books:
    if book["name"] == search_name:
        print(f"{search_name} isimli kitap bulundu.")
        break
else:
    print("Kitap bulunamadı.")


# 23. Dictionary ve list kombinasyonu

new_book = {
    "name": "Developer101",
    "author": "Osman Bozok",
    "page": 350,
    "category": "Programming"
}

books.append(new_book)

print(books)


# 24. Dictionary'nin içindeki değeri değiştirme

books[0]["page"] = 5500

print(books[0])


# 25. Dictionary içindeki veriler üzerinde dolaşma

for book in books:
    print("----------")
    for key, value in book.items():
        print(f"{key}: {value}")