# Type Conversion

## 1. Type Conversion Nedir?

Type conversion, bir verinin veri tipini başka bir veri tipine dönüştürme işlemidir.

Python'da özellikle kullanıcıdan alınan verilerle çalışırken sık kullanılır.

    age = input("Yaşınızı giriniz: ")

`input()` fonksiyonu kullanıcıdan aldığı değeri **string** olarak döndürür.

Bu nedenle sayısal işlem yapmak istediğimizde dönüşüm yapmamız gerekir.

    age = int(input("Yaşınızı giriniz: "))

---

## 2. `int()`

Bir değeri integer yani tam sayıya dönüştürmek için `int()` kullanılır.

    number = "32"

    number = int(number)

    print(number)
    print(type(number))

String sayısal bir değer içeriyorsa `int()` ile dönüştürülebilir.

    age = int(input("Yaşınızı giriniz: "))

---

## 3. `float()`

Bir değeri ondalıklı sayıya dönüştürmek için `float()` kullanılır.

    height = "95.5"

    height = float(height)

    print(height)
    print(type(height))

Kullanıcıdan ondalıklı bir değer alırken de kullanılabilir.

    height = float(input("Boyunuzu giriniz: "))

---

## 4. `str()`

Bir değeri string'e dönüştürmek için `str()` kullanılır.

    age = 32

    age = str(age)

    print(age)
    print(type(age))

Bir sayıyı metinsel bir ifadeyle birleştirmek gerektiğinde kullanılabilir.

    age = 32

    message = "Yaşım: " + str(age)

    print(message)

f-string kullanıldığında ise çoğu durumda açıkça `str()` yazmaya gerek kalmaz.

    age = 32

    print(f"Yaşım: {age}")

---

## 5. `bool()`

Bir değeri boolean yani `True` veya `False` değerine dönüştürmek için `bool()` kullanılabilir.

    print(bool(1))
    print(bool(0))

Sonuç:

    True
    False

Genel olarak sıfır değerleri ve boş yapılar `False`, sıfır olmayan değerler ve dolu yapılar `True` olarak değerlendirilir.

Örneğin:

    print(bool(""))
    print(bool("Python"))

Sonuç:

    False
    True

---

## 6. Kullanıcı Girdisi ve Type Conversion

`input()` her zaman string döndürür.

    age = input("Yaşınızı giriniz:")

    print(type(age))

Bu nedenle matematiksel işlem yapmak için dönüşüm gerekir.

    age = int(input("Yaşınızı giriniz: "))

    print(age + 1)

Ondalık değerlerde:

    height = float(input("Boyunuzu giriniz: "))

    print(height)

---

## 7. Bir Türden Başka Bir Türe Dönüşüm

Bazı temel dönüşümler:

    number = 32

    print(str(number))
    print(float(number))
    print(bool(number))

Bir string sayı da farklı türlere dönüştürülebilir.

    number = "32"

    print(int(number))
    print(float(number))

---

## 8. Geçersiz Dönüşümler

Her veri her tipe dönüştürülemez.

Örneğin:

    number = "Osman"

    number = int(number)

Bu işlem hata verir çünkü `"Osman"` geçerli bir integer değildir.

Benzer şekilde:

    number = "Python"

    number = float(number)

işlemi de hata verir.

Bu tür hataları daha sonra `Exceptions` konusunda ele alacağız.

---

## 9. `input()` ile Birlikte Kullanım

Kullanıcıdan farklı türlerde veri alınabilir.

    name = input("Adınızı giriniz: ")
    age = int(input("Yaşınızı giriniz: "))
    height = float(input("Boyunuzu giriniz: "))

    print(type(name))
    print(type(age))
    print(type(height))

Burada:

- `name` → `str`
- `age` → `int`
- `height` → `float`

olur.

---

## 10. Type Conversion ve İşlemler

Dönüşüm yapılmadan:

    number1 = input("Birinci sayıyı giriniz: ")
    number2 = input("İkinci sayıyı giriniz: ")

    print(number1 + number2)

Burada sayılar matematiksel olarak toplanmaz.

Örneğin kullanıcı `10` ve `20` girerse sonuç:

    1020

olur.

Çünkü iki string birleştirilmiştir.

Doğru kullanım:

    number1 = int(input("Birinci sayıyı giriniz: "))
    number2 = int(input("İkinci sayıyı giriniz: "))

    print(number1 + number2)

Sonuç:

    30

---

## 11. Explicit Conversion

Programcının dönüşümü açıkça yapmasına explicit conversion denir.

    age = "32"

    age = int(age)

Python burada bizim açıkça istediğimiz dönüşümü gerçekleştirir.

---

## 12. Özet

Temel type conversion fonksiyonları:

| Fonksiyon | Dönüşüm |
|---|---|
| `int()` | Integer |
| `float()` | Float |
| `str()` | String |
| `bool()` | Boolean |

Özellikle kullanıcıdan veri alırken `input()` ile birlikte type conversion kullanımı çok yaygındır.

    age = int(input("Yaşınızı giriniz: "))

    height = float(input("Boyunuzu giriniz: "))

    name = str(input("Adınızı giriniz: "))

Ancak `input()` zaten string döndürdüğü için aşağıdaki kullanımda `str()` yazmak zorunlu değildir:

    name = input("Adınızı giriniz: ")

---

## Özet Mantık

Kullanıcıdan gelen veri:

    input()
        ↓
    str
        ↓
    int() / float() / bool()
        ↓
    İhtiyaç duyulan veri tipi
