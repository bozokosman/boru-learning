# Tuples

## 1. Tuple Nedir?

Tuple, Python'da birden fazla değeri tek bir yapı içerisinde saklamak için kullanılan veri tipidir.

Tuple'lar sıralıdır ve elemanlarına indeks ile erişilebilir.

    coordinates = (10, 20)

    print(coordinates)

Tuple oluştururken parantez kullanılır.

    person = ("Osman", 32, "Podgorica")

---

## 2. Tuple Indexing

Tuple elemanlarına indeks numarasıyla erişilebilir.

İndeksler `0`'dan başlar.

    person = ("Osman", 32, "Podgorica")

    print(person[0])
    print(person[1])
    print(person[2])

Negatif indeksler de kullanılabilir.

    print(person[-1])
    print(person[-2])

---

## 3. Tuple Slicing

Tuple'larda slicing kullanılabilir.

    numbers = (10, 20, 30, 40, 50)

    print(numbers[1:4])
    print(numbers[:3])
    print(numbers[2:])
    print(numbers[::-1])

Slicing sonucunda yine tuple elde edilir.

---

## 4. Tuple Immutable'dır

Tuple'ların en önemli özelliklerinden biri immutable olmalarıdır.

Yani oluşturulduktan sonra elemanları değiştirilemez.

    numbers = (10, 20, 30)

    numbers[0] = 100

Yukarıdaki işlem hata verir.

Liste ile karşılaştırıldığında:

    numbers = [10, 20, 30]

    numbers[0] = 100

Liste değiştirilebilirken tuple değiştirilemez.

---

## 5. Tuple İçerisinde Farklı Veri Tipleri

Tuple içerisinde farklı veri tipleri bulunabilir.

    person = (
        "Osman",
        32,
        95.5,
        True
    )

    print(person)

---

## 6. `len()`

Tuple içerisindeki eleman sayısını bulmak için `len()` kullanılabilir.

    numbers = (10, 20, 30, 40)

    print(len(numbers))

---

## 7. `in`

Bir elemanın tuple içerisinde bulunup bulunmadığı `in` ile kontrol edilebilir.

    numbers = (10, 20, 30, 40)

    print(20 in numbers)
    print(50 in numbers)

---

## 8. Tuple Üzerinde `for`

Tuple üzerinde `for` döngüsü ile dolaşılabilir.

    books = (
        "Python101",
        "Clean Code",
        "Computer Science"
    )

    for book in books:
        print(book)

---

## 9. Tuple Packing

Birden fazla değer parantez kullanılmadan da tuple haline getirilebilir.

    person = "Osman", 32, "Podgorica"

    print(person)
    print(type(person))

Python bu değerleri otomatik olarak tuple haline getirir.

---

## 10. Tuple Unpacking

Tuple içerisindeki değerler ayrı değişkenlere aktarılabilir.

    person = ("Osman", 32, "Podgorica")

    name, age, city = person

    print(name)
    print(age)
    print(city)

Burada değişken sayısının tuple içerisindeki eleman sayısıyla uyumlu olması gerekir.

---

## 11. Multiple Assignment

Tuple unpacking mantığı Python'da birden fazla değişkene aynı anda değer atamak için de kullanılabilir.

    name, age = "Osman", 32

    print(name)
    print(age)

Bu Python'da sık kullanılan bir özelliktir.

---

## 12. Tuple Metodları

Tuple'ların immutable olması nedeniyle sahip oldukları metod sayısı listelere göre daha azdır.

### `count()`

Belirli bir elemanın kaç kez bulunduğunu sayar.

    numbers = (10, 20, 20, 30, 20)

    print(numbers.count(20))

### `index()`

Bir elemanın ilk bulunduğu indeks numarasını döndürür.

    numbers = (10, 20, 30, 40)

    print(numbers.index(30))

---

## 13. Tuple ve List Karşılaştırması

List:

    books = ["Python101", "Clean Code"]

Tuple:

    books = ("Python101", "Clean Code")

Temel fark:

| Özellik | List | Tuple |
|---|---|---|
| Sıralı | Evet | Evet |
| İndekslenebilir | Evet | Evet |
| Slicing | Evet | Evet |
| Değiştirilebilir | Evet | Hayır |
| `append()` | Evet | Hayır |
| `remove()` | Evet | Hayır |
| `count()` | Evet | Evet |
| `index()` | Evet | Evet |

---

## 14. Tuple Ne Zaman Kullanılır?

Verilerin değiştirilmemesi gerektiği durumlarda tuple kullanılabilir.

Örneğin koordinatlar:

    coordinates = (41.0082, 28.9784)

Bir kişinin temel bilgileri:

    person = ("Osman", 32, "Podgorica")

Bir fonksiyon birden fazla değeri birlikte döndürecekse tuple kullanılabilir.

    def get_user():
        return "Osman", 32

    user = get_user()

    print(user)

---

## 15. Fonksiyondan Tuple Döndürmek

Bir fonksiyon birden fazla değer döndürebilir.

    def get_user():
        name = "Osman"
        age = 32

        return name, age

    name, age = get_user()

    print(name)
    print(age)

Burada Python aslında bir tuple döndürür ve daha sonra tuple unpacking yapılır.

---

## 16. Tuple İçerisinde Tuple

Tuple içerisinde başka tuple'lar bulunabilir.

    coordinates = (
        (10, 20),
        (30, 40),
        (50, 60)
    )

    print(coordinates[0])
    print(coordinates[0][0])

---

## 17. Özet

Tuple:

- sıralıdır
- indekslenebilir
- slicing destekler
- `for` ile dolaşılabilir
- immutable'dır
- farklı veri tiplerini saklayabilir
- `count()` ve `index()` metodlarına sahiptir
- tuple unpacking destekler

Temel tuple oluşturma:

    numbers = (10, 20, 30)

Temel tuple unpacking:

    numbers = (10, 20, 30)

    a, b, c = numbers

Tuple'ın en önemli özelliği:

    Immutable
