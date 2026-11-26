# Input and Output

## 1. `print()`

Python'da ekrana çıktı vermek için `print()` fonksiyonu kullanılır.

```python
print("Hello World")
```

Bir değişkenin değerini de yazdırabiliriz:

```python
name = "Osman"

print(name)
```

Birden fazla değeri aynı anda yazdırabiliriz:

```python
name = "Osman"
age = 32

print(name, age)
```

---

## 2. `input()`

Kullanıcıdan veri almak için `input()` fonksiyonu kullanılır.

```python
name = input("Adınızı giriniz: ")

print(name)
```

Program kullanıcıdan bir değer bekler ve kullanıcının girdiği değeri `name` değişkenine atar.

---

## 3. `input()` Her Zaman `str` Döndürür

Önemli bir nokta:

`input()` ile alınan veri, kullanıcı sayı girmiş olsa bile varsayılan olarak `str` türündedir.

```python
age = input("Yaşınızı giriniz: ")

print(type(age))
```

Kullanıcı:

```text
32
```

girse bile sonuç:

```text
<class 'str'>
```

olacaktır.

Bu nedenle kullanıcıdan alınan sayısal veriler gerektiğinde dönüştürülmelidir.

---

## 4. `int(input())`

Kullanıcıdan alınan değeri tam sayıya çevirmek için `int()` kullanılabilir.

```python
age = int(input("Yaşınızı giriniz: "))

print(age)
print(type(age))
```

Bu durumda kullanıcı `32` girerse:

```text
<class 'int'>
```

elde edilir.

Böylece kullanıcıdan alınan veri matematiksel işlemlerde kullanılabilir:

```python
age = int(input("Yaşınızı giriniz: "))

next_year = age + 1

print(next_year)
```

---

## 5. `float(input())`

Ondalıklı bir sayı almak istediğimizde `float()` kullanılabilir.

```python
height = float(input("Boyunuzu giriniz: "))

print(height)
print(type(height))
```

Kullanıcı:

```text
180.5
```

girdiğinde değer `float` türünde olur.

---

## 6. `print()` ve Birden Fazla Değer

`print()` fonksiyonuna birden fazla değer gönderebiliriz.

```python
name = "Osman"
age = 32

print(name, age)
```

Python varsayılan olarak değerlerin arasına bir boşluk koyar.

---

## 7. `sep`

`print()` içerisinde değerlerin arasına hangi ayırıcının konulacağını `sep` parametresiyle belirleyebiliriz.

```python
name = "Osman"
age = 32
city = "Podgorica"

print(name, age, city, sep=" - ")
```

Çıktı:

```text
Osman - 32 - Podgorica
```

`sep` özellikle birden fazla değerin belirli bir formatta gösterilmesi gerektiğinde kullanılabilir.

---

## 8. `end`

`print()` varsayılan olarak çıktıdan sonra yeni satıra geçer.

`end` parametresi bu davranışı değiştirmemizi sağlar.

```python
print("Hello", end=" ")
print("World")
```

Çıktı:

```text
Hello World
```

Örneğin `end=""` kullanırsak:

```python
print("Hello", end="")
print("World")
```

Çıktı:

```text
HelloWorld
```

---

## 9. f-string

Değişkenleri metin içerisinde kullanmanın okunabilir yollarından biri f-string kullanmaktır.

```python
name = "Osman"
age = 32

print(f"My name is {name}. I am {age} years old.")
```

Süslü parantezler `{}` içerisine değişkenleri yerleştirebiliriz.

Bu yöntem özellikle birden fazla değişkenin aynı metin içerisinde kullanılacağı durumlarda okunabilirliği artırır.

---

## 10. Kullanıcıdan Alınan Veriyi Kullanmak

`input()` ile alınan veri doğrudan başka işlemlerde kullanılabilir.

```python
name = input("Adınız: ")
age = int(input("Yaşınız: "))

print(f"Merhaba {name}. Gelecek yıl {age + 1} yaşında olacaksınız.")
```

Burada:

1. Kullanıcıdan isim alınır.
2. Kullanıcıdan yaş alınır.
3. Yaş `int` türüne dönüştürülür.
4. Matematiksel işlem yapılır.
5. Sonuç f-string ile ekrana yazdırılır.

---

## 11. Öğrenme Notu

`input()` ile çalışırken en önemli noktalardan biri, kullanıcıdan gelen verinin türünü unutmamaktır.

Örneğin:

```python
age = input("Yaşınız: ")
```

ifadesinden sonra `age` bir `str` değeridir.

Bu nedenle:

```python
age + 1
```

gibi bir işlem doğrudan yapılamaz.

Bunun yerine:

```python
age = int(input("Yaşınız: "))
```

şeklinde dönüşüm yapılabilir.

Bu ayrım, kullanıcı girdileriyle çalışan programlarda temel bir konudur.

---

## Özet

| Yapı       | Görevi                                                    |
| ---------- | --------------------------------------------------------- |
| `print()`  | Ekrana çıktı verir                                        |
| `input()`  | Kullanıcıdan veri alır                                    |
| `int()`    | Değeri tam sayıya dönüştürür                              |
| `float()`  | Değeri ondalıklı sayıya dönüştürür                        |
| `sep`      | `print()` içerisindeki değerlerin ayırıcısını belirler    |
| `end`      | `print()` sonrasındaki davranışı belirler                 |
| `f-string` | Değişkenleri metin içerisinde okunabilir şekilde kullanır |

Bu yapıların daha karmaşık kullanımları ilerleyen Python bölümlerinde gerektiğinde ele alınacaktır.

