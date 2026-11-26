# Python Functions

> 🇬🇧 [Click here for English documentation](README.md)

## 1. Function Nedir?
Function, belirli bir işi gerçekleştiren ve ihtiyaç duyulduğunda tekrar çağrılabilen kod bloğudur.

Fonksiyon kullanmak:
- Kod tekrarını azaltır.
- Programı parçalara ayırır.
- Kodun okunabilirliğini artırır.
- Kodun tekrar kullanılmasını sağlar.
- Büyük programları daha küçük parçalara bölmeyi kolaylaştırır.

---

## 2. Function Tanımlama
Python'da fonksiyon tanımlamak için `def` keyword'ü kullanılır.

```python
def greet():
    print("Merhaba!")
```
Fonksiyon tanımlandıktan sonra çağrılabilir:
```python
greet()
```
Sonuç:
```text
Merhaba!
```

## 3. Function Call
Bir fonksiyonun içerisindeki kodun çalışması için fonksiyon çağrılmalıdır.

```python
def say_hello():
    print("Hello")

say_hello()
say_hello()
say_hello()
```
Aynı fonksiyon birden fazla kez çağrılabilir.

## 4. Parameters
Fonksiyon dışarıdan veri alabilir. Bu verilere **parameter** denir.

```python
def greet(name):
    print(f"Merhaba {name}!")
```
Fonksiyon çağrılırken verilen değere ise **argument** denir:
```python
greet("Osman")
```
Burada:
- `name` → parameter
- `"Osman"` → argument

## 5. Birden Fazla Parameter
Bir fonksiyon birden fazla parameter alabilir.

```python
def introduce(name, age, city):
    print(f"Ben {name}. {age} yaşındayım ve {city} şehrinde yaşıyorum.")
```
Çağırma:
```python
introduce("Osman", 32, "Podgorica")
```
Parameter sırası önemlidir.

## 6. Arguments
Function çağrılırken parametrelere gönderilen değerlere argument denir.

```python
def add(number1, number2):
    print(number1 + number2)

add(10, 20)
```
Burada:
- `number1`, `number2` → parameter
- `10`, `20` → argument

## 7. Return
`return`, fonksiyonun sonucunu fonksiyonu çağıran yere geri gönderir.

```python
def add(number1, number2):
    return number1 + number2
```
Sonucu bir değişkende saklayabiliriz:
```python
result = add(10, 20)
print(result)
```
Sonuç:
```text
30
```
`print()` ile `return` aynı şey değildir.

```python
def add(number1, number2):
    print(number1 + number2)
```
Bu fonksiyon sonucu ekrana yazdırır.

```python
def add(number1, number2):
    return number1 + number2
```
Bu fonksiyon sonucu geri döndürür.

## 8. Return Sonrası Kod
`return` çalıştığında fonksiyon sona erer.

```python
def test():
    print("Bir")
    return
    print("İki")

test()
```
Sonuç:
```text
Bir
```
`return` sonrasındaki kod çalışmaz.

## 9. Function ile Hesaplama
Fonksiyonlar hesaplama işlemlerini tekrar kullanılabilir hale getirebilir.

```python
def square(number):
    return number ** 2

print(square(5))
print(square(10))
print(square(20))
```
Sonuç:
```text
25
100
400
```

## 10. Local Variables
Fonksiyon içerisinde oluşturulan değişkenler normalde local variable'dır.

```python
def calculate():
    number = 10
    print(number)

calculate()
```
`number` fonksiyonun local scope'u içerisindedir.
Fonksiyon dışında:
```python
print(number)
```
kullanılmaya çalışılırsa hata alınır.

## 11. Global Variables
Fonksiyon dışında oluşturulan değişkenler global scope'ta bulunur.

```python
name = "Osman"

def greet():
    print(name)

greet()
```
Fonksiyon global değişkeni okuyabilir.

## 12. Local ve Global Aynı İsim
Aynı isimde local ve global değişken bulunabilir.

```python
name = "Osman"

def greet():
    name = "Ahmet"
    print(name)

greet()
print(name)
```
Sonuç:
```text
Ahmet
Osman
```
Fonksiyon içerisindeki `name` local variable'dır. Fonksiyon dışındaki `name` global variable'dır.

## 13. global Keyword
Bir fonksiyon içerisinde global bir değişkenin değerini değiştirmek için `global` kullanılabilir.

