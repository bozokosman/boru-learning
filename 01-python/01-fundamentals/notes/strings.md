# Strings

## 1. String Nedir?

String, metinsel verileri temsil eden veri tipidir.

Python'da string oluşturmak için tek veya çift tırnak kullanılabilir.

    name = "Osman"
    city = 'Podgorica'

---

## 2. String Indexing

String içerisindeki karakterlere indeks numarasıyla erişilebilir.

İndeksler `0`'dan başlar.

    name = "Osman"

    print(name[0])
    print(name[1])
    print(name[2])

Negatif indeksler sondan başlayarak erişim sağlar.

    print(name[-1])
    print(name[-2])

---

## 3. String Slicing

String'in belirli bir bölümünü almak için slicing kullanılabilir.

    name = "Osman"

    print(name[0:3])
    print(name[:3])
    print(name[2:])
    print(name[::-1])

Başlangıç indeksi dahil edilir, bitiş indeksi dahil edilmez.

---

## 4. `len()`

`len()` bir string içerisindeki karakter sayısını verir.

    name = "Osman"

    print(len(name))

Boşluklar da karakter olarak sayılır.

    text = "Hello World"

    print(len(text))

---

## 5. `upper()`

String içerisindeki karakterleri büyük harfe dönüştürür.

    name = "Osman"

    print(name.upper())

---

## 6. `lower()`

String içerisindeki karakterleri küçük harfe dönüştürür.

    name = "OSMAN"

    print(name.lower())

---

## 7. `strip()`

String'in başındaki ve sonundaki boşlukları temizler.

    name = "   Osman   "

    print(name.strip())

---

## 8. `replace()`

Bir string içerisindeki belirli bir ifadeyi başka bir ifadeyle değiştirir.

    text = "I like Java"

    print(text.replace("Java", "Python"))

---

## 9. `split()`

Bir string'i belirli bir ayırıcıya göre parçalayıp listeye dönüştürür.

    text = "Python,Java,C++"

    languages = text.split(",")

    print(languages)

Boşluklara göre de parçalanabilir.

    text = "Python is powerful"

    words = text.split()

    print(words)

---

## 10. `join()`

Bir string listesindeki elemanları belirli bir ayırıcı kullanarak birleştirir.

    languages = ["Python", "Java", "C++"]

    text = ", ".join(languages)

    print(text)

Başka bir ayırıcı da kullanılabilir.

    text = " - ".join(languages)

    print(text)

---

## 11. `in` ve `not in`

Bir string içerisinde belirli bir ifadenin bulunup bulunmadığını kontrol etmek için `in` kullanılabilir.

    text = "Python programming"

    print("Python" in text)
    print("Java" in text)

`not in`, bir ifadenin string içerisinde bulunmadığını kontrol eder.

    print("Java" not in text)

---

## 12. String Karşılaştırma

Stringler karşılaştırılabilir.

    name = "Osman"

    print(name == "Osman")
    print(name != "Ahmet")

Karşılaştırmalar özellikle kullanıcıdan alınan verileri kontrol ederken kullanılabilir.

    password = input("Şifrenizi giriniz: ")

    if password == "1234":
        print("Giriş başarılı.")
    else:
        print("Şifre yanlış.")

---

## 13. f-string

f-string, değişkenleri string içerisinde kolayca kullanmayı sağlar.

    name = "Osman"
    age = 32

    print(f"My name is {name}. I am {age} years old.")

Birden fazla değişken kullanılabilir.

    name = "Osman"
    age = 32
    city = "Podgorica"

    print(f"My name is {name}. I am {age} years old and I live in {city}.")

---

## 14. Escape Characters

Bazı özel karakterleri string içerisinde kullanmak için escape karakterleri kullanılabilir.

### Yeni Satır — `\n`

    print("Hello\nWorld")

### Tab — `\t`

    print("Hello\tWorld")

