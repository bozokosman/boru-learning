book = {
    "name": "Python101",
    "author": "Osman Bozok",
    "page": 5000,
    "category": "Programming"
}
print(book["name"])
print(book["author"])
print(book["page"])
print(book["category"])

book["page"] = 5500
book["publisher"] = "Börü Publishing"
print(book)

search = input("Kitabın hangi bilgisine ihtiyacınız var: ")
if search in book.keys():
    print(book.get(search))
else:
    print("Bu bilgi kitapta bulunmuyor.")
    
for key, value in book.items():
    print(f"{key}: {value}")
    
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
    }
]
for book in books:
    print(book["name"])
    
for book in books:
    if book["category"] == "World Classics":
        print(book["name"])
        
for book in books:
    if book["page"] > 1000:
        print(book["name"])
        
search_name = input("Aradığınız kitap adını giriniz: ")
for book in books:
    if search_name == book["name"]:
        print("Kitap bulundu")
        break
else:
    print("Kitap bulunamadı.")
    
new_book = {
    "name": "Developer101",
    "author": "Osman Bozok",
    "page": 350,
    "category": "Programming"}
books.append(new_book)
for book in books:
    print(book)
    
books2 = []
while True:
    islem = input("""Kitap eklemek için '1',
Çıkmak için '0' Tuşlayınız,
""")
    if islem == "1":
        name = input("Lütfen eklemek istediğiniz kitabın adını giriniz: ")
        author = input("Lütfen eklemek istediğiniz kitabın yazarını giriniz: ")
        page = int(input("Lütfen eklemek istediğiniz kitabın sayfasını giriniz: "))
        category = input("Lütfen eklemek istediğiniz kitabın kategorisini giriniz: ")
        yeni_kitap = {"ad": name, "yazar": author, "sayfa": page, "kategori": category}
        books2.append(yeni_kitap)
        print("Kitabınız, kitaplığa eklenmiştir.")
    else:
        print("Hoşçakalın")
        break
for book in books2:
    print(book)