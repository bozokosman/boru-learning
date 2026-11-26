# Python Öğrenme Yolculuğu

---

## Bölüm 3: Data Structures

### 📖 Konu Özeti

Python'un dört temel veri yapısı bu bölümün kalbi. Her biri farklı bir problemi çözmek için tasarlanmış:

- **List** — sıralı, değiştirilebilir (mutable) koleksiyon. Üzerinde döngü kurulur, eleman eklenir/çıkarılır.
- **Tuple** — sıralı ama değiştirilemez (immutable). Sabit verileri tutmak için idealdir.
- **Set** — sırasız, tekrarsız koleksiyon. Küme işlemleri (birleşim, kesişim, fark) için kullanılır.
- **Dict** — anahtar-değer (key-value) çiftleri. Hızlı arama ve veri eşleştirme için kullanılır.

---

### 💡 Öğrendiklerim

**List Metotları**
- `append(x)` — listenin sonuna eleman ekler
- `extend(iterable)` — başka bir listeyi sona ekler
- `insert(i, x)` — belirtilen index'e eleman ekler
- `remove(x)` — ilk eşleşen elemanı siler
- `pop(i)` — index'teki elemanı siler ve döndürür; index verilmezse sonuncuyu alır
- `sort()` — listeyi yerinde sıralar, `None` döndürür
- `reverse()` — listeyi yerinde ters çevirir
- `count(x)` — elemanın kaç kez geçtiğini sayar
- `index(x)` — elemanın ilk geçtiği index'i döndürür
- `copy()` — sığ kopya (shallow copy) oluşturur
- `clear()` — tüm elemanları siler

**`sort()` vs `sorted()` Farkı**
- `list.sort()` → orijinal listeyi değiştirir, `None` döndürür
- `sorted(liste)` → orijinale dokunmaz, yeni bir liste döndürür

**List Comprehension**
- Döngü + append kombinasyonunu tek satırda yazmanın Pythonic yolu
- Şablon: `[ifade for eleman in liste if koşul]`

**Tuple**
- Immutable — oluşturulduktan sonra değiştirilemez
- Tek elemanlı tuple: `('hello',)` ← virgül zorunlu!
- Tuple packing: `t = 1, 2, 3`
- Sequence unpacking: `x, y, z = t`

**Set**
- Tekrar eden elemanları otomatik atar
- `|` birleşim, `&` kesişim, `-` fark, `^` simetrik fark
- Boş set: `set()` ← `{}` değil! (o dict oluşturur)

**Dict**
- Key'ler immutable olmak zorunda → list key olamaz, tuple olabilir
- Neden? Key'lerin hash değeri hesaplanır; mutable objeler hash'lenemez
- Aynı key'i iki kez tanımlarsan Python sonrakini kabul eder, öncekini siler
- `d[key]` → key yoksa `KeyError` fırlatır
- `d.get(key)` → key yoksa `None` döndürür (güvenli erişim)
- `d.items()` → key-value çiftlerini döndürür
- `d.keys()` → sadece key'leri döndürür
- `d.values()` → sadece value'ları döndürür

**Lambda**
- Tek satırlık, isimsiz fonksiyon
- `lambda x: x["point"]` → x'i al, point değerini döndür
- `sorted()` ile birlikte sıklıkla kullanılır: `key=lambda x: x["field"]`

**Döngü Teknikleri**
- `enumerate(liste)` → index + değer birlikte verir
- `zip(liste1, liste2)` → iki listeyi eşleştirir
- `sorted(set(liste))` → tekrarsız + sıralı döngü için klasik kombinasyon
- `reversed(liste)` → ters sırada döngü

**`del` Statement**
- `del liste[0]` → index'e göre siler (pop'tan farkı: değer döndürmez)
- `del liste[2:4]` → slice siler
- `del a` → değişkeni tamamen siler

---

### 🧠 En Zorlandığım Kavram

**Liste içinde dict yapısı** — başta her öğrenci için ayrı değişken açmak mantıklı geldi (`student1`, `student2`...). Ama 500 öğrenci olsaydı bu çökerdi. Doğru yaklaşım: tek bir liste içinde her öğrenci bir dict olarak tutulur, böylece döngüyle hepsini tek seferde işleyebilirsin.

---

### 💡 Keşfettiğim Nüanslar

- `sort()` `None` döndürür — `x = liste.sort()` yaparsak `x` boş olur. Python bunu kasıtlı tasarlamış: veriyi değiştiren metodlar `None` döndürür, böylece yanlışlıkla atama yapılmaz.
- Dict'te `{}` boş dict oluşturur, boş set için `set()` yazmak gerekir.
- `list` key olamaz çünkü mutable → hash'lenemez. `tuple` key olabilir çünkü immutable → hash'i sabittir.
- List comprehension'da `print()` kullanmak `None` dolu bir liste üretir — comprehension içine ifade yazılır, `print` değil.

---

### 💻 Kod Örneği

```python
students = [
    {"name": "Ali", "point": [50, 60, 70]},
    {"name": "Veli", "point": [60, 70, 80]},
    {"name": "Mehmet", "point": [70, 80, 90]},
    {"name": "Fatma", "point": [80, 90, 100]},
    {"name": "Ayse", "point": [40, 50, 60]}
]

# Her öğrencinin ortalamasını hesapla ve yeni listeye kaydet
students_avg = []
for student in students:
    students_avg.append({
        "name": student["name"],
        "point": sum(student["point"]) / len(student["point"])
    })

# Ortalamalara göre en yüksekten en düşüğe sırala
sequential = sorted(students_avg, key=lambda x: x["point"], reverse=True)
print(sequential)

# Ortalaması 70 ve üzeri olan öğrencileri listele
for student in sequential:
    if student["point"] >= 70:
        print(student)
```

**List Comprehension versiyonu:**
```python
# Ortalama hesaplama — tek satır
students_avg = [
    {"name": s["name"], "point": sum(s["point"]) / len(s["point"])}
    for s in students
]

# Filtreleme — tek satır
basarili = [s for s in sequential if s["point"] >= 70]
print(basarili)
```

---

### 🔗 Kaynak

- [Python Resmi Dokümantasyon - Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
