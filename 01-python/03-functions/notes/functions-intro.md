# Functions

## 1. Function Nedir?

Function, belirli bir işi gerçekleştirmek için yazılan ve gerektiğinde tekrar kullanılabilen kod bloğudur.

Fonksiyonlar `def` anahtar kelimesiyle tanımlanır.

    def greet():
        print("Hello!")

Fonksiyonu çalıştırmak için fonksiyon adı parantezlerle çağrılır.

    greet()

---

## 2. Parameters

Fonksiyonlara dışarıdan bilgi göndermek için parameter kullanılabilir.

    def greet(name):
        print(f"Hello, {name}!")

    greet("Osman")

Burada `name` parametredir.

---

## 3. Multiple Parameters

Bir fonksiyon birden fazla parameter alabilir.

    def introduce(name, age, city):
        print(f"My name is {name}.")
        print(f"I am {age} years old.")
        print(f"I live in {city}.")

    introduce("Osman", 32, "Podgorica")

---

## 4. `return`

Fonksiyon içerisindeki sonucu dışarıya göndermek için `return` kullanılır.

    def add(number1, number2):
        return number1 + number2

    result = add(10, 20)

    print(result)

`return` fonksiyonu sonlandırır ve belirtilen değeri çağrıldığı yere gönderir.

---

## 5. `print()` ve `return` Farkı

`print()` sonucu ekrana yazdırır.

    def add(number1, number2):
        print(number1 + number2)

`return` ise sonucu fonksiyonun dışına gönderir.

    def add(number1, number2):
        return number1 + number2

Bu nedenle dönen değer başka işlemlerde kullanılabilir.

    result = add(10, 20)
    print(result * 2)

---

## 6. Local Variables

Fonksiyon içerisinde oluşturulan değişkenler varsayılan olarak local değişkenlerdir.

    def calculate():
        number = 10
        print(number)

    calculate()

Fonksiyon dışında doğrudan `number` değişkenine erişilemez.

---

## 7. Global Variables

Fonksiyon dışında tanımlanan değişkenler global scope içerisinde bulunur.

    name = "Osman"

    def greet():
        print(name)

    greet()

Fonksiyon global değişkene erişebilir.

---

## 8. `global`

Bir fonksiyon içerisinden global bir değişkenin değerini değiştirmek için `global` kullanılabilir.

    counter = 0

    def increase():
        global counter
        counter += 1

    increase()

    print(counter)

Global değişkenleri gereksiz yere değiştirmekten kaçınmak genellikle daha sağlıklı bir tasarımdır.

---

## 9. Default Parameters

Fonksiyon parametrelerine varsayılan değer verilebilir.

    def greet(name="Guest"):
        print(f"Hello, {name}!")

    greet()
    greet("Osman")

Argüman verilmezse varsayılan değer kullanılır.

---

## 10. Keyword Arguments

Fonksiyon çağrılırken parametrelerin isimleri belirtilerek değer gönderilebilir.

    def introduce(name, age):
        print(f"{name} is {age} years old.")

    introduce(age=32, name="Osman")

Bu yöntem parametrelerin sırasına bağımlılığı azaltabilir.

---

## 11. Positional Arguments

Fonksiyon çağrılırken değerler parametrelerin sırasına göre gönderilebilir.

    def introduce(name, age):
        print(name)
        print(age)

    introduce("Osman", 32)

Burada `"Osman"` `name` parametresine, `32` ise `age` parametresine gönderilir.

---

## 12. `*args`

Bir fonksiyona değişken sayıda positional argument göndermek için `*args` kullanılabilir.

    def total(*numbers):
        result = 0

        for number in numbers:
            result += number

        return result

    print(total(10, 20))
    print(total(10, 20, 30, 40))

`args` içerisinde gönderilen değerler tuple olarak bulunur.

---

## 13. `**kwargs`

Bir fonksiyona değişken sayıda keyword argument göndermek için `**kwargs` kullanılabilir.

    def show_info(**info):
        for key, value in info.items():
            print(f"{key}: {value}")

    show_info(name="Osman", age=32, city="Podgorica")

`kwargs` içerisinde gönderilen değerler dictionary olarak bulunur.

---

## 14. Function Composition

Bir fonksiyonun sonucu başka bir fonksiyona gönderilebilir.

    def double(number):
        return number * 2

    def add_five(number):
        return number + 5

    result = add_five(double(10))

    print(result)

Fonksiyonlar bu şekilde birlikte kullanılabilir.

---

## 15. Fonksiyon İçerisinde `if`

Fonksiyon içerisinde koşul ifadeleri kullanılabilir.

    def check_age(age):
        if age >= 18:
            return "Giriş yapılabilir."
        else:
            return "Giriş yapılamaz."

    print(check_age(20))

---

## 16. Fonksiyon İçerisinde Loop

Fonksiyon içerisinde döngüler de kullanılabilir.

    def print_books(books):
        for book in books:
            print(book)

    books = ["Python101", "Clean Code", "Computer Science"]

    print_books(books)

---

## 17. Fonksiyon ve Listeler

Fonksiyonlara liste gönderilebilir.

    def find_even_numbers(numbers):
        even_numbers = []

        for number in numbers:
            if number % 2 == 0:
                even_numbers.append(number)

        return even_numbers

    numbers = [1, 2, 3, 4, 5, 6]

    result = find_even_numbers(numbers)

    print(result)

---

## 18. Fonksiyon ve Dictionary

Fonksiyonlara dictionary gönderilebilir.

    def print_book(book):
        print(f"Name: {book['name']}")
        print(f"Author: {book['author']}")

    book = {
        "name": "Python101",
        "author": "Osman Bozok"
    }

    print_book(book)

Bu yapı daha sonra OOP içerisindeki method mantığına bağlanacaktır.

---

## 19. Fonksiyonların Avantajları

Fonksiyonlar:

- Kod tekrarını azaltır.
- Kodun okunabilirliğini artırır.
- Büyük problemleri küçük parçalara ayırmayı sağlar.
- Kodun tekrar kullanılmasını sağlar.
- Test etmeyi kolaylaştırır.
- Programın sorumluluklarını ayırmaya yardımcı olur.

---

## 20. Özet

Temel function yapısı:

    def function_name(parameters):
        # işlemler
        return result

Fonksiyonlarda önemli kavramlar:

- `def`
- parameter
- argument
- `return`
- local scope
- global scope
- default parameter
- positional argument
- keyword argument
- `*args`
- `**kwargs`

Fonksiyonlar Python'da kodun tekrar kullanılabilir ve yönetilebilir parçalara ayrılmasını sağlar.
