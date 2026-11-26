# Python Öğrenme Yolculuğu

---

## Bölüm 2: Control Flow

### 📖 Konu Özeti
...

### 💡 Öğrendiklerim
- `if / elif / else` — koşullu dallanma; programın hangi yolu izleyeceğini belirler
- `for` — bir dizinin (liste, string, range vb.) üzerinde sırayla iterasyon yapar
- `range()` — sayı dizisi üreten iterable; liste değil, lazy evaluation ile çalışır
- `break` — döngüyü anında durdurur
- `continue` — o anki adımı atlayıp döngüye devam eder
- `while` — koşul doğru olduğu sürece döngüyü çalıştırır
- `for ... else` — döngü `break`'siz tamamlanırsa `else` bloğu çalışır
- `pass` — sözdizimsel olarak bir şey yazman gerektiğinde, mantıksal işlem istemediğinde kullanılır
- `def` — fonksiyon tanımlamak için kullanılır
- `return` — fonksiyondan değer döndürür; çalıştığı anda fonksiyon biter
- `*args / **kwargs` — esnek sayıda argüman almak için kullanılır
- `lambda` — tek satırlık anonim fonksiyonlar
- Docstring — fonksiyonun ne yaptığını açıklayan belgeleme metni

### 🧠 En Zorlandığım Kavram
...

### 💡 Keşfettiğim Nüanslar
- `return` varsa `break` gereksizdir — `return` zaten fonksiyonu ve döngüyü durdurur
- `range(10)` bir liste değildir; bellekte tüm elemanları tutmaz, anlık üretir (lazy evaluation)
- `for ... else` yapısında `else`, döngü `break` ile kesilmeden tamamlanırsa çalışır
- Fonksiyonun tek bir görevi olmalı — "bu sayı asal mı?" sorusunu cevaplamak, aralık bulmak değil

### 💻 Kod Örneği

```python
number1 = int(input("Lütfen ilk sayınızı giriniz: "))
number2 = int(input("Lütfen ikinci sayınızı giriniz: "))


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True


while True:
    if number1 < number2:
        for i in range(number1, number2):
            if is_prime(i) == True:
                print(i)
        break
    else:
        print("İlk sayınız, ikinci sayınızdan küçük olamaz. Lütfen tekrar deneyiniz.")
        number1 = int(input("Lütfen ilk sayınızı giriniz: "))
        number2 = int(input("Lütfen ikinci sayınızı giriniz: "))
```

### 🔗 Kaynak
- [Python Resmi Dokümantasyon - Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
