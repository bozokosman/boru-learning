# Loops

## 1. Döngüler Nedir?

Döngüler, aynı veya benzer işlemleri birden fazla kez çalıştırmak için kullanılır.

Örneğin bir işlemi 5 kez yapmak istersek aynı kodu 5 kez yazmak yerine bir döngü kullanabiliriz.

Python'da temel olarak iki döngü yapısı vardır:

* `for`
* `while`

---

## 2. `for` Döngüsü

`for`, bir koleksiyonun veya belirli bir aralığın elemanları üzerinde sırayla işlem yapmak için kullanılır.

```python
for number in range(5):
    print(number)
```

Çıktı:

```text
0
1
2
3
4
```

Burada `range(5)` 0'dan başlayarak 5'e kadar olan değerleri üretir. `5` dahil değildir.

---

## 3. `range()`

`range()` özellikle belirli sayıda tekrar yapmak gerektiğinde kullanılır.

### Tek parametre

```python
for number in range(5):
    print(number)
```

Sonuç:

```text
0
1
2
3
4
```

### Başlangıç ve bitiş

```python
for number in range(2, 6):
    print(number)
```

Sonuç:

```text
2
3
4
5
```

Başlangıç değeri dahil edilir, bitiş değeri dahil edilmez.

### Adım değeri

```python
for number in range(0, 10, 2):
    print(number)
```

Sonuç:

```text
0
2
4
6
8
```

Buradaki `2`, her adımda kaç değer ilerlenmesi gerektiğini belirtir.

---

## 4. Koleksiyonlar Üzerinde `for`

`for` yalnızca sayılarla kullanılmaz.

Bir liste içerisindeki elemanları sırayla alabiliriz:

```python
books = ["Python101", "Computer Science", "Developer101"]

for book in books:
    print(book)
```

Her döngü turunda `book` değişkeni listenin bir elemanını temsil eder.

---

## 5. String Üzerinde `for`

Stringler de karakterlerden oluşan iterable yapılardır.

```python
name = "Osman"

for letter in name:
    print(letter)
```

Sonuç:

```text
O
s
m
a
n
```

Döngü string içerisindeki karakterleri sırayla ele alır.

---

## 6. `while` Döngüsü

`while`, verilen koşul `True` olduğu sürece çalışır.

```python
number = 0

while number < 5:
    print(number)
    number += 1
```

Sonuç:

```text
0
1
2
3
4
```

Burada her döngü turunda `number` artırılır.

Koşul bir noktada `False` olduğunda döngü sona erer.

---

## 7. Sonsuz Döngü

`while` döngüsünde koşulun hiçbir zaman `False` olmamasına dikkat edilmelidir.

Örneğin:

```python
number = 0

while number < 5:
    print(number)
```

Burada `number` hiçbir zaman değişmediği için koşul sürekli `True` kalır.

Bu bir sonsuz döngü oluşturur.

Bu nedenle `while` kullanırken döngünün ne zaman sona ereceğini düşünmek önemlidir.

---

## 8. `break`

`break`, döngüyü bulunduğu noktada tamamen sonlandırır.

```python
for number in range(10):
    if number == 5:
        break

    print(number)
```

Sonuç:

```text
0
1
2
3
4
```

`number` 5 olduğunda `break` çalışır ve döngü sona erer.

---

## 9. `continue`

`continue`, mevcut döngü turunun geri kalanını atlar ve bir sonraki tura geçer.

```python
for number in range(5):
    if number == 2:
        continue

    print(number)
```

Sonuç:

```text
0
1
3
4
```

`2` yazdırılmaz çünkü `continue` o turu atlar.

---

## 10. `for` ve `if` Birlikte

Döngüler koşullarla birlikte kullanılabilir.

```python
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number % 2 == 0:
        print(number)
```

Burada listedeki her sayı kontrol edilir.

`%` operatörü sayesinde çift sayılar bulunur.

Sonuç:

```text
2
4
```

---

## 11. `while` ve Kullanıcı Girdisi

`while`, kullanıcıdan belirli bir koşul sağlanana kadar veri almak için kullanılabilir.

