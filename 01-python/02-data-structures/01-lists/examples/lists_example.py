# 1. Liste oluşturma

books = ["Python101", "Clean Code", "Computer Science"]

print(books)


# 2. Index ile erişim

print(books[0])
print(books[1])
print(books[-1])


# 3. Eleman değiştirme

books[0] = "Python Advanced"

print(books)


# 4. Listenin uzunluğu

print(len(books))


# 5. append()

books.append("Developer101")

print(books)


# 6. insert()

books.insert(1, "Algorithms")

print(books)


# 7. remove()

books.remove("Algorithms")

print(books)


# 8. pop()

removed_book = books.pop(1)

print(f"Çıkarılan kitap: {removed_book}")
print(books)


# 9. in

print("Python Advanced" in books)
print("Java" in books)


# 10. not in

if "Java" not in books:
    print("Java listede bulunmuyor.")


# 11. for ile liste üzerinde dolaşma

for book in books:
    print(f"Kitap: {book}")


# 12. Liste dilimleme

numbers = [0, 1, 2, 3, 4, 5]

print(numbers[1:4])
print(numbers[:3])
print(numbers[3:])


# 13. Adımlı dilimleme

print(numbers[0:6:2])


# 14. Listeyi ters çevirme

print(numbers[::-1])


# 15. sort()

numbers2 = [5, 2, 8, 1, 3]

numbers2.sort()

print(numbers2)

numbers2.sort(reverse=True)

print(numbers2)


# 16. reverse()

books.reverse()

print(books)


# 17. count()

numbers3 = [1, 2, 2, 3, 2, 4]

print(numbers3.count(2))


# 18. index()

print(books.index("Python Advanced"))


# 19. Liste birleştirme

books1 = ["Python101", "Clean Code"]
books2 = ["Computer Science", "Developer101"]

all_books = books1 + books2

print(all_books)


# 20. Liste içinde liste

library = [
    ["Python101", "Osman Bozok"],
    ["Clean Code", "Robert C. Martin"]
]

print(library)
print(library[0])
print(library[0][0])


# 21. Liste üzerinde koşul

numbers4 = [1, 2, 3, 4, 5, 6]

for number in numbers4:
    if number % 2 == 0:
        print(f"Çift sayı: {number}")


# 22. Listeyi filtreleme mantığı

world_classics = [
    "Crime and Punishment",
    "Les Misérables",
    "The Outsider"
]

for book in world_classics:
    print(f"World Classic: {book}")


# 23. Nesneleri listede tutma

class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author


book1 = Book("Python101", "Osman Bozok")
book2 = Book("Clean Code", "Robert C. Martin")

book_list = []

book_list.append(book1)
book_list.append(book2)

for book in book_list:
    print(book.name)
    print(book.author)