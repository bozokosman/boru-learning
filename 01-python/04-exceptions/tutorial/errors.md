# 📚 Python — Errors and Exceptions (Hatalar ve İstisnalar)

## 1. Sözdizim Hataları (Syntax Errors)

### 1.1 Nedir?

**Syntax Error**, Python kodunu çalıştırmadan **önce** (parsing aşamasında) interpreter tarafından bulunur. Python'un yazım kurallarını ihlal ettiğinde oluşur.

```python
# ❌ HATA 1: Kapalı olmayan parantez
print("Merhaba"
# SyntaxError: '(' was never closed

# ❌ HATA 2: Hatalı if sözdizimi
if x = 5:  # = yerine == olması lazım (karşılaştırma)
    print(x)
# SyntaxError: invalid syntax

# ❌ HATA 3: Yanlış indentasyon (girinti)
def greet():
print("Selam")  # def'in altında olması lazım, girinti gerekli
# IndentationError: expected an indented block

# ❌ HATA 4: Tanımlı olmayan kolon
for i in range(5)  # Döngüden sonra ':' gerekli
    print(i)
# SyntaxError: expected ':'

# ❌ HATA 5: Yanlış operatör
x == 5  # Atama değil karşılaştırma (if içinde)
y = 10 = 20  # Çoklu atama yanlış
# SyntaxError: cannot assign to operator
```

### 1.2 Hata İzlemesi (Traceback)

```
  File "program.py", line 1
    print("Merhaba"
                  ^
SyntaxError: '(' was never closed
```

Python sana:
- **Dosya adı** ve **satır numarası** gösterir
- Hatanın **yaklaşık yeri** (^) gösterir
- **Hata türü** ve **açıklaması** verir

---

## 2. Çalışma Zamanı Hataları (Runtime Errors / Exceptions)

### 2.1 Nedir?

**Exception**, kod sözdizimi olarak doğru olmasına rağmen, **çalıştırılırken** oluşan hatadır. Program bu noktada durur (crash olur).

---

### 2.2 Yaygın Exception Türleri

#### 🔴 **ValueError**
Fonksiyona doğru tip ama **geçersiz değer** geçildiğinde:

```python
# Stringi integere çevirmek, ama string sayı değil
x = int("hello")
# ValueError: invalid literal for int() with base 10: 'hello'

# Listeden olmayan bir değer çıkarmak
numbers = [1, 2, 3]
numbers.remove(5)  # 5 listede yok
# ValueError: list.remove(x): x not in list

# Packing/unpacking uyumsuzluğu
a, b = [1, 2, 3]  # 2 değer bekleniyor, 3 verildi
# ValueError: too many values to unpack (expected 2)
```

#### 🔴 **TypeError**
Yanlış **tip** (type) ile bir işlem yapıldığında:

```python
# String ve integer toplayamaz
result = "5" + 10
# TypeError: can only concatenate str (not "int") to str

# Parametrelerin sayısı yanlış
def add(a, b):
    return a + b

add(5)  # İki parametre gerekli, bir tane verildi
# TypeError: add() missing 1 required positional argument: 'b'

# Tanımsız bir metodu çağırmak
text = "hello"
text.upper_wrong()
# TypeError: 'str' object is not callable
```

#### 🔴 **IndexError**
Listede **olmayan indekse** erişmek:

```python
# Index out of range
fruits = ["apple", "banana"]
print(fruits[5])  # Sadece 0 ve 1 indeksi var
# IndexError: list index out of range

# String indeksi
word = "Python"
print(word[10])
# IndexError: string index out of range
```

#### 🔴 **KeyError**
Sözlükte **olmayan anahtar** kullanmak:

```python
# Sözlükte olmayan key
person = {"name": "Ali", "age": 25}
print(person["city"])  # "city" key'i yok
# KeyError: 'city'
```

#### 🔴 **AttributeError**
Nesne veya modülde **olmayan attribute** çağırmak:

```python
# String'in böyle bir metodu yok
text = "hello"
text.upper_wrong()
# AttributeError: 'str' object has no attribute 'upper_wrong'

# Modülde olmayan fonksiyon
import os
os.nonexistent_function()
# AttributeError: module 'os' has no attribute 'nonexistent_function'
```

