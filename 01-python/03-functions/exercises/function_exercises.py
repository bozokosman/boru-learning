def say_hello():
    return "Hello world!"
print(say_hello())

def greet_user(name):
    return f"Hello, {name}"
name = input("Adınızı giriniz: ")
print(greet_user(name))

def user_info(name,age,city):
    return f"Merhaba, ben {name}, {age} yaşındayım ve {city} şehrinde yaşıyorum."
print(user_info("osman", 32, "PG"))

def add_numbers(a,b):
    return a+b
result = add_numbers(5,4)
print(result)

def square(a):
    return a ** 2
result2 = square(5)
print(result2)

def is_even(a):
    if a % 2 == 0:
        return True
    else:
        return False
result3 = is_even(5)
print(result3)

def user_greet2(name="Guest"):
    return f"Hello, {name}"
print(user_greet2())
print(user_greet2("Osman"))

def user(name, age, city):
    return f"{name}, {age}, {city}"
print(user(age=33, city="PG", name="Osman"))

def user2(name, age, city):
    return name, age, city
a,b,c = user2("osman", 32, "PG")
print(a,b,c)

numbers = [10, 20, 30, 40]
def calculate_total(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
print(calculate_total(numbers))
        
def find_max(numbers):
    bigger = numbers[0]
    for number in numbers:
        if number > bigger:
            bigger = number
    return bigger
print(find_max(numbers))

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
def find_book(books, search):
    for book in books:
        if book["name"] == search:
            return True
    else:
        return False
print(find_book(books, "The Outsider"))

def sum_numbers(*number):
    total = 0
    for i in number:
        total += i
    return total
print(sum_numbers(10, 20, 30, 40))

def show_information(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
show_information(
    name="Osman",
    age=32,
    city="PG"
)

def double(number):
    return number *2
def square2(number):
    return number ** 2
sayi = 5
print(square2(double(sayi)))

def countdown(current):
    if current == 0:
        return
    print(current)
    countdown(current-1)
countdown(10)

def calculate_average(list):
    total = 0
    for number in list:
        total+= number
    return total / len(list)
print(calculate_average(numbers))

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
def find_common_books(set1,set2):
    return set1 & set2
print(find_common_books(programming_books,computer_science_books))


book = {
    "name": "Python101",
    "author": "Osman Bozok",
    "page": 5000
}
def print_book(book):
    print(f"Kitap: {book['name']}")
    print(f"Yazar: {book['author']}")
    print(f"Sayfa: {book['page']}")
print_book(book)