book = input("Kitap adını giriniz: ")
new_book = book.strip().lower()
print(new_book)


string = "Python is a powerful programming language"
word = input("Bir kelime giriniz: ")
if word in string:
    print("Bulundu.")
else:
    print("Bulunamadı.")

string2 = "Python,Java,C++,Go,Rust"
new_string = string2.split(",")
for word in new_string:
    print(word)
    

liste = ["Python", "C++", "Go", "Rust"]
new_liste = " | ".join(liste)
print(new_liste)

book_name = input("Kitap adını giriniz: ").strip().capitalize()
author_name = input("Yazar adını giriniz: ").strip().capitalize()
print(f"Kitap : {book_name}\nYazar : {author_name}")