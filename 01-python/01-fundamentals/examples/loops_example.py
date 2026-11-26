# for + range()

for number in range(5):
    print(number)


# range(start, stop)

for number in range(2, 6):
    print(number)


# range(start, stop, step)

for number in range(0, 10, 2):
    print(number)


# for + list

books = ["Python101", "Computer Science", "Developer101"]

for book in books:
    print(book)


# for + string

name = "Osman"

for letter in name:
    print(letter)


# for + if

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number % 2 == 0:
        print(number)


# while

number = 0

while number < 5:
    print(number)
    number += 1


# while + input

number = int(input("Bir sayı giriniz: "))

while number != 0:
    print(f"Girdiğiniz sayı: {number}")
    number = int(input("Başka bir sayı giriniz: "))


# break

for number in range(10):
    if number == 5:
        break

    print(number)


# continue

for number in range(5):
    if number == 2:
        continue

    print(number)


# nested loops

for i in range(3):
    for j in range(2):
        print(i, j)


# Library example

books = [
    "Python101",
    "Crime and Punishment",
    "Les Misérables",
    "The Outsider"
]

for book in books:
    print(f"Kitap: {book}")