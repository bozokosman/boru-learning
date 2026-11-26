# Dictionaries

## 1. Dictionary Nedir?

Python'da `dictionary`, verileri **key-value (anahtar-değer)** çiftleri halinde saklayan bir veri yapısıdır.

```python
book = {
    "name": "Python101",
    "author": "Osman Bozok",
    "page": 5000,
    "category": "Programming"
}
```

Burada:

* `"name"` → key
* `"Python101"` → value
* `"author"` → key
* `"Osman Bozok"` → value

Dictionary'de verilere indeks numarasıyla değil, key üzerinden erişilir.

---

## 2. Dictionary'den Veri Okuma

```python
book = {
    "name": "Python101",
    "author": "Osman Bozok",
    "page": 5000
}

print(book["name"])
print(book["author"])
print(book["page"])
```

Sonuç:

```text
Python101
Osman Bozok
5000
```

---

## 3. Yeni Veri Eklemek

Dictionary'e yeni bir key-value çifti eklenebilir.

```python
book = {
    "name": "Python101",
    "author": "Osman Bozok"
}

book["page"] = 5000

print(book)
```

---

## 4. Mevcut Veriyi Değiştirmek

Var olan bir key'e yeni değer atanırsa mevcut değer değiştirilir.

```python
book = {
    "name": "Python101",
    "page": 5000
}

book["page"] = 6000

print(book)
```

Burada yeni bir `"page"` oluşturulmaz. Mevcut `"page"` değerinin üzerine yazılır.

---

## 5. `get()`

Bir key'e erişmek için `get()` kullanılabilir.

```python
book = {
    "name": "Python101",
    "author": "Osman Bozok"
}

print(book.get("name"))
```

Key bulunamazsa `get()` varsayılan olarak `None` döndürür.

```python
print(book.get("page"))
```

Sonuç:

```text
None
```

İstenirse alternatif bir değer verilebilir:

```python
print(book.get("page", "Sayfa bilgisi yok"))
```

---

## 6. `in`

Bir key'in dictionary içerisinde bulunup bulunmadığını kontrol etmek için `in` kullanılabilir.

```python
book = {
    "name": "Python101",
    "author": "Osman Bozok"
}

print("name" in book)
print("page" in book)
```

Sonuç:

```text
True
False
```

Dictionary üzerinde `in` kullanıldığında varsayılan olarak **key'ler kontrol edilir**.

---

## 7. Key ile Value Arasındaki Fark

```python
book = {
    "name": "Python101",
    "author": "Osman Bozok"
}
```

Burada:

```python
"name" in book
```

şunu kontrol eder:

> `"name"` key olarak var mı?

Value kontrol etmek için:

```python
"Python101" in book.values()
```

kullanılabilir.

---

## 8. `keys()`

Dictionary'deki bütün key'leri almak için `keys()` kullanılır.

```python
book = {
    "name": "Python101",
    "author": "Osman Bozok",
    "page": 5000
}

print(book.keys())
```

---

## 9. `values()`

Dictionary'deki bütün value'ları almak için `values()` kullanılır.

```python
print(book.values())
```

---

## 10. `items()`

Key ve value çiftlerini birlikte almak için `items()` kullanılır.

```python
print(book.items())
```

Özellikle `for` döngülerinde kullanışlıdır.

```python
for key, value in book.items():
    print(key, value)
```

Sonuç:

```text
name Python101
author Osman Bozok
page 5000
```

---

## 11. Dictionary Üzerinde `for`

Dictionary üzerinde doğrudan `for` kullanılırsa key'ler üzerinde dolaşılır.

```python
book = {
    "name": "Python101",
    "author": "Osman Bozok",
    "page": 5000
}

for key in book:
    print(key)
```

Value'lara ulaşmak için:

```python
for key in book:
    print(book[key])
```

Key ve value'ları birlikte almak için:

```python
for key, value in book.items():
    print(f"{key}: {value}")
```

---

## 12. Veri Silmek

`del` ile belirli bir key-value çifti silinebilir.

```python
book = {
    "name": "Python101",
    "author": "Osman Bozok",
    "page": 5000
}

del book["page"]

print(book)
```