#### 🔴 **NameError**
**Tanımlanmamış değişkeni** kullanmak:

```python
# x değişkeni hiç tanımlanmadı
print(x)
# NameError: name 'x' is not defined

# Yazım hatası
message = "Hello"
print(mesage)  # Yanlış yazıldı
# NameError: name 'mesage' is not defined
```

#### 🔴 **ZeroDivisionError**
Sıfıra bölmek:

```python
# Sıfıra bölünemez
result = 10 / 0
# ZeroDivisionError: division by zero

# Modulo operatörü ile sıfır
x = 5 % 0
# ZeroDivisionError: integer division or modulo by zero
```

#### 🔴 **FileNotFoundError**
Dosya bulunamadığında:

```python
# Dosya yok
with open("nonexistent.txt", "r") as f:
    content = f.read()
# FileNotFoundError: [Errno 2] No such file or directory: 'nonexistent.txt'
```

#### 🔴 **ImportError / ModuleNotFoundError**
Modül bulunamadığında:

```python
# Modül kurulu değil
import nonexistent_module
# ModuleNotFoundError: No module named 'nonexistent_module'

# Yanlış import
from os import fake_function
# ImportError: cannot import name 'fake_function' from 'os'
```

---

### 2.3 Hata Hiyerarşisi (Exception Hierarchy)

```
BaseException
├── SystemExit (sys.exit() çağrıldığında)
├── KeyboardInterrupt (Ctrl+C basıldığında)
├── GeneratorExit
└── Exception (Normal hatalar — bunu yakala!)
    ├── StopIteration
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   ├── FloatingPointError
    │   └── OverflowError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── NameError
    ├── TypeError
    ├── ValueError
    ├── FileNotFoundError (OSError'in alt sınıfı)
    └── ... (50+ daha)
```

**Önemli:** En genel `BaseException`'ı yakalama, **her zaman `Exception` yakala.**

---

## 3. Hata Yakalama: try/except Bloğu

### 3.1 Temel Yapı

```python
try:
    # Hata olabilecek kod
    risky_code()
except ExceptionType:
    # Hata oluştuğunda çalışacak kod
    handle_error()
```

#### Tam Akış Şeması

```python
try:
    # ADIM 1: Hata olabilecek kod çalışır
    number = int(input("Bir sayı gir: "))
    result = 10 / number
    print(f"Sonuç: {result}")

except ValueError:
    # ADIM 2A: Değer hatası varsa buraya girer
    print("❌ Lütfen geçerli bir sayı gir!")

except ZeroDivisionError:
    # ADIM 2B: Sıfıra bölme hatası varsa buraya girer
    print("❌ Sıfıra bölünemez!")

except Exception as e:
    # ADIM 2C: Diğer tüm hatalar
    print(f"❌ Beklenmeyen hata: {e}")

else:
    # ADIM 3: Eğer hiçbir hata yoksa
    print("✅ İşlem başarılı!")

finally:
    # ADIM 4: Her durumda çalışır (hata olsa da olmasa da)
    print("Program bitişi")
```

**Çalışma Sırası:**
1. `try` bloğu çalışır
2. Hata olursa → uygun `except` bloğuna gider
3. Hata yoksa → `else` bloğu çalışır
4. Her iki durumda da → `finally` çalışır

---

### 3.2 Belirli Exception'ları Yakalamak (En İyi Yöntem)

```python
try:
    number = int(input("Bir sayı gir: "))
    result = 10 / number
    print(f"Sonuç: {result}")

except ValueError:
    print("❌ Lütfen geçerli bir sayı gir!")

except ZeroDivisionError:
    print("❌ Sıfıra bölünemez!")
```

**Neden belirli exception yakalamalısın?**
- ✅ Hangı hata olduğunu bilirsin
- ✅ Sorun arama kolaylaşır
- ✅ Önemli hataları gözden kaçırmazsın
- ❌ `except:` veya `except Exception:` çok geniş, sorunları saklar

---

### 3.3 ❌ YANLIŞ YÖNTEMLER

```python
# ❌ YANLIŞ 1: Tüm hatalar görmezden gelinir
try:
    risky_code()
except:  # Boş except
    pass

# ❌ YANLIŞ 2: Hata saklanır
try:
    risky_code()
except Exception:  # Çok geniş
    pass

# ❌ YANLIŞ 3: try bloğu hata kaynağını kapsamıyor
number = int(input(...))  # Hata BURADAN gelebilir
try:
    if number > 0:  # Ama try BURADAN başlıyor
        return number
except ValueError:  # Hiç çalışmaz
    print("Hata")
```

