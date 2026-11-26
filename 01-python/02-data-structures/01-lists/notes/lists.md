# Lists

## 1. Liste Nedir?

Python'da `list`, birden fazla değeri tek bir değişkende saklamak için kullanılan veri yapısıdır.

```python
books = ["Python101", "Clean Code", "Computer Science"]
```

Bir liste:

* Birden fazla değer tutabilir.
* Elemanların sırasını korur.
* Değiştirilebilir (`mutable`).
* Farklı veri tiplerini aynı listede tutabilir.

```python
data = ["Osman", 32, True, 95.5]
```

---

## 2. Liste Elemanlarına Erişim

Python listelerinde indeksler `0`'dan başlar.

```python
books = ["Python101", "Clean Code", "Computer Science"]

print(books[0])
print(books[1])
print(books[2])
```

Sonuç:

```text
Python101
Clean Code
Computer Science
```

İlk elemanın indeksi `0`, ikinci elemanın indeksi `1` olur.

---

## 3. Negatif İndeks

Negatif indeksler listenin sonundan başlayarak erişim sağlar.

```python
books = ["Python101", "Clean Code", "Computer Science"]

print(books[-1])
print(books[-2])
```

Sonuç:

```text
Computer Science
Clean Code
```

`-1`, listenin son elemanıdır.

---

## 4. Eleman Değiştirme

Listeler değiştirilebilir.

```python
books = ["Python101", "Clean Code", "Computer Science"]

books[0] = "Python Advanced"

print(books)
```

Sonuç:

```text
["Python Advanced", "Clean Code", "Computer Science"]
```

Burada listenin ilk elemanı değiştirilmiştir.

---

## 5. Liste Uzunluğu

`len()` listenin kaç eleman içerdiğini verir.

```python
books = ["Python101", "Clean Code", "Computer Science"]

print(len(books))
```

Sonuç:

```text
3
```

---

## 6. `append()`

`append()` listenin sonuna yeni bir eleman ekler.

```python
books = ["Python101", "Clean Code"]

books.append("Computer Science")

print(books)
```

Sonuç:

```text
["Python101", "Clean Code", "Computer Science"]
```

Mini Library projemizde kullandığımız:

```python
self.books.append(book)
```

yapısının temelinde de bu davranış vardır.

Burada `book`, listeye eklenen nesnedir.

---

## 7. `insert()`

`insert()` belirli bir indekse eleman ekler.

```python
books = ["Python101", "Computer Science"]

books.insert(1, "Clean Code")

print(books)
```

Sonuç:

```text
["Python101", "Clean Code", "Computer Science"]
```

İlk parametre indeks, ikinci parametre eklenecek değerdir.

---

## 8. `remove()`

`remove()` verilen değeri listeden kaldırır.

```python
books = ["Python101", "Clean Code", "Computer Science"]

books.remove("Clean Code")

print(books)
```

Sonuç:

```text
["Python101", "Computer Science"]
```

`remove()` elemanın indeksini değil, değerini kullanır.

---

## 9. `pop()`

`pop()` belirtilen indeksteki elemanı listeden çıkarır ve çıkarılan elemanı geri döndürür.

```python
books = ["Python101", "Clean Code", "Computer Science"]

removed_book = books.pop(1)

print(removed_book)
print(books)
```

Sonuç:

```text
Clean Code
["Python101", "Computer Science"]
```

Parametre verilmezse son eleman çıkarılır:

```python
books.pop()
```

---

## 10. `del`

`del` belirli bir indeks veya dilim üzerinden eleman silmek için kullanılabilir.

```python
books = ["Python101", "Clean Code", "Computer Science"]

del books[1]

print(books)
```

Sonuç:

```text
["Python101", "Computer Science"]
```

`del` ile değişkenin kendisi de silinebilir:

```python
book = "Python101"

del book
```

---

## 11. `in`

`in`, bir elemanın listede bulunup bulunmadığını kontrol eder.

```python
books = ["Python101", "Clean Code", "Computer Science"]

print("Python101" in books)
print("Java" in books)
```

Sonuç:

```text
True
False
```

Bu özellikle arama işlemlerinde kullanışlıdır.

---

## 12. `not in`

Bir değerin listede bulunmadığını kontrol etmek için `not in` kullanılabilir.

```python
books = ["Python101", "Clean Code"]

if "Java" not in books:
    print("Java listede bulunmuyor.")
```

---

## 13. Listeler ve `for`

Listeler üzerinde `for` döngüsüyle dolaşabiliriz.

```python
books = ["Python101", "Clean Code", "Computer Science"]

for book in books:
    print(book)
```

Her döngü turunda `book`, listenin bir elemanını temsil eder.

---

## 14. Liste Dilimleme

Listelerden belirli bir bölüm alınabilir.

```python
numbers = [0, 1, 2, 3, 4, 5]

print(numbers[1:4])
```

Sonuç:

```text
[1, 2, 3]
```

