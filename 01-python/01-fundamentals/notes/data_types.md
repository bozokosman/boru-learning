# Data Types

## 1. Veri Türü Nedir?

Python'da program içerisinde farklı türlerde verilerle çalışırız.

Bir değerin veri türü, Python'un o değeri nasıl değerlendireceğini ve hangi işlemlerin yapılabileceğini belirler.

Örneğin:

```python
name = "Osman"
age = 32
height = 1.80
is_learning = True
```

Bu değişkenlerin değerleri farklı veri türlerine sahiptir.

---

## 2. `str` — String

String, metinsel verileri temsil eder.

Tek veya çift tırnak kullanılabilir:

```python
name = "Osman"
city = 'Podgorica'
```

String değerlerin türünü `type()` ile kontrol edebiliriz:

```python
print(type(name))
```

Çıktı:

```text
<class 'str'>
```

Stringler üzerinde daha sonra ayrıntılı olarak çalışacağız.

---

## 3. `int` — Integer

`int`, tam sayıları temsil eder.

```python
age = 32
page = 100
number = -5
```

Türünü kontrol edebiliriz:

```python
print(type(age))
```

Çıktı:

```text
<class 'int'>
```

Ondalıklı sayılar `int` değildir.

```python
age = 32
height = 1.80
```

Burada `age` bir `int`, `height` ise `float` değeridir.

---

## 4. `float`

`float`, ondalıklı sayıları temsil eder.

```python
height = 1.80
price = 19.99
temperature = -3.5
```

Türünü kontrol edebiliriz:

```python
print(type(height))
```

Çıktı:

```text
<class 'float'>
```

---

## 5. `bool` — Boolean

Boolean veri türü iki değer alabilir:

```python
True
False
```

Örneğin:

```python
is_learning = True
is_finished = False
```

Türünü kontrol edebiliriz:

```python
print(type(is_learning))
```

Çıktı:

```text
<class 'bool'>
```

Boolean değerler özellikle koşullarda kullanılır:

```python
is_adult = True

if is_adult:
    print("Adult")
```

`bool` konusu koşullar bölümünde daha ayrıntılı kullanılacaktır.

---

## 6. `list`

`list`, birden fazla değeri sıralı şekilde tutabilen değiştirilebilir bir veri yapısıdır.

```python
books = ["Python101", "Crime and Punishment", "The Outsider"]
```

Listenin türü:

```python
print(type(books))
```

Çıktı:

```text
<class 'list'>
```

Listeler değiştirilebilir:

```python
books.append("Les Misérables")
```

Listeler daha sonra `03_Lists` bölümünde ayrıntılı olarak incelenecektir.

---

## 7. `tuple`

`tuple`, birden fazla değeri sıralı şekilde tutabilen bir veri yapısıdır.

```python
coordinates = (10, 20)
```

Türü:

```python
print(type(coordinates))
```

Çıktı:

```text
<class 'tuple'>
```

Tuple'lar oluşturulduktan sonra elemanlarının değiştirilmesine izin vermez.

Tuple konusu ilerleyen bölümlerde daha ayrıntılı incelenecektir.

---

## 8. `dict` — Dictionary

Dictionary, verileri anahtar-değer ilişkisi içerisinde tutan bir veri yapısıdır.

```python
book = {
    "name": "Python101",
    "author": "Osman Bozok",
    "page": 100
}
```

Burada:

* `"name"` bir anahtardır.
* `"Python101"` bu anahtarın değeridir.
* `"author"` başka bir anahtardır.
* `"Osman Bozok"` onun değeridir.

Türünü kontrol edebiliriz:

```python
print(type(book))
```

Çıktı:

```text
<class 'dict'>
```

Dictionary konusu `04_Dictionaries` bölümünde ayrıntılı olarak incelenecektir.

---

## 9. `None`

`None`, Python'da bir değerin bulunmadığını veya henüz bir değer verilmediğini ifade etmek için kullanılabilir.

```python
result = None
```

Türü:

```python
print(type(result))
```

Çıktı:

```text
<class 'NoneType'>
```

`None`, `0`, `False` veya boş bir string ile aynı şey değildir.

---

## 10. `type()`

Bir değerin veya değişkenin veri türünü öğrenmek için `type()` fonksiyonunu kullanabiliriz.

```python
name = "Osman"
age = 32
height = 1.80
is_learning = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_learning))
```

Çıktı:

```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

`type()` özellikle öğrenme aşamasında bir değerin hangi türde olduğunu kontrol etmek için oldukça kullanışlıdır.

---

## 11. Veri Türlerini Birlikte Kullanmak

Bir program içerisinde farklı veri türlerini aynı anda kullanabiliriz.

```python
name = "Osman"
age = 32
height = 1.80
is_learning = True
books = ["Python101", "The Outsider"]
```

Burada:

```text
name       → str
age        → int
height     → float
is_learning → bool
books      → list
```

şeklinde farklı veri türleri kullanılmıştır.

---

## 12. Öğrenme Notu

Python'da veri türlerini ezberlemekten daha önemli olan şey, **hangi türde veriyle çalıştığımızı ve o veri üzerinde hangi işlemleri yapabileceğimizi anlamaktır.**

Örneğin:

```python
age = 32
```

ile:

```python
age = "32"
```

aynı görünseler de aynı veri türüne sahip değildirler.

İlk değer:

```python
int
```

ikinci değer:

```python
str
```

türündedir.

Bu fark, programın ilerleyen bölümlerinde işlemlerin nasıl çalışacağını doğrudan etkiler.

---

## Özet

Temel Python veri türleri:

| Tür        | Açıklama                            | Örnek               |
| ---------- | ----------------------------------- | ------------------- |
| `str`      | Metin                               | `"Osman"`           |
| `int`      | Tam sayı                            | `32`                |
| `float`    | Ondalıklı sayı                      | `1.80`              |
| `bool`     | Doğru / yanlış                      | `True`              |
| `list`     | Sıralı, değiştirilebilir koleksiyon | `[1, 2, 3]`         |
| `tuple`    | Sıralı, değiştirilemez koleksiyon   | `(1, 2, 3)`         |
| `dict`     | Anahtar-değer yapısı                | `{"name": "Osman"}` |
| `NoneType` | Değer yokluğu                       | `None`              |

Bu veri yapılarının daha ayrıntılı kullanımı ilgili Python bölümlerinde ele alınacaktır.

