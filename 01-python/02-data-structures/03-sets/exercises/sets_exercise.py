books = [
    "Python101",
    "Clean Code",
    "Python101",
    "Computer Science",
    "Clean Code",
    "Python101"
]
set_book = set(books)
print(set_book, type(set_book))

books = {
    "Computer Science",
    "Clean Code",
    "Python101"
    }
books.remove("Computer Science")
print(books)



books = {
    "Python101",
    "Clean Code",
    "Computer Science",
    "The Pragmatic Programmer"
}
search = input("Lütfen kitap adını giriniz: ")
if search in books:
    print("Kitap Bulundu.")
else:
    print("Kitap Bulunamadı.")


programming_books = {
    "Python101",
    "Clean Code",
    "Python Advanced"
}
computer_science_books = {
    "Python101",
    "Algorithms",
    "Computer Science"
}
total_books = programming_books | computer_science_books
print(total_books)

total_books2 = programming_books.intersection(computer_science_books)
print(total_books2)

total_books3 = programming_books - computer_science_books
print(total_books3)


basic_python = {
    "variables",
    "conditions",
    "loops"
}

python_topics = {
    "variables",
    "conditions",
    "loops",
    "functions",
    "oop"
}
print(basic_python.issubset(python_topics))
print(python_topics.issuperset(basic_python))
print(basic_python.isdisjoint(python_topics))

unique_numbers = []
i = 1
while i <= 5:
    want_number = int(input("Lütfen bir sayi giriniz: "))
    unique_numbers.append(want_number)
    i+=1
unique_numbers_set = set(unique_numbers)
print(len(unique_numbers_set))

categories = {
    "Programming",
    "History",
    "Programming",
    "Classic",
    "History"
}
print(len(categories))

python_books = {
    "Python101",
    "Python Advanced",
    "Clean Code"
}
cs_books = {
    "Clean Code",
    "Algorithms",
    "Computer Science"
}
print(python_books | cs_books)
print(python_books & cs_books)
print(python_books)
print(cs_books)