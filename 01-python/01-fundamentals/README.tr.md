🇬🇧 [English](README.md)

# Python Fundamentals

Bu bölüm, Python öğrenme yolunun temel yapı taşlarını içerir.

Amaç; Python syntax'ını ezberlemekten ziyade değişkenleri, veri tiplerini, kullanıcı girdilerini, operatörleri, koşulları, döngüleri ve temel string işlemlerini kullanarak küçük programlar yazabilmektir.
---

## Topics

### 01. Variables
Değişkenlerin oluşturulması, değer atanması ve değerlerinin değiştirilmesi.

Öğrenilen temel konular:
- Variable declaration
- Assignment
- Reassignment
- Variable naming
- Birden fazla değişkenle çalışma
- f-string kullanımı

**Example:**
```python
name = "Osman"
age = 32

print(f"My name is {name}. I am {age} years old.")
```

### 02. Data Types
Python'daki temel veri tipleri.

Öğrenilen temel tipler:
- str
- int
- float
- bool
- list
- tuple
- dict
- None

Ayrıca `type()` ile bir değişkenin veri tipi kontrol edildi.

### 03. Input / Output
Kullanıcıdan veri alma ve program çıktısı üretme.

Öğrenilen konular:
- `input()`
- `print()`
- `sep`
- `end`
- f-strings

**Example:**
```python
name = input("Adınızı giriniz: ")

print(f"Merhaba, {name}.")
```

### 04. Type Conversion
Bir verinin başka bir veri tipine dönüştürülmesi.

Temel dönüşüm fonksiyonları:
- `int()`
- `float()`
- `str()`
- `bool()`

Özellikle `input()` fonksiyonunun her zaman str döndürdüğü ve matematiksel işlemler için uygun type conversion yapılması öğrenildi.

**Example:**
```python
age = int(input("Yaşınızı giriniz: "))

print(age + 5)
```
Ayrıca `bool()` dönüşümünde 0 değerinin False, sıfır dışındaki sayıların ise True olması test edildi.

### 05. Operators
Python'daki temel operatörler.

**Arithmetic Operators**
- `+`
- `-`
- `*`
- `/`
- `//`
- `%`
- `**`

**Comparison Operators**
- `>`
- `<`
- `>=`
- `<=`
- `==`
- `!=`

**Logical Operators**
- `and`
- `or`
- `not`

Ayrıca operatör önceliği ve parantez kullanımının işlemlerin sonucunu nasıl değiştirdiği çalışıldı.

### 06. Conditionals
Programın belirli koşullara göre farklı davranmasını sağlamak için conditional statements kullanıldı.

Temel yapılar:
- `if`
- `elif`
- `else`

Öğrenilen konular:
- Tek koşul
- Birden fazla koşul
- Nested conditions
- `and`
- `or`
- `not`
- Boolean ifadeler
- Koşullu program akışı

**Example:**
```python
if age >= 18:
    print("Giriş yapabilirsiniz.")
else:
    print("Giriş yapamazsınız.")
```

### 07. Loops
Kodun belirli işlemleri tekrar tekrar gerçekleştirmesi için loops kullanıldı.

Öğrenilen yapılar:
- `for`
- `while`
- `range()`
- `break`
- `else` ile `for`
- Koşullu döngüler

**Example:**
```python
for i in range(1, 11):
    print(i)
```
Ayrıca listeler üzerinde dolaşma ve döngü içerisinde koşul kullanımı çalışıldı.

### 08. Strings
String veri tipi ve temel string işlemleri çalışıldı.

Öğrenilen metod ve işlemler:
- Indexing
- Slicing
- `strip()`
- `lower()`
- `upper()`
- `capitalize()`
- `replace()`
- `split()`
- `join()`
- `in`
- String üzerinde for döngüsü
- f-strings

**Example:**
```python
book = "  Python101  "

book = book.strip().lower()

print(book)
```
Ayrıca string → list dönüşümü için `split()` ve list → string dönüşümü için `join()` kullanıldı.

---

## Learning Structure
Her konu üç bölüm halinde arşivlenmiştir:

```text
Topic
├── Notes
├── Examples
└── Exercises
```

- **Notes:** Konunun temel kavramlarını ve syntax'ını açıklar.
- **Examples:** Öğrenilen syntax'ın çalışan örneklerini içerir.
- **Exercises:** Konuyu kullanarak problem çözme pratiği yapılır.