---

## 13. `pop()`

`pop()` belirli bir key'i dictionary'den kaldırır ve value'yu geri döndürür.

```python
book = {
    "name": "Python101",
    "author": "Osman Bozok",
    "page": 5000
}

page = book.pop("page")

print(page)
print(book)
```

---

## 14. `clear()`

`clear()` dictionary'deki bütün verileri siler.

```python
book = {
    "name": "Python101",
    "author": "Osman Bozok"
}

book.clear()

print(book)
```

Sonuç:

```text
{}
```

---

## 15. Dictionary Uzunluğu

`len()` dictionary içerisindeki key-value çiftlerinin sayısını verir.

```python
book = {
    "name": "Python101",
    "author": "Osman Bozok",
    "page": 5000
}

print(len(book))
```

Sonuç:

```text
3
```

---

## 16. İç İçe Dictionary

Dictionary value olarak başka bir dictionary tutabilir.

```python
library = {
    "book1": {
        "name": "Python101",
        "author": "Osman Bozok"
    },
    "book2": {
        "name": "Clean Code",
        "author": "Robert C. Martin"
    }
}
```

Bir değere birden fazla key üzerinden erişilebilir:

```python
print(library["book1"]["name"])
```

---

## 17. Dictionary Listesi

Bir liste içerisinde dictionary'ler tutulabilir.

```python
books = [
    {
        "name": "Python101",
        "author": "Osman Bozok"
    },
    {
        "name": "Clean Code",
        "author": "Robert C. Martin"
    }
]
```

Bu yapı Mini Library projemizin **eski dictionary tabanlı yaklaşımına** benzer.

Liste üzerinde dolaşabiliriz:

```python
for book in books:
    print(book["name"])
    print(book["author"])
```

Burada:

* `books` → dictionary'leri tutan liste
* `book` → o anki dictionary
* `book["name"]` → kitabın adı

---

## 18. Dictionary ve OOP Arasındaki Bağlantı

Eski sistemimizde bir kitabı dictionary olarak temsil edebiliyorduk:

```python
book = {
    "name": "Python101",
    "author": "Osman Bozok",
    "page": 5000,
    "category": "Programming"
}
```

Daha sonra OOP öğrenirken aynı kavramı `Book` class'ına taşıdık:

```python
class Book:
    def __init__(self, name, author, page, category):
        self.name = name
        self.author = author
        self.page = page
        self.category = category
```

Böylece:

```python
book["name"]
```

yerine:

```python
book.name
```

kullanabiliriz.

Bu iki yapı aynı şey değildir. Ancak aynı veriyi farklı bir modelleme yaklaşımıyla temsil ederler.

Dictionary veri tutmak için oldukça kullanışlıdır.

Class ve nesneler ise veriyi **davranışlarla birlikte modellememize** olanak sağlar.

---

## Özet

Dictionary:

```python
{
    "key": "value"
}
```

mantığıyla çalışır.

Temel işlemler:

| İşlem                     | Amaç                                  |
| ------------------------- | ------------------------------------- |
| `dictionary[key]`         | Değere erişmek                        |
| `dictionary[key] = value` | Veri eklemek veya değiştirmek         |
| `get()`                   | Güvenli şekilde değer almak           |
| `keys()`                  | Key'leri almak                        |
| `values()`                | Value'ları almak                      |
| `items()`                 | Key-value çiftlerini almak            |
| `in`                      | Key kontrolü                          |
| `del`                     | Veri silmek                           |
| `pop()`                   | Veriyi çıkarıp value'yu almak         |
| `clear()`                 | Dictionary'i temizlemek               |
| `len()`                   | Key-value çiftlerinin sayısını bulmak |

Dictionary'ler özellikle yapılandırılmış verileri temsil etmek için kullanışlıdır.

Liste + dictionary kombinasyonu:

```python
books = [
    {"name": "Python101", "author": "Osman Bozok"},
    {"name": "Clean Code", "author": "Robert C. Martin"}
]
```

Python'da çok yaygın bir veri modelidir.

Daha sonra bu yapıların class ve nesnelere dönüştürülmesiyle OOP yaklaşımına geçilebilir.

