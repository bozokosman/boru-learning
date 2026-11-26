myTuple = ("Python", "C++", "Go", "Rust")
print(myTuple[0])
print(myTuple[-1])
print(myTuple[1])

myTuple2 = (10, 20, 30, 40, 50, 60, 70)
print(myTuple2[:3])
print(myTuple2[:3:-1])
print(myTuple2[2:5])
print(myTuple2[::-1])

myTuple3 = (10, 20, 30, 20, 40, 20, 50)
print(myTuple3.count(20))
print(myTuple3.index(40))

myTuple4 = ("Osman", 32, "Podgorica")
name, age, city = myTuple4
print(f"Ben {name}, {age} yaşındayım ve {city} şehrinde yaşıyorum.")

myTuple5 = (41.9981, 21.4254)
latitude, longitude = myTuple5
print(latitude)
print(longitude)

myTuple6 = ("Python101", "Osman Bozok", 5000)
book_name, author, page = myTuple6
print(f"Kitap: {book_name}\nYazar: {author}\nSayfa: {page}")

def get_book():
    return myTuple7 = ("Python101", "Osman Bozok", 5000)
book_name, author, page = get_book()
print(book_name, author, page)
# Correct way
# def get_book():
#     return "Python101", "Osman Bozok", 5000
# 
# book_name, author, page = get_book()
# print(book_name)
# print(author)
# print(page)