```python
number = int(input("Bir sayı giriniz: "))

while number != 0:
    print(f"Girdiğiniz sayı: {number}")
    number = int(input("Başka bir sayı giriniz: "))
```

Kullanıcı `0` girdiğinde döngü sona erer.

Bu yapı kullanıcıdan sürekli veri alınan programların temelini oluşturur.

---

## 12. İç İçe Döngüler

Bir döngünün içerisinde başka bir döngü bulunabilir.

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

İçteki döngü, dıştaki döngünün her turunda çalışır.

İç içe döngüler özellikle daha karmaşık veri yapıları ve algoritmalarda kullanılabilir.

---

## 13. Döngü Değişkeni

Döngü içerisindeki değişken her turda farklı bir değeri temsil eder.

```python
books = ["Python101", "Clean Code", "Computer Science"]

for book in books:
    print(book)
```

İlk turda:

```text
book → "Python101"
```

İkinci turda:

```text
book → "Clean Code"
```

Üçüncü turda:

```text
book → "Computer Science"
```

Burada `book` değişkeninin adı özel değildir. İhtiyaca göre farklı bir isim kullanılabilir.

```python
for item in books:
    print(item)
```

Önemli olan değişkenin döngü içerisindeki rolüdür.

---

## 14. Döngülerde Liste Değiştirmek

Bir liste üzerinde döngü kurarken aynı listeyi döngü içerisinde değiştirmek dikkat gerektirir.

Örneğin:

```python
books = ["A", "B", "C"]

for book in books:
    if book == "B":
        books.remove(book)
```

Bu tür işlemler bazı durumlarda beklenmeyen sonuçlara yol açabilir.

Liste üzerinde işlem yaparken neyin değiştiğini ve döngünün hangi elemanlar üzerinde ilerlediğini anlamak önemlidir.

Bu konu daha ileri veri yapıları ve programlama tekniklerinde tekrar ele alınacaktır.

---

## 15. Döngüler ve Program Mantığı

Döngülerin temel amacı yalnızca aynı kodu tekrar çalıştırmak değildir.

Asıl önemli fikir:

> Bir veri grubunun veya tekrar eden bir işlemin üzerinde sistematik olarak çalışabilmek.

Örneğin kütüphanemizdeki kitapları düşünelim:

```python
for book in library.books:
    print(book.info())
```

Burada kütüphanedeki her `Book` nesnesi sırayla ele alınabilir.

Daha sonra bu yapı:

* kitap arama,
* belirli kategorideki kitapları bulma,
* kitapları filtreleme,
* kitap sayısını hesaplama,
* kitapları sıralama

gibi işlemlerin temelini oluşturacaktır.

---

## 16. `for` ve `while` Ne Zaman Kullanılır?

Genel olarak:

### `for`

Elimizde üzerinde dolaşacağımız bir koleksiyon veya belirli bir tekrar aralığı olduğunda kullanışlıdır.

```python
for book in books:
    print(book)
```

### `while`

Bir koşul doğru olduğu sürece devam etmek istediğimiz durumlarda kullanışlıdır.

```python
while user_input != "q":
    user_input = input("Komut: ")
```

Bu kesin bir kural değildir. Aynı problem bazen iki farklı döngüyle de çözülebilir.

Önemli olan problemin mantığını doğru ifade eden yapıyı seçmektir.

---

## Özet

Python'daki temel döngü yapıları:

| Yapı       | Görevi                                                           |
| ---------- | ---------------------------------------------------------------- |
| `for`      | Bir iterable üzerinde dolaşmak veya belirli sayıda tekrar yapmak |
| `while`    | Bir koşul doğru olduğu sürece çalışmak                           |
| `range()`  | Sayısal aralık oluşturmak                                        |
| `break`    | Döngüyü tamamen sonlandırmak                                     |
| `continue` | Mevcut turu atlayıp sonraki tura geçmek                          |

Döngüler, programların tekrar eden işlemleri otomatik olarak gerçekleştirmesini sağlar.

`for`, `while`, koşullar ve veri yapıları birlikte kullanıldığında çok daha güçlü programlar oluşturulabilir.

