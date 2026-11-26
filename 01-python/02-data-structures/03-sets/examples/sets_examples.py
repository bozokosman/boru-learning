# 1. Basic Set

numbers = {10, 20, 30, 40}

print(numbers)
print(type(numbers))


# 2. Duplicate values

numbers2 = {10, 20, 20, 30, 30, 30}

print(numbers2)


# 3. Empty Set

empty_set = set()

print(empty_set)
print(type(empty_set))


# 4. Add

books = {"Python101", "Clean Code"}

books.add("Computer Science")

print(books)


# 5. Update

books.update({
    "The Pragmatic Programmer",
    "Developer101"
})

print(books)


# 6. Remove

books.remove("Clean Code")

print(books)


# 7. Discard

books.discard("C++")

print(books)


# 8. Pop

removed_book = books.pop()

print(f"Çıkarılan kitap: {removed_book}")
print(books)


# 9. Membership

print("Python101" in books)
print("C++" in books)


# 10. Length

print(len(books))


# 11. Loop

for book in books:
    print(f"Kitap: {book}")


# 12. Union

python_books = {
    "Python101",
    "Python Advanced",
    "Developer101"
}

programming_books = {
    "Clean Code",
    "Python101",
    "C++"
}

all_books = python_books.union(programming_books)

print(all_books)


# Union operator

all_books2 = python_books | programming_books

print(all_books2)


# 13. Intersection

python_books = {
    "Python101",
    "Clean Code",
    "Python Advanced"
}

programming_books = {
    "Python101",
    "Clean Code",
    "C++"
}

common_books = python_books.intersection(programming_books)

print(common_books)


# Intersection operator

common_books2 = python_books & programming_books

print(common_books2)


# 14. Difference

python_books = {
    "Python101",
    "Clean Code",
    "Python Advanced"
}

programming_books = {
    "Python101",
    "C++"
}

python_only = python_books.difference(programming_books)

print(python_only)


# Difference operator

python_only2 = python_books - programming_books

print(python_only2)


# 15. Symmetric Difference

set1 = {1, 2, 3}
set2 = {3, 4, 5}

different_values = set1.symmetric_difference(set2)

print(different_values)


# Symmetric difference operator

different_values2 = set1 ^ set2

print(different_values2)


# 16. Subset

small = {1, 2}
large = {1, 2, 3, 4}

print(small.issubset(large))


# 17. Superset

print(large.issuperset(small))


# 18. Disjoint

set3 = {1, 2, 3}
set4 = {4, 5, 6}

print(set3.isdisjoint(set4))


# 19. List -> Set

numbers_list = [
    10,
    20,
    20,
    30,
    30,
    40
]

unique_numbers = set(numbers_list)

print(unique_numbers)


# 20. Set -> List

numbers_set = {10, 20, 30}

numbers_list = list(numbers_set)

print(numbers_list)


# 21. Set vs Dictionary

my_set = {
    "Python101",
    "Clean Code"
}

my_dictionary = {
    "name": "Python101",
    "author": "Osman Bozok"
}

print(my_set)
print(my_dictionary)


# 22. Clear

temporary_set = {1, 2, 3, 4}

temporary_set.clear()

print(temporary_set)