```python
counter = 0

def increase():
    global counter
    counter += 1

increase()
increase()

print(counter)
```
Sonuç:
```text
2
```
Ancak mümkün olduğunda global değişkenleri değiştirmek yerine fonksiyonlara parameter gönderip `return` kullanmak daha temiz bir yaklaşımdır.

## 14. Default Parameters
Bir parametreye varsayılan değer verilebilir.

```python
def greet(name="Guest"):
    print(f"Merhaba {name}!")
```
Argument gönderilmezse default değer kullanılır:
```python
greet()
```
Sonuç:
```text
Merhaba Guest!
```
Argument gönderilirse verilen değer kullanılır:
```python
greet("Osman")
```
Sonuç:
```text
Merhaba Osman!
```

## 15. Birden Fazla Parameter ve Default Value
Bazı parametreler default value taşıyabilir.

```python
def introduce(name, age=18):
    print(f"{name} {age} yaşında.")

introduce("Osman")
```
Sonuç:
```text
Osman 18 yaşında.
```
ve:
```python
introduce("Osman", 32)
```
Sonuç:
```text
Osman 32 yaşında.
```
Default parameter'dan önce normal parameter bulunabilir. Ancak default parameter'dan sonra tekrar default olmayan parameter yazılamaz.

**Yanlış:**
```python
def test(age=18, name):
    pass
```

## 16. Keyword Arguments
Fonksiyon çağrılırken parameter adı açıkça belirtilebilir.

```python
def introduce(name, age, city):
    print(name, age, city)

introduce(
    name="Osman",
    age=32,
    city="Podgorica"
)
```
Bu yöntemde argument sırasına bağımlılık azalır.
Örneğin:
```python
introduce(
    city="Podgorica",
    name="Osman",
    age=32
)
```
şeklinde de çağrılabilir.

## 17. Positional ve Keyword Arguments
İki yöntem aynı fonksiyon içerisinde birlikte kullanılabilir.

```python
def introduce(name, age, city):
    print(name, age, city)

introduce("Osman", age=32, city="Podgorica")
```
Positional argument'lar keyword argument'lardan önce gelmelidir.

## 18. Multiple Return Values
Bir fonksiyon birden fazla değer döndürebilir. Python bu değerleri tuple olarak döndürür.

```python
def get_book():
    return "Python101", "Osman Bozok", 5000
```
Dönen değerler unpack edilebilir:
```python
book_name, author, page = get_book()

print(book_name)
print(author)
print(page)
```
Sonuç:
```text
Python101
Osman Bozok
5000
```

## 19. *args
Bir fonksiyona kaç tane positional argument gönderileceğinin önceden bilinmediği durumlarda `*args` kullanılabilir.

```python
def add_numbers(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total
```
Artık farklı sayıda argument gönderebiliriz:
```python
print(add_numbers(10, 20))
print(add_numbers(10, 20, 30))
print(add_numbers(1, 2, 3, 4, 5))
```
`args` fonksiyon içerisinde tuple olarak bulunur.

## 20. **kwargs
Kaç tane keyword argument gönderileceğinin önceden bilinmediği durumlarda `**kwargs` kullanılabilir.

```python
def show_info(**information):
    for key, value in information.items():
        print(f"{key}: {value}")
```
Çağırma:
```python
show_info(
    name="Osman",
    age=32,
    city="Podgorica"
)
```
`kwargs` fonksiyon içerisinde dictionary olarak bulunur.

## 21. *args ve **kwargs Birlikte
İki yapı aynı fonksiyonda kullanılabilir.

```python
def example(*args, **kwargs):
    print(args)
    print(kwargs)
```
Örneğin:
```python
example(
    10,
    20,
    30,
    name="Osman",
    city="Podgorica"
)
```
Burada:
- `args` → tuple
- `kwargs` → dictionary

## 22. Function Composition
Bir fonksiyonun sonucunu başka bir fonksiyona gönderebiliriz.

```python
def double(number):
    return number * 2

def add_five(number):
    return number + 5

result = add_five(double(10))
print(result)
```
İlk olarak `double(10)` çalışır. Sonuç: `20`
Daha sonra `add_five(20)` çalışır. Sonuç: `25`

## 23. Recursive Functions
Bir fonksiyonun kendisini tekrar çağırmasına recursion denir.
Basit örnek:

