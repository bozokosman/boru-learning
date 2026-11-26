# Tuple oluşturma
person = ("Osman", 32, "Podgorica")

print(person)
print(type(person))


# Indexing
print(person[0])
print(person[1])
print(person[-1])


# Slicing
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])


# Farklı veri tipleri
data = ("Osman", 32, 95.5, True)

for value in data:
    print(value, type(value))


# len()
print(len(numbers))


# in
print(20 in numbers)
print(100 in numbers)


# for loop
books = (
    "Python101",
    "Clean Code",
    "Computer Science",
    "Crime and Punishment"
)

for book in books:
    print(book)


# count()
numbers2 = (10, 20, 20, 30, 20)

print(numbers2.count(20))


# index()
print(numbers2.index(30))


# Tuple packing
user = "Osman", 32, "Podgorica"

print(user)
print(type(user))


# Tuple unpacking
name, age, city = user

print(name)
print(age)
print(city)


# Multiple assignment
name, age = "Osman", 32

print(name)
print(age)


# Function returning a tuple
def get_user():
    return "Osman", 32


user_info = get_user()

print(user_info)
print(type(user_info))


# Function return + unpacking
name, age = get_user()

print(name)
print(age)


# Nested tuples
coordinates = (
    (10, 20),
    (30, 40),
    (50, 60)
)

print(coordinates)
print(coordinates[0])
print(coordinates[0][0])