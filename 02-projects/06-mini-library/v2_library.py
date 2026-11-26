class Library:
    def __init__(self, library_name, address):
        self.library_name = library_name
        self.address = address
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)

library = Library(
    library_name= "Ege",
    address = "Kordon Caddesi")

class Book:
    def __init__(self, name, author, page, category):
        self.name = name # Dışarıdan gelen name değerini bu nesnenin name özelliğine atadım.
        self.author = author # Dışarıdan gelen author değerini bu nesnenin author özelliğine atadım.
        self.page = page # Dışarıdan gelen page değerini bu nesnenin page özelliğine atadım.
        self.category = category # Dışarıdan gelen category değerini bu nesnenin category özelliğine atadım.
        
    def info(self):
        return f"Kitabın adı: {self.name}, kitabın yazarı: {self.author}, kitabın sayfa sayısı: {self.page}, kitabın türü: {self.category}"
        


book1 = Book(
    name = "Python101",
    author = "Osman Bozok",
    page = 100,
    category = "Programming")

book2 = Book(
    name = "Crime and Punishment",
    author = "Dostoyevski",
    page = 705,
    category = "World Classics")

book3 = Book(
    name = "Les Misérables",
    author = "Victor Hugo",
    page = 1724,
    category = "World Classics")

book4 = Book(
    name = "The Outsider",
    author = "Albert Camus",
    page = 128,
    category = "World Classics")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
for book in library.books:
    print(book.info())