### Çift Tırnak — `\"`

    print("He said \"Hello\"")

### Tek Tırnak — `\'`

    print('It\'s Python')

---

## 15. Çok Satırlı String

Üç tırnak kullanılarak birden fazla satıra yayılan string oluşturulabilir.

    text = """
    Python
    Computer Science
    Programming
    """

    print(text)

---

## 16. String Immutability

Python'daki stringler **immutable**, yani değiştirilemez veri tipleridir.

Örneğin aşağıdaki işlem hata verir:

    name = "Osman"

    name[0] = "A"

String'in kendisi üzerinde doğrudan değişiklik yapmak yerine yeni bir string oluşturulur.

    name = "Ahmet"

String metodları da genellikle mevcut string'i değiştirmek yerine yeni bir string döndürür.

    name = "osman"

    new_name = name.upper()

    print(name)
    print(new_name)

Burada `name` değişmeden kalır ve `new_name` yeni string olur.

---

## 17. String ve List Arasındaki Bağlantı

String üzerinde slicing yapılabilir.

    name = "Osman"

    print(name[0:3])

String `split()` kullanılarak listeye dönüştürülebilir.

    text = "Python Java C++"

    languages = text.split()

    print(languages)

Liste tekrar `join()` ile string haline getirilebilir.

    text = " ".join(languages)

    print(text)

Bu nedenle `split()` ve `join()` özellikle veri işleme sırasında önemlidir.

---

## 18. String Üzerinde `for`

Stringler üzerinde karakter karakter dolaşılabilir.

    name = "Osman"

    for character in name:
        print(character)

Sonuç karakterleri tek tek yazdırır:

    O
    s
    m
    a
    n

---

## 19. String İçerisinde Arama

`in` kullanılarak bir kelimenin veya karakterin string içerisinde bulunup bulunmadığı kontrol edilebilir.

    text = "Python programming language"

    if "Python" in text:
        print("Python bulundu.")
    else:
        print("Python bulunamadı.")

---

## 20. Temel String İşlemleri Özeti

| İşlem | Amaç |
|---|---|
| `len()` | Karakter sayısını bulmak |
| `upper()` | Büyük harfe dönüştürmek |
| `lower()` | Küçük harfe dönüştürmek |
| `strip()` | Baş ve sondaki boşlukları temizlemek |
| `replace()` | Metin değiştirmek |
| `split()` | String'i listeye ayırmak |
| `join()` | String listesini birleştirmek |
| `in` | String içerisinde arama yapmak |
| `not in` | String içerisinde bulunmadığını kontrol etmek |
| `[]` | İndeks ile karaktere erişmek |
| `[:]` | String slicing yapmak |
| `f""` | String formatting yapmak |
| `\n` | Yeni satır |
| `\t` | Tab boşluğu |

---

## 21. Mini Örnek

String işlemlerinin birkaçını birlikte kullanabiliriz.

    name = input("Adınızı giriniz: ")

    name = name.strip()
    name = name.lower()

    if "osman" in name:
        print("Osman bulundu.")

    print(f"Merhaba, {name}!")

Burada:

1. Kullanıcıdan string alındı.
2. Başındaki ve sonundaki boşluklar temizlendi.
3. Küçük harfe dönüştürüldü.
4. `in` ile arama yapıldı.
5. f-string ile çıktı oluşturuldu.

---

## Özet

Stringler Python'da metinsel verileri temsil eder.

Temel olarak:

    name = "Osman"

şeklinde oluşturulur.

Stringler üzerinde:

- indeksleme
- slicing
- arama
- karşılaştırma
- dönüştürme
- parçalama
- birleştirme
- formatting

gibi işlemler yapılabilir.

Stringlerin immutable olması önemli bir özelliktir.

Özellikle `split()`, `join()`, `replace()`, `strip()`, `in` ve f-string kullanımı Python'da günlük programlama sırasında oldukça yaygındır.
