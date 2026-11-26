# Variables

## 1. Variable Nedir?

Variable (değişken), bir değere bir isim vererek program içerisinde o değere tekrar erişebilmemizi sağlayan yapıdır.

Python'da bir değişken oluşturmak için özel bir anahtar kelime kullanmamız gerekmez. Değişken ismi yazılır ve `=` operatörü ile bir değer atanır.

```python
name = "Osman"
age = 32
```

Burada:

* `name` değişkeninin değeri `"Osman"`
* `age` değişkeninin değeri `32`

olur.

---

## 2. Değer Atama

Python'da `=` operatörü matematikteki eşitlik anlamından farklı olarak **atama** işlemi için kullanılır.

```python
name = "Osman"
```

Bu ifade:

> `"Osman"` değerini `name` adıyla ilişkilendir.

şeklinde düşünülebilir.

Bir değişkenin değeri daha sonra değiştirilebilir:

```python
age = 32
age = 33
```

Bu durumda `age` artık `33` değerini temsil eder.

---

## 3. Birden Fazla Değişken

Aynı program içerisinde istediğimiz kadar değişken oluşturabiliriz.

```python
name = "Osman"
age = 32
city = "Podgorica"
```

Değişkenler farklı türlerde değerler de tutabilir:

```python
name = "Osman"
age = 32
height = 1.80
is_learning = True
```

---

## 4. Birden Fazla Değişkene Aynı Anda Değer Atama

Python'da birden fazla değişkene aynı satırda değer atanabilir.

```python
name, age, city = "Osman", 32, "Podgorica"
```

Bu yapı özellikle Python'un çoklu atama özelliğini anlamak açısından önemlidir.

---

## 5. Değişken İsimlendirme

Değişken isimleri anlamlı seçilmelidir.

Örneğin:

```python
user_name = "Osman"
book_page = 100
library_name = "Ege"
```

şu kullanımdan daha okunabilirdir:

```python
x = "Osman"
a = 100
b = "Ege"
```

Python'da değişken isimleri:

* Harf veya `_` ile başlayabilir.
* Sayı ile başlayamaz.
* Harf, sayı ve `_` içerebilir.
* Büyük/küçük harfe duyarlıdır.
* Python'un ayrılmış anahtar kelimeleri değişken adı olarak kullanılmamalıdır.

Örnek:

```python
user_name = "Osman"
book1 = "Python101"
_book_count = 10
```

Geçersiz örnek:

```python
1book = "Python101"
```

---

## 6. Değişkenlerin Değerlerini Kullanmak

Bir değişkene değer atadıktan sonra değişkenin kendisini kullanabiliriz.

```python
name = "Osman"
print(name)
```

Çıktı:

```text
Osman
```

Değişkenleri başka ifadelerin içerisinde de kullanabiliriz:

```python
name = "Osman"
age = 32

print(f"{name} {age} yaşında.")
```

---

## 7. Değişkenlerin Değerlerini Değiştirmek

Bir değişken daha sonra farklı bir değerle yeniden atanabilir.

```python
score = 10
score = 20
```

Son durumda:

```python
print(score)
```

çıktısı:

```text
20
```

olur.

---

## 8. Öğrenme Notu

Python öğrenirken değişkenleri yalnızca "içinde değer bulunan kutular" olarak düşünmek başlangıç için faydalıdır.

Ancak Python'un çalışma mantığını daha derin öğrendikçe değişkenlerin aslında nesnelere ve değerlere nasıl bağlandığını daha ayrıntılı incelemek gerekir.

Bu konu ilerleyen bölümlerde daha derin ele alınacaktır.

---

## Örnek

```python
name = "Osman"
age = 32
city = "Podgorica"

print(f"Adım: {name}")
print(f"Yaşım: {age}")
print(f"Şehrim: {city}")
```

Bu örnekte üç farklı değişken oluşturulmuş ve daha sonra bu değişkenlerin değerleri kullanılmıştır.

