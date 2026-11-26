# Python Öğrenme Yolculuğu

---

## Bölüm 4: Modules

### 📖 Konu Özeti

Modüller, Python'da kodu dosyalara bölüp yeniden kullanılabilir hale getirmenin temel yoludur. Python interpreter'ı kapattığında yazdığın her şey kaybolur — modüller bu sorunu çözer. Bir `.py` dosyası hem bağımsız script olarak hem de başka dosyalar tarafından import edilebilen kütüphane olarak kullanılabilir.

---

### 💡 Öğrendiklerim

#### Import Yöntemleri

**`import modül`** — Modülün tamamını namespace'e alır, fonksiyonlara `modül.fonksiyon()` ile erişilir.
```python
import fibo
fibo.fib(100)   # ✅ Doğru
fib(100)        # ❌ NameError — fib bu namespace'de yok
```

**`from modül import fonksiyon`** — Sadece belirtilen ismi direkt namespace'e alır.
```python
from fibo import fib, fib2
fib(100)        # ✅ Direkt kullanılabilir
fibo.fib(100)   # ❌ fibo bu namespace'de yok
```

**`import modül as takmaad`** — Modüle kısa takma ad verir.
```python
import numpy as np       # Gerçek hayatta sık kullanılan kalıp
import pandas as pd
```

**`from modül import fonksiyon as takmaad`** — Fonksiyona takma ad verir.
```python
from fibo import fib as fibonacci
fibonacci(100)
```

**`from modül import *`** — Modüldeki her şeyi alır. Üretim kodunda kullanılmaz, isim çakışmasına yol açar.

---

#### Hangi Import Yöntemi Ne Zaman?

| Durum | Tercih |
|---|---|
| Modülden az sayıda fonksiyon kullanacaksan | `from matematik import topla, carp` |
| Modülü yoğun kullanacaksan | `import matematik` → `matematik.carp()` |
| İsim çakışması riski varsa | `import modül` (namespace korumalı) |
| Uzun modül adını kısaltmak istersen | `import numpy as np` |

---

#### `__name__` ve `if __name__ == "__main__"`

Her Python dosyasına çalışma anında otomatik `__name__` değişkeni atanır:

| Kullanım | `__name__` değeri |
|---|---|
| `python dosya.py` (direkt çalıştırma) | `"__main__"` |
| Başka dosyadan `import dosya` | `"dosya"` |

**Neden önemli?** Dosyanın sonundaki test/çalıştırma kodları, import edildiğinde de tetiklenir. Bunu önlemek için:

```python
def topla(a, b):
    return a + b

def carp(a, b):
    return a * b

if __name__ == "__main__":
    # Sadece "python matematik.py" dediğinde çalışır
    # import edilince bu blok hiç çalışmaz
    print("Test modu")
    print(topla(2, 3))
```

**Gerçek hayat senaryosu:** Dosyada `input()`, `print()` veya veritabanı bağlantısı varsa ve bunu `if __name__` ile korumadıysan, başka biri sadece import etmek istese bile bunlar tetiklenir. `if __name__ == "__main__"` bu kapıyı kapatır.

---

#### Namespace Kavramı

`import fibo` dediğinde `fib` fonksiyonu senin namespace'ine **girmez**, sadece `fibo` ismi girer. Python bunu kasıtlı yapar — farklı modüllerde aynı isimde fonksiyonlar olabilir, birbirini ezmemesi için.

```python
import fibo
import baska_modul   # bu modülde de fib() olabilir

fibo.fib(100)            # hangisi olduğu net
baska_modul.fib(100)     # hangisi olduğu net
```

---

#### `dir()` Fonksiyonu

Bir modülün içinde ne olduğunu görmek için kullanılır:

```python
import fibo
print(dir(fibo))    # ['__name__', 'fib', 'fib2']
```

Argümansız çağırırsan, o an aktif namespace'deki her şeyi listeler:

```python
x = 5
import fibo
print(dir())    # ['__builtins__', '__name__', 'fibo', 'x']
```

---

#### Module Search Path — Python Modülü Nereden Bulur?

`import spam` dediğinde Python şu sırayla arar:

1. **Built-in modüller** (`sys`, `os` gibi — Python'a gömülü)
2. **`sys.path`** listesindeki klasörler:
   - Önce çalıştırılan dosyanın bulunduğu klasör
   - `PYTHONPATH` ortam değişkenindeki yollar
   - Python'un kurulu olduğu standart kütüphane klasörleri

```python
import sys
print(sys.path)   # Arama yapılan klasörleri listeler
```

---

#### Packages — Modüllerin Modülü

Büyük projelerde modüller klasörlere bölünür. Bu klasörlere **package** denir. Bir klasörün package sayılması için içinde `__init__.py` dosyası olması gerekir.

```
myproject/
    sound/
        __init__.py        ← Bu olmadan Python klasörü package saymaz
        effects/
            __init__.py
            echo.py
            surround.py
```

```python
import sound.effects.echo                   # Tam yol
from sound.effects import echo              # Alt modülü direkt al
from sound.effects.echo import echofilter  # Fonksiyonu direkt al
```

**Relative import** — Paket içindeki modüller birbirini şöyle çağırır:

```python
from . import echo          # Aynı klasördeki echo.py
from .. import formats      # Bir üst klasördeki formats.py
from ..filters import equalizer
```

---

### 🧠 En Zorlandığım Kavram

**`if __name__ == "__main__"` mantığı** — Başta soyut geldi. Ama şu analoji netleştirdi: bir pizza tarifi defterini sen kendin kullanırsan yemek yaparsın, arkadaşın ödünç alırsa sadece malzeme listesine bakar. `__name__` değişkeni tam olarak "bu dosya şu an hangi rolde?" sorusunun cevabı.

---

### 💡 Keşfettiğim Nüanslar

- `import fibo` ile `from fibo import fib` sadece yazım kolaylığı farkı değil — namespace'e giren isim farklı. Birinde `fibo`, diğerinde `fib` girer.
- `from modül import *` kullanmak production kodda anti-pattern sayılır — hangi ismin nereden geldiği belli olmaz.
- Her modül sadece **bir kez** import edilir. Aynı modülü iki dosyadan import etsen bile Python ikinci seferinde cache'den alır.
- `__pycache__` klasörü Python'un otomatik oluşturduğu derleme cache'i — sen oluşturmazsın, silersen de Python yeniden oluşturur.

---

### 💻 Kod Örneği

```python
# matematik.py
def topla(a, b):
    return a + b

def carp(a, b):
    return a * b

if __name__ == "__main__":
    print("Test modu")
    print(topla(2, 3))   # 5
    print(carp(3, 4))    # 12
```

```python
# main.py — Seçici import
from matematik import topla

print(topla(3, 5))   # 8
# print(carp(3, 5))  # ❌ NameError — import edilmedi
```

```python
# main.py — Modül bazlı import (yoğun kullanım için)
import matematik

print(matematik.topla(3, 5))   # 8
print(matematik.carp(3, 4))    # 12
```

---

### 🔗 Kaynak

- [Python Resmi Dokümantasyon - Modules](https://docs.python.org/3/tutorial/modules.html)
