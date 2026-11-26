# Operators

## 1. Operatör Nedir?

Operatörler, değerler üzerinde işlem yapmak için kullanılan sembol veya anahtar kelimelerdir.

Örneğin:

```python
result = 10 + 5
```

Burada `+` iki değeri toplamak için kullanılan aritmetik operatördür.

Python'da farklı amaçlarla kullanılan çeşitli operatör grupları vardır.

---

## 2. Arithmetic Operators

Aritmetik operatörler matematiksel işlemler yapmak için kullanılır.

| Operatör | Açıklama         | Örnek     | Sonuç      |
| -------- | ---------------- | --------- | ---------- |
| `+`      | Toplama          | `10 + 3`  | `13`       |
| `-`      | Çıkarma          | `10 - 3`  | `7`        |
| `*`      | Çarpma           | `10 * 3`  | `30`       |
| `/`      | Bölme            | `10 / 3`  | `3.333...` |
| `//`     | Tam sayı bölmesi | `10 // 3` | `3`        |
| `%`      | Modulo / kalan   | `10 % 3`  | `1`        |
| `**`     | Üs alma          | `10 ** 2` | `100`      |

Örnek:

```python
number1 = 10
number2 = 3

print(number1 + number2)
print(number1 - number2)
print(number1 * number2)
print(number1 / number2)
print(number1 // number2)
print(number1 % number2)
print(number1 ** number2)
```

---

## 3. Comparison Operators

Karşılaştırma operatörleri iki değeri karşılaştırır ve sonuç olarak `True` veya `False` üretir.

| Operatör | Anlamı          |
| -------- | --------------- |
| `==`     | Eşit            |
| `!=`     | Eşit değil      |
| `>`      | Büyük           |
| `<`      | Küçük           |
| `>=`     | Büyük veya eşit |
| `<=`     | Küçük veya eşit |

Örnek:

```python
age = 32

print(age == 32)
print(age != 20)
print(age > 18)
print(age < 18)
print(age >= 32)
print(age <= 30)
```

Karşılaştırmaların sonucu `bool` türündedir.

```python
print(type(age > 18))
```

Sonuç:

```text
<class 'bool'>
```

---

## 4. Logical Operators

Mantıksal operatörler birden fazla koşulu birleştirmek veya bir koşulun mantıksal sonucunu değiştirmek için kullanılır.

### `and`

İki koşulun da `True` olması gerekir.

```python
age = 25
has_ticket = True

print(age >= 18 and has_ticket)
```

Her iki ifade doğru olduğu için sonuç `True` olur.

---

### `or`

Koşullardan en az birinin `True` olması yeterlidir.

```python
has_cash = False
has_card = True

print(has_cash or has_card)
```

Sonuç `True` olur.

---

### `not`

Bir boolean değerin tersini verir.

```python
is_closed = False

print(not is_closed)
```

Sonuç:

```text
True
```

Mantıksal operatörler özellikle `if` koşullarında yoğun şekilde kullanılacaktır.

---

## 5. Assignment Operators

Değişkenlere değer atamak veya mevcut değerlerini güncellemek için kullanılır.

Temel atama:

```python
number = 10
```

Bazı kısaltılmış atama operatörleri:

| Operatör | Anlamı                |
| -------- | --------------------- |
| `=`      | Değer ata             |
| `+=`     | Topla ve ata          |
| `-=`     | Çıkar ve ata          |
| `*=`     | Çarp ve ata           |
| `/=`     | Böl ve ata            |
| `//=`    | Tam böl ve ata        |
| `%=`     | Kalanı hesapla ve ata |
| `**=`    | Üs al ve ata          |

Örnek:

```python
number = 10

number += 5
print(number)
```

Sonuç:

```text
15
```

Bu ifade:

```python
number += 5
```

mantıksal olarak:

```python
number = number + 5
```

ile aynıdır.

---

## 6. Operatörleri Birlikte Kullanmak

Bir ifade içerisinde birden fazla operatör kullanılabilir.

```python
age = 32
next_year = age + 1

print(next_year > 30)
```

Burada önce aritmetik işlem yapılır:

```python
age + 1
```

sonrasında sonuç karşılaştırılır:

```python
next_year > 30
```

Sonuç `True` veya `False` olur.

---

## 7. Parantez Kullanımı

İşlem sırasını kontrol etmek için parantez kullanılabilir.

```python
result1 = 10 + 5 * 2
result2 = (10 + 5) * 2

print(result1)
print(result2)
```

İlk ifadede çarpma önce yapılır.

İkinci ifadede parantez içerisindeki toplama önce yapılır.

Bu nedenle sonuçlar farklıdır.

---

## 8. Operatörler ve Veri Türleri

Operatörlerin davranışı kullanılan veri türüne göre değişebilir.

Örneğin sayılarda:

```python
print(10 + 5)
```

sonucu:

```text
15
```

olur.

Stringlerde ise `+` birleştirme amacıyla kullanılabilir:

```python
first_name = "Osman"
last_name = "Bozok"

full_name = first_name + " " + last_name

print(full_name)
```

Sonuç:

```text
Osman Bozok
```

`*` operatörü de stringlerde tekrar amacıyla kullanılabilir:

```python
word = "Python"

print(word * 3)
```

Sonuç:

```text
PythonPythonPython
```

Bu davranışlar Python'un veri türlerine göre operatörlere farklı anlamlar verebilmesinin bir örneğidir.

---

## 9. `==` ve `=` Farkı

Yeni başlayanlar için özellikle dikkat edilmesi gereken bir ayrım vardır.

```python
age = 32
```

Buradaki `=` bir değer atama operatörüdür.

```python
age == 32
```

Buradaki `==` ise iki değerin eşit olup olmadığını karşılaştırır.

Örneğin:

```python
age = 32

print(age == 32)
```

Sonuç:

```text
True
```

---

## 10. Öğrenme Notu

Operatörleri sadece sembol olarak ezberlemek yerine, **hangi durumda hangi tür sonuç ürettiklerini** anlamak önemlidir.

Örneğin:

```python
10 / 2
```

bir sayı üretirken:

```python
10 > 2
```

bir `bool` üretir.

Benzer şekilde:

```python
"Python" + "101"
```

string birleştirirken:

```python
10 + 20
```

aritmetik toplama yapar.

Aynı operatörün farklı veri türlerinde farklı davranabilmesi Python'un önemli özelliklerinden biridir.

---

## Özet

Python'daki temel operatör grupları:

* **Arithmetic Operators** → Matematiksel işlemler
* **Comparison Operators** → Değerleri karşılaştırma
* **Logical Operators** → Koşulları mantıksal olarak birleştirme
* **Assignment Operators** → Değer atama ve güncelleme

Operatörler ilerleyen bölümlerde özellikle koşullar, döngüler ve fonksiyonlarla birlikte tekrar kullanılacaktır.