---

### 3.4 Hata Nesnesini Yakalamak

```python
try:
    x = int("abc")
except ValueError as error:
    print(f"Hata türü: {type(error).__name__}")
    print(f"Hata mesajı: {error}")
    
    # Çıktı:
    # Hata türü: ValueError
    # Hata mesajı: invalid literal for int() with base 10: 'abc'
```

#### Hata Bilgilerini Loga Kaydetme

```python
import logging

try:
    risky_code()
except Exception as e:
    # Traceback ile tüm detayı kaydet
    logging.error(f"Hata oluştu: {e}", exc_info=True)
```

---

### 3.5 Çoklu Exception'ları Aynı Bloğa Yakalamak

```python
try:
    x = int(input("Sayı gir: "))
    result = 10 / x

except (ValueError, ZeroDivisionError) as e:
    print(f"Hata: {type(e).__name__} - {e}")
```

---

## 4. else ve finally Blokları

### 4.1 else Bloğu

Eğer **hiçbir exception oluşmazsa** çalışır:

```python
try:
    number = int(input("Bir sayı gir: "))
    result = 10 / number
except (ValueError, ZeroDivisionError) as e:
    print(f"Hata: {e}")
else:
    # Sadece hata yoksa çalışır
    print(f"✅ Başarılı! Sonuç: {result}")
    # Yazılan sayıyı kullanabilirsin
```

**Ne zaman kullanılır?**
- Hata yoksa çalışması gereken ek kod varsa
- try bloğunun başarısını kontrol etmek istiyorsan

---

### 4.2 finally Bloğu

Hata olsa da olmasa da **her zaman** çalışır (kaynak temizliği için):

```python
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("Dosya bulunamadı!")
finally:
    # Hata olsa da olmasa da dosya kapatılır
    file.close()
    print("Dosya kapatıldı.")
```

#### with Bloğu (Altın Kural)

```python
# finally yazma gereği yoktur, with otomatik kapatır
with open("data.txt", "r") as file:
    content = file.read()
# Blok bitince dosya otomatik kapanır
```

---

### 4.3 Tam Yapı

```python
try:
    risky_code()
except SpecificError as e:
    handle_error(e)
else:
    if_no_error()
finally:
    cleanup()
```

**Çalışma Sırası:**
1. `try` çalışır
2. Hata varsa → `except` çalışır (hatalı kodu bitir)
3. Hata yoksa → `else` çalışır
4. Her durumda → `finally` çalışır

---

## 5. Hata Fırlatma: raise

### 5.1 Basit Kullanım

Bazen **kendi hatalı durumuzu** yaratmak isteriz:

```python
def set_age(age):
    if age < 0:
        raise ValueError("Yaş negatif olamaz!")
    if age > 150:
        raise ValueError("Yaş çok büyük!")
    return age

# Kullanım
try:
    person_age = set_age(-5)
except ValueError as e:
    print(f"Hata: {e}")
    # Çıktı: Hata: Yaş negatif olamaz!
```

---

### 5.2 Özel Exception Sınıfları

```python
# Kendi exception'ımızı tanımlıyoruz
class InvalidAgeError(Exception):
    """Yaş hatasını belirtmek için özel exception"""
    pass

class InvalidNameError(Exception):
    """İsim hatasını belirtmek için özel exception"""
    pass

def create_person(name, age):
    if not isinstance(name, str) or len(name) == 0:
        raise InvalidNameError("İsim boş olamaz!")
    if age < 0 or age > 150:
        raise InvalidAgeError("Yaş 0-150 arasında olmalı!")
    return {"name": name, "age": age}

# Kullanım
try:
    person = create_person("", 25)
except InvalidNameError as e:
    print(f"İsim hatası: {e}")
except InvalidAgeError as e:
    print(f"Yaş hatası: {e}")
```

---

### 5.3 Hata Zincirleme

```python
try:
    x = int("abc")
except ValueError as e:
    # Orijinal hatayı koruyan yeni hata
    raise ValueError("Geçersiz giriş") from e
```