Başlangıç indeksi dahil edilir, bitiş indeksi dahil edilmez.

---

## 15. Adımlı Dilimleme

Dilimleme üçüncü bir parametre ile adım alabilir.

```python
numbers = [0, 1, 2, 3, 4, 5]

print(numbers[0:6:2])
```

Sonuç:

```text
[0, 2, 4]
```

---

## 16. Listeyi Ters Çevirmek

Dilimleme kullanılarak liste ters çevrilebilir.

```python
numbers = [1, 2, 3, 4, 5]

print(numbers[::-1])
```

Sonuç:

```text
[5, 4, 3, 2, 1]
```

---

## 17. `sort()`

`sort()` listenin elemanlarını sıralar.

```python
numbers = [5, 2, 8, 1, 3]

numbers.sort()

print(numbers)
```

Sonuç:

```text
[1, 2, 3, 5, 8]
```

Ters sıralama için:

```python
numbers.sort(reverse=True)
```

---

## 18. `reverse()`

`reverse()` listenin mevcut sırasını tersine çevirir.

```python
books = ["Python101", "Clean Code", "Computer Science"]

books.reverse()

print(books)
```

Bu işlem alfabetik sıralama yapmaz. Sadece mevcut sırayı tersine çevirir.

---

## 19. `count()`

`count()` belirli bir değerin listede kaç kez bulunduğunu verir.

```python
numbers = [1, 2, 2, 3, 2, 4]

print(numbers.count(2))
```

Sonuç:

```text
3
```

---

## 20. `index()`

`index()` verilen değerin listedeki ilk bulunduğu indeksini döndürür.

```python
books = ["Python101", "Clean Code", "Computer Science"]

print(books.index("Clean Code"))
```

Sonuç:

```text
1
```

---

## 21. Listeleri Birleştirme

İki liste `+` operatörüyle birleştirilebilir.

```python
books1 = ["Python101", "Clean Code"]
books2 = ["Computer Science", "Developer101"]

books = books1 + books2

print(books)
```

Sonuç:

```text
["Python101", "Clean Code", "Computer Science", "Developer101"]
```

---

## 22. Liste İçinde Liste

Listeler başka listeleri de eleman olarak tutabilir.

```python
library = [
    ["Python101", "Osman"],
    ["Clean Code", "Robert C. Martin"]
]
```

Bu yapı iç içe listeler oluşturur.

Daha sonra daha gelişmiş veri yapıları çalışırken bu tür yapılar daha detaylı ele alınacaktır.

---

## 23. Liste ve Nesneler

Python listeleri yalnızca string, sayı veya boolean değerleri tutmak zorunda değildir.

Nesneler de liste içerisinde tutulabilir.

```python
books = []

book1 = Book("Python101", "Osman Bozok", 100, "Programming")
book2 = Book("Clean Code", "Robert C. Martin", 464, "Programming")

books.append(book1)
books.append(book2)
```

Böylece liste içerisinde `Book` nesneleri bulunur.

Mini Library projemizde kullandığımız yapı tam olarak buna dayanır:

```python
self.books.append(book)
```

Burada `self.books` bir listedir ve içerisine `Book` nesneleri eklenmektedir.

Bu, basit listelerden nesne tabanlı programlamaya geçişte önemli bir bağlantıdır.

---

## 24. Liste Üzerinde Döngü ve Nesne

Bir listedeki nesneler üzerinde döngü kurulabilir.

```python
for book in books:
    print(book.name)
```

Burada:

* `books` → `Book` nesnelerini tutan liste
* `book` → o anki `Book` nesnesi
* `book.name` → nesnenin `name` özelliği

olur.

Mini Library'deki kitap arama mantığının temelinde de bu yapı vardır.

---

## Özet

Python listeleri:

* Birden fazla değer saklamak için kullanılır.
* Sıralıdır.
* Değiştirilebilirdir.
* İndekslerle erişilebilir.
* Döngülerle gezilebilir.
* İçerisinde nesneler dahil farklı veri tipleri tutulabilir.

Temel liste işlemleri:

| İşlem       | Amaç                               |
| ----------- | ---------------------------------- |
| `len()`     | Eleman sayısını bulmak             |
| `append()`  | Sona eleman eklemek                |
| `insert()`  | Belirli indekse eleman eklemek     |
| `remove()`  | Değere göre eleman silmek          |
| `pop()`     | Elemanı çıkarıp geri döndürmek     |
| `del`       | Eleman veya dilim silmek           |
| `in`        | Eleman var mı kontrol etmek        |
| `sort()`    | Listeyi sıralamak                  |
| `reverse()` | Mevcut sırayı ters çevirmek        |
| `count()`   | Bir değerin tekrar sayısını bulmak |
| `index()`   | Bir değerin ilk indeksini bulmak   |

Listeler Python'da çok temel bir veri yapısıdır ve daha ileri konularda, özellikle nesnelerle çalışırken, sürekli karşımıza çıkacaktır.

