# ==========================================
# PYTHON FUNCTIONS EXAMPLES
# ==========================================


# 1. Basic Function


def greet():
    print("Merhaba!")


greet()


# ==========================================
# 2. Function Call
# ==========================================


def say_hello():
    print("Hello")


say_hello()
say_hello()
say_hello()


# ==========================================
# 3. Parameter and Argument
# ==========================================


def greet_user(name):
    print(f"Merhaba {name}!")


greet_user("Osman")
greet_user("Ahmet")


# ==========================================
# 4. Multiple Parameters
# ==========================================


def introduce(name, age, city):
    print(f"Ben {name}. {age} yaşındayım ve {city} şehrinde yaşıyorum.")


introduce("Osman", 32, "Podgorica")


# ==========================================
# 5. Return
# ==========================================


def add(number1, number2):
    return number1 + number2


result = add(10, 20)

print(result)


# ==========================================
# 6. Print vs Return
# ==========================================


def add_print(number1, number2):
    print(number1 + number2)


def add_return(number1, number2):
    return number1 + number2


add_print(10, 20)

result = add_return(10, 20)

print(result)


# ==========================================
# 7. Return Ends the Function
# ==========================================


def test_return():
    print("Fonksiyon başladı.")
    return
    print("Bu satır çalışmaz.")


test_return()


# ==========================================
# 8. Function Calculation
# ==========================================


def square(number):
    return number ** 2


print(square(5))
print(square(10))
print(square(20))


# ==========================================
# 9. Local Variable
# ==========================================


def calculate():
    number = 10
    print(number)


calculate()


# ==========================================
# 10. Global Variable
# ==========================================


name = "Osman"


def greet_global():
    print(name)


greet_global()


# ==========================================
# 11. Local and Global Variables
# ==========================================


name2 = "Osman"


def change_name():
    name2 = "Ahmet"
    print(name2)


change_name()

print(name2)


# ==========================================
# 12. Global Keyword
# ==========================================


counter = 0


def increase():
    global counter
    counter += 1


increase()
increase()
increase()

print(counter)


# ==========================================
# 13. Default Parameter
# ==========================================


def greet_default(name="Guest"):
    print(f"Merhaba {name}!")


greet_default()
greet_default("Osman")


# ==========================================
# 14. Multiple Parameters with Default Value
# ==========================================


def introduce_default(name, age=18):
    print(f"{name} {age} yaşında.")


introduce_default("Osman")
introduce_default("Osman", 32)


# ==========================================
# 15. Keyword Arguments
# ==========================================


def introduce_keyword(name, age, city):
    print(f"{name}, {age}, {city}")


introduce_keyword(
    city="Podgorica",
    name="Osman",
    age=32
)


# ==========================================
# 16. Positional and Keyword Arguments
# ==========================================


def introduce_mixed(name, age, city):
    print(f"{name}, {age}, {city}")


introduce_mixed(
    "Osman",
    age=32,
    city="Podgorica"
)


# ==========================================
# 17. Multiple Return Values
# ==========================================


def get_book():
    return "Python101", "Osman Bozok", 5000


book_name, author, page = get_book()

print(book_name)
print(author)
print(page)


# ==========================================
# 18. *args
# ==========================================


def add_numbers(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total


print(add_numbers(10, 20))
print(add_numbers(10, 20, 30))
print(add_numbers(1, 2, 3, 4, 5))


# ==========================================
# 19. **kwargs
# ==========================================


def show_info(**information):
    for key, value in information.items():
        print(f"{key}: {value}")


show_info(
    name="Osman",
    age=32,
    city="Podgorica"
)


# ==========================================
# 20. *args and **kwargs
# ==========================================


def show_all(*args, **kwargs):
    print("Args:")
    print(args)

    print("Kwargs:")
    print(kwargs)


show_all(
    10,
    20,
    30,
    name="Osman",
    city="Podgorica"
)


# ==========================================
# 21. Function Composition
# ==========================================


def double(number):
    return number * 2


def add_five(number):
    return number + 5


result = add_five(double(10))

print(result)


# ==========================================
# 22. Recursive Function
# ==========================================


def countdown(number):
    if number == 0:
        return

    print(number)

    countdown(number - 1)


countdown(5)


# ==========================================
# 23. Lambda Function
# ==========================================


square_lambda = lambda number: number ** 2

print(square_lambda(5))


# ==========================================
# 24. Function with List
# ==========================================


def calculate_total(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


numbers = [10, 20, 30, 40]

print(calculate_total(numbers))


# ==========================================
# 25. Function with Dictionary
# ==========================================


def print_book(book):
    print(f"Kitap: {book['name']}")
    print(f"Yazar: {book['author']}")
    print(f"Sayfa: {book['page']}")


book = {
    "name": "Python101",
    "author": "Osman Bozok",
    "page": 5000
}

print_book(book)


# ==========================================
# 26. Function with Set
# ==========================================


def find_common_books(books1, books2):
    return books1 & books2


books1 = {
    "Python101",
    "Clean Code",
    "Algorithms"
}

books2 = {
    "Python101",
    "Clean Code",
    "Computer Science"
}

common_books = find_common_books(books1, books2)

print(common_books)


# ==========================================
# 27. Docstring
# ==========================================


def calculate_average(numbers):
    """
    Verilen sayıların ortalamasını döndürür.
    """

    total = 0

    for number in numbers:
        total += number

    return total / len(numbers)


numbers = [10, 20, 30, 40]

print(calculate_average(numbers))


# ==========================================
# 28. Single Responsibility
# ==========================================


def add_book(book_list, book_name):
    book_list.append(book_name)


def remove_book(book_list, book_name):
    if book_name in book_list:
        book_list.remove(book_name)


def list_books(book_list):
    for book in book_list:
        print(book)


books = []

add_book(books, "Python101")
add_book(books, "Clean Code")
add_book(books, "Algorithms")

remove_book(books, "Clean Code")

list_books(books)