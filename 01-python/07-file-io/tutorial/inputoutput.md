# 📚 Python — Input & Output

## 1. Çıktı Formatlama

### 1.1 f-string (En Modern Yol)

Stringin başına `f` koy, süslü parantez `{}` içine Python ifadesi yaz.

```python
year = 2016
event = "Referendum"
print(f"Results of the {year} {event}")
# Çıktı: Results of the 2016 Referendum
```

#### Format Specifier'lar

```python
# Ondalık basamak
print(f"{3.14159:.2f}")       # → 3.14

# Minimum genişlik
print(f"{'Ali':10} ==> {4127:10d}")  # → Ali        ==>       4127

# Debug modu (= operatörü)
count = 13
print(f"{count=}")            # → count=13

# repr() uygula
animals = "eels"
print(f"{animals!r}")         # → 'eels'
```

| Syntax | Ne yapar? |
|--------|-----------|
| `{deger:.3f}` | 3 ondalık basamak float |
| `{deger:10d}` | Min 10 karakter genişliğinde integer |
| `{deger:10}` | Min 10 karakter genişliğinde string |
| `{deger!r}` | `repr()` uygular |
| `{deger!s}` | `str()` uygular |
| `{deger=}` | İsim ve değeri birlikte yazar |

---

### 1.2 str.format() Metodu

```python
# Pozisyon ile
print("{0} and {1}".format("spam", "eggs"))
# → spam and eggs

# İsim ile
print("{food} is {adj}.".format(food="spam", adj="horrible"))
# → spam is horrible.

# Dict ile (**) operatörü
table = {"Jack": 4098, "Sjoerd": 4127}
print("Jack: {Jack:d}; Sjoerd: {Sjoerd:d}".format(**table))
```

---

### 1.3 Manuel Formatlama (str Metodları)

```python
print("42".rjust(5))    # '   42'  → sağa yasla
print("42".ljust(5))    # '42   '  → sola yasla
print("42".center(5))   # ' 42  '  → ortala
print("42".zfill(5))    # '00042'  → soluna sıfır doldur
```

---

### 1.4 str() vs repr()

```python
s = "Hello\n"
print(str(s))    # Hello        → insan için okunabilir
print(repr(s))   # 'Hello\n'   → Python yorumlayıcısı için
```

- `str()` → **insan için** okunabilir çıktı
- `repr()` → **debug için**, Python'ın gördüğü hali

---

## 2. Dosya Okuma ve Yazma

### 2.1 open() — Mod Parametreleri

```python
f = open("dosya.txt", "r", encoding="utf-8")
```

| Mod | Anlamı |
|-----|--------|
| `"r"` | Sadece oku (dosya yoksa hata verir) |
| `"w"` | Sadece yaz (varsa siler, sıfırdan başlar) |
| `"a"` | Ekle (dosya varsa sonuna ekler) |
| `"r+"` | Hem oku hem yaz |
| `"rb"` | Binary modda oku |
| `"wb"` | Binary modda yaz |

> ⚠️ Türkçe karakterler için her zaman `encoding="utf-8"` kullan!

---

### 2.2 with Bloğu (Altın Kural)

```python
with open("dosya.txt", "r", encoding="utf-8") as f:
    icerik = f.read()
# Blok bitince dosya otomatik kapanır
```

**Neden `with` kullanmalısın?**
- Hata olsa bile dosyayı otomatik kapatır
- Yazılan verinin diske tam yazılmasını garantiler
- `f.close()` unutma riskini ortadan kaldırır

---

### 2.3 Dosya Okuma Metodları

```python
with open("dosya.txt", encoding="utf-8") as f:

    # Tüm dosyayı tek string olarak al
    icerik = f.read()

    # Tek satır oku
    satir = f.readline()

    # Tüm satırları liste olarak al (RAM'e çeker!)
    satirlar = f.readlines()

    # Satır satır döngü (büyük dosyalar için en güvenli)
    for satir in f:
        print(satir, end="")
```

#### Büyük Dosya Kuralı

```python
# ✅ Büyük dosya — satır satır, az RAM kullanır
with open("buyuk.txt", encoding="utf-8") as f:
    for satir in f:
        print(satir)

# ❌ Büyük dosya — tüm dosyayı RAM'e çeker, tehlikeli!
with open("buyuk.txt", encoding="utf-8") as f:
    satirlar = f.readlines()
```

---

### 2.4 Dosyaya Yazma

```python
with open("dosya.txt", "w", encoding="utf-8") as f:
    f.write("Merhaba dünya\n")  # kaç karakter yazıldığını döner

    # String olmayan tipleri dönüştür
    value = ("cevap", 42)
    f.write(str(value))
```

---

### 2.5 append() vs extend()

```python
myList = []
myList.append(["a", "b", "c"])   # → [["a", "b", "c"]]  liste içinde liste!
myList.extend(["a", "b", "c"])   # → ["a", "b", "c"]    açarak ekler

# Ama en temizi:
myList = file.readlines()         # direkt atama
```

---

## 3. JSON ile Veri Kaydetme

```python
import json

# Python → JSON string
x = [1, "simple", "list"]
json_str = json.dumps(x)           # '[1, "simple", "list"]'

# Python → Dosyaya yaz
with open("veri.json", "w", encoding="utf-8") as f:
    json.dump(x, f, ensure_ascii=False)  # Türkçe için ensure_ascii=False!

# Dosyadan oku → Python
with open("veri.json", "r", encoding="utf-8") as f:
    data = json.load(f)
```

| Fonksiyon | Ne yapar? |
|-----------|-----------|
| `json.dumps(x)` | Python → **string** |
| `json.dump(x, f)` | Python → **dosyaya** yazar |
| `json.loads(s)` | JSON string → **Python** |
| `json.load(f)` | JSON dosyası → **Python** |

> ⚠️ `ensure_ascii=False` olmadan Türkçe karakterler `\u00f6` gibi görünür!

---

## 4. Tam Örnek

```python
import json

# txt dosyasını oku
with open("notlar.txt", "r", encoding="utf-8") as f:
    myList = f.readlines()
print(myList)

# JSON olarak kaydet
with open("notlar.json", "w", encoding="utf-8") as j:
    json.dump(myList, j, ensure_ascii=False)

# JSON'dan geri oku
with open("notlar.json", "r", encoding="utf-8") as j:
    myList_last = json.load(j)
print(myList_last)
```