---

## 6. Pratik Örnek: Kullanıcıdan Doğrulanmış Sayı Okuma

### 6.1 Tam Kod

```python
def get_positive_number():
    """
    Kullanıcıdan pozitif bir sayı okur.
    Hatalı girişlerde uyarı verir ve tekrar sorar.
    
    Döndürüş:
        int: Pozitif bir sayı
    """
    while True:
        try:
            number = int(input("Lütfen pozitif bir sayı giriniz: "))
            if number > 0:
                return number
            else:
                print("❌ Lütfen 0'dan büyük bir sayı giriniz!")
        except ValueError:
            print("❌ Lütfen geçerli bir sayı giriniz!")

# Kullanım
result = get_positive_number()
print(f"✅ Başarılı! Sayınız: {result}")
```

### 6.2 Test Senaryoları

```
Senaryo 1: Pozitif sayı
Lütfen pozitif bir sayı giriniz: 42
✅ Başarılı! Sayınız: 42

Senaryo 2: Negatif sayı
Lütfen pozitif bir sayı giriniz: -5
❌ Lütfen 0'dan büyük bir sayı giriniz!
Lütfen pozitif bir sayı giriniz: 10
✅ Başarılı! Sayınız: 10

Senaryo 3: Harf giriş
Lütfen pozitif bir sayı giriniz: abc
❌ Lütfen geçerli bir sayı giriniz!
Lütfen pozitif bir sayı giriniz: 7
✅ Başarılı! Sayınız: 7
```

---

## 7. En İyi Uygulamalar (Best Practices)

### ✅ DOĞRU YÖNTEMLER

```python
# 1. Belirli exception'ları yakala
try:
    value = int(user_input)
except ValueError:
    print("Sayı gir!")

# 2. with bloğu ile dosya aç (otomatik kapatılır)
with open("file.txt", "r") as f:
    content = f.read()

# 3. Hata nesnesini kaydet
try:
    risky_code()
except Exception as e:
    logging.error(f"Hata: {e}", exc_info=True)

# 4. try bloğu hata kaynağını kapsasın
try:
    number = int(input(...))  # Hata BURADAN gelebilir
    if number > 0:
        return number
except ValueError:
    print("Hata!")

# 5. Özel exception tanımla
class CustomError(Exception):
    pass

try:
    risky_code()
except CustomError as e:
    print(f"Özel hata: {e}")
```

### ❌ YANLIŞ YÖNTEMLER

```python
# 1. Tüm hatalar görmezden gelinir
try:
    risky_code()
except:
    pass

# 2. Hata saklanır
try:
    risky_code()
except Exception:
    pass

# 3. try bloğu yanlış yerde
hata_kaynagi()  # Hata BURADAN gelebilir
try:
    if condition:
        code()
except ValueError:  # Hiç çalışmaz
    pass

# 4. Dosya elle kapatılmazsa, hata varsa açık kalır
f = open("file.txt", "r")
content = f.read()
f.close()  # Hata varsa çalışmaz!

# 5. Genel exception kullan
try:
    risky_code()
except Exception as e:  # Çok geniş
    print("Hata")
```

---

## 8. Özet Tablosu

| Konsept | Örnek | Kullanım |
|---------|-------|----------|
| **Syntax Error** | `if x = 5:` | Çalıştırmadan yakalanır |
| **ValueError** | `int("abc")` | Yanlış değer türü |
| **TypeError** | `"a" + 5` | Yanlış operand tipi |
| **IndexError** | `list[10]` | Olmayan indeks |
| **KeyError** | `dict["key"]` | Olmayan anahtar |
| **NameError** | `print(x)` | Tanımlanmamış değişken |
| **try/except** | Hata yakalama | Her zaman kullan |
| **else** | Hata yoksa | Başarı kodu |
| **finally** | Kaynak temizliği | `close()`, `cleanup()` |
| **raise** | Kendi hatası | Veri doğrulama |
| **with** | Dosya işlemleri | Otomatik kapatma |

---

## 9. Kaynaklar

- [Python Official Documentation — Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)
- [Python logging Module](https://docs.python.org/3/library/logging.html)

---

**Son Güncelleme:** 2026  
**Seviye:** Başlangıç → Orta  
**Süre:** 1-2 hafta pratik