```python
def countdown(number):
    if number == 0:
        return
    print(number)
    countdown(number - 1)

countdown(5)
```
Sonuç:
```text
5
4
3
2
1
```
Recursive function içerisinde mutlaka durma koşulu bulunmalıdır. Aksi durumda fonksiyon kendisini sonsuza kadar çağırabilir.

## 24. Lambda Functions
Lambda, kısa ve basit fonksiyonlar oluşturmak için kullanılan bir syntax'tır.

Normal function:
```python
def square(number):
    return number ** 2
```
Lambda:
```python
square = lambda number: number ** 2
```
Kullanım:
```python
print(square(5))
```
Lambda genellikle kısa işlemlerde ve özellikle başka fonksiyonlarla birlikte kullanıldığında faydalıdır.

## 25. Functions ve Data Structures
Fonksiyonlar list, tuple, set ve dictionary gibi veri yapılarıyla birlikte kullanılabilir.

Örneğin:
```python
def calculate_total(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
```
Kullanım:
```python
numbers = [10, 20, 30, 40]
result = calculate_total(numbers)
print(result)
```
Fonksiyonun içerisine veri yapısı gönderilebilir.

## 26. Function ile Dictionary Kullanımı
Dictionary içerisindeki bilgileri işleyen fonksiyonlar oluşturulabilir.

```python
def print_book(book):
    print(f"Kitap: {book['name']}")
    print(f"Yazar: {book['author']}")
    print(f"Sayfa: {book['page']}")
```
Kullanım:
```python
book = {
    "name": "Python101",
    "author": "Osman Bozok",
    "page": 5000
}

print_book(book)
```

## 27. Function Design
Fonksiyonlar mümkün olduğunca tek bir sorumluluğa sahip olmalıdır.

Örneğin:
```python
def calculate_total(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
```
Bu fonksiyonun görevi yalnızca toplam hesaplamaktır.

Bunun yerine:
```python
def calculate_and_print_and_save_and_send(numbers):
    pass
```
gibi çok fazla sorumluluğu tek fonksiyona yüklemek kodun bakımını zorlaştırır.

## 28. Function Naming
Fonksiyon isimleri genellikle `snake_case` kullanılarak yazılır.

İyi örnekler:
- `calculate_total()`
- `get_book()`
- `find_user()`
- `print_books()`
- `calculate_average()`

Kaçınılması gereken örnekler:
- `x()`
- `abc()`
- `doit()`
- `function1()`

Fonksiyon adı mümkün olduğunca fonksiyonun ne yaptığını açıklamalıdır.

## 29. Docstring
Fonksiyonun ne yaptığını açıklamak için docstring kullanılabilir.

```python
def calculate_total(numbers):
    """
    Verilen sayıların toplamını döndürür.
    """
    total = 0
    for number in numbers:
        total += number
    return total
```
Docstring fonksiyonun amacı ve kullanımı hakkında bilgi vermek için kullanılır.

## 30. Functions ile Programı Parçalamak
Büyük bir programı tek bir kod bloğu halinde yazmak yerine küçük fonksiyonlara ayırabiliriz.

Örneğin bir kütüphane programında:
```python
def add_book():
    pass

def remove_book():
    pass

def search_book():
    pass

def list_books():
    pass
```
Her fonksiyon programın farklı bir sorumluluğunu üstlenir. Bu yaklaşım büyük projelerde kodun okunabilirliğini ve bakımını kolaylaştırır.

---

## Summary
Functions bölümünde şu konular öğrenildi:
- Function tanımlama
- Function call
- Parameters
- Arguments
- `return`
- Local scope
- Global scope
- `global`
- Default parameters
- Keyword arguments
- Positional arguments
- Multiple return values
- Tuple unpacking
- `*args`
- `**kwargs`
- Function composition
- Recursive functions
- Lambda functions
- Functions + Data Structures
- Docstrings
- Function naming
- Single responsibility
- Büyük programları fonksiyonlara bölme

Temel function yapısı:
```python
def function_name(parameters):
    # işlemler
    return result
```
Basit örnek:
```python
def add(number1, number2):
    return number1 + number2

result = add(10, 20)
print(result)
```
Fonksiyonların temel amacı kodu tekrar kullanılabilir, anlaşılır ve yönetilebilir parçalara ayırmaktır.
