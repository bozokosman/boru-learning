# Sets

> 🇬🇧 [Click here for English documentation](README.md)

## 1. Set Nedir?
Set, Python'da birden fazla değeri tek bir yapı içerisinde saklamak için kullanılan veri tipidir.

Set'lerin en önemli özellikleri:
- Benzersiz elemanlar saklar.
- Aynı elemanı birden fazla kez saklamaz.
- İndeksleme desteklemez.
- Değiştirilebilir bir veri yapısıdır.
- Küme işlemlerini destekler.

```python
numbers = {10, 20, 30, 40}

print(numbers)
```

## 2. Set Oluşturma
Set oluşturmak için süslü parantezler kullanılabilir.

```python
numbers = {10, 20, 30}
```
String değerlerden oluşan bir set:
```python
books = {
    "Python101",
    "Clean Code",
    "Computer Science"
}
```

## 3. Duplicate Elemanlar
Set aynı değeri birden fazla kez saklamaz.

```python
numbers = {10, 20, 20, 30, 30, 30}

print(numbers)
```
Sonuçta her değer yalnızca bir kez bulunur. Bu özellik özellikle tekrar eden verileri temizlemek için kullanışlıdır.

## 4. Boş Set
Boş bir set oluşturmak için sadece `{}` kullanılamaz.

```python
empty_set = set()
```
Çünkü:
```python
empty = {}
```
ifadesi boş bir dictionary oluşturur.

## 5. Set'e Eleman Ekleme
Set'e tek bir eleman eklemek için `add()` kullanılır.

```python
books = {"Python101", "Clean Code"}

books.add("Computer Science")

print(books)
```

## 6. Birden Fazla Eleman Ekleme
Birden fazla eleman eklemek için `update()` kullanılabilir.

```python
books = {"Python101"}

books.update({
    "Clean Code",
    "Computer Science",
    "The Pragmatic Programmer"
})

print(books)
```
`update()` bir iterable içerisindeki elemanları sete ekler.

## 7. Eleman Silme — remove()
Belirli bir elemanı silmek için `remove()` kullanılabilir.

```python
books = {
    "Python101",
    "Clean Code",
    "Computer Science"
}

books.remove("Clean Code")

print(books)
```
Eğer eleman sette yoksa `remove()` hata verir.

## 8. Eleman Silme — discard()
`discard()` da eleman siler. Ancak eleman sette bulunmuyorsa hata vermez.

```python
books = {
    "Python101",
    "Clean Code"
}

books.discard("Computer Science")

print(books)
```
Bu nedenle `remove()` ve `discard()` arasındaki fark önemlidir.

## 9. pop()
`pop()` set içerisinden bir elemanı siler ve silinen elemanı döndürür.

```python
books = {
    "Python101",
    "Clean Code",
    "Computer Science"
}

removed_book = books.pop()

print(removed_book)
print(books)
```
Set indeksli olmadığı için hangi elemanın silineceğine güvenilmemelidir.

## 10. clear()
Set içerisindeki bütün elemanları silmek için `clear()` kullanılır.

```python
books = {
    "Python101",
    "Clean Code"
}

books.clear()

print(books)
```
Sonuç:
```python
set()
```

## 11. len()
Set içerisindeki eleman sayısını bulmak için `len()` kullanılabilir.

```python
numbers = {10, 20, 30, 40}

print(len(numbers))
```

## 12. in
Bir elemanın set içerisinde bulunup bulunmadığını kontrol etmek için `in` kullanılabilir.

```python
books = {
    "Python101",
    "Clean Code"
}

print("Python101" in books)
print("C++" in books)
```

## 13. Set Üzerinde for
Set üzerinde for döngüsü kullanılabilir.

```python
books = {
    "Python101",
    "Clean Code",
    "Computer Science"
}

for book in books:
    print(book)
```
Set indeksli olmadığı için:
```python
books[0]
```
gibi bir kullanım yapılamaz.

## 14. Set Union
İki setin bütün elemanlarını birleştirmek için `union` işlemi kullanılabilir.

```python
python_books = {
    "Python101",
    "Python Advanced"
}

programming_books = {
    "Clean Code",
    "Python101"
}

result = python_books.union(programming_books)

print(result)
```
`|` operatörü de union işlemi için kullanılabilir.
```python
result = python_books | programming_books
```
Aynı elemanlar sonuçta yalnızca bir kez bulunur.

## 15. Set Intersection
İki sette ortak bulunan elemanları bulmak için `intersection` kullanılır.

```python
python_books = {
    "Python101",
    "Clean Code",
    "Python Advanced"
}

programming_books = {
    "Python101",
    "Clean Code",
    "C++"
}

result = python_books.intersection(programming_books)

print(result)
```
`&` operatörü de kullanılabilir.
```python
result = python_books & programming_books
```

## 16. Set Difference
Bir sette olup diğer sette olmayan elemanları bulmak için `difference` kullanılır.

```python
python_books = {
    "Python101",
    "Clean Code",
    "Python Advanced"
}

programming_books = {
    "Python101",
    "C++"
}

result = python_books.difference(programming_books)

print(result)
```
`-` operatörü de kullanılabilir.
```python
result = python_books - programming_books
```

## 17. Symmetric Difference
İki sette bulunan fakat her ikisinde ortak olmayan elemanları bulmak için `symmetric_difference` kullanılabilir.

```python
set1 = {
    1,
    2,
    3
}

set2 = {
    3,
    4,
    5
}

result = set1.symmetric_difference(set2)

print(result)
```
`^` operatörü de kullanılabilir.
```python
result = set1 ^ set2
```
Sonuç:
```python
{1, 2, 4, 5}
```

## 18. Set Karşılaştırmaları
Set'ler birbirleriyle karşılaştırılabilir.

**issubset()**
Bir setin diğer setin alt kümesi olup olmadığını kontrol eder.
```python
small = {1, 2}
large = {1, 2, 3, 4}

print(small.issubset(large))
```

**issuperset()**
Bir setin diğer seti kapsayıp kapsamadığını kontrol eder.
```python
large = {1, 2, 3, 4}
small = {1, 2}

print(large.issuperset(small))
```

**isdisjoint()**
İki sette ortak eleman bulunup bulunmadığını kontrol eder.
```python
set1 = {1, 2, 3}
set2 = {4, 5, 6}

print(set1.isdisjoint(set2))
```

## 19. Set ve List Arasındaki Temel Fark
**List:**
```python
books = [
    "Python101",
    "Clean Code",
    "Python101"
]
```
List aynı elemanı birden fazla kez saklayabilir.

**Set:**
```python
books = {
    "Python101",
    "Clean Code",
    "Python101"
}
```
Set tekrar eden elemanları tekilleştirir.

## 20. Listeden Set Oluşturma
Bir listeden set oluşturulabilir.

```python
numbers = [
    10,
    20,
    20,
    30,
    30,
    40
]

unique_numbers = set(numbers)

print(unique_numbers)
```
Bu yöntem tekrar eden değerleri temizlemek için kullanılabilir.

## 21. Set'ten Liste Oluşturma
Bir set tekrar listeye dönüştürülebilir.

```python
numbers = {10, 20, 30}

numbers_list = list(numbers)

print(numbers_list)
```

## 22. Set ve Dictionary Farkı
İkisi de `{}` kullanabildiği için başlangıçta karıştırılabilir.

**Set:**
```python
books = {
    "Python101",
    "Clean Code"
}
```

**Dictionary:**
```python
book = {
    "name": "Python101",
    "author": "Osman Bozok"
}
```
Set değerlerden oluşur. Dictionary ise key: value çiftlerinden oluşur.

Boş yapı oluştururken:
- `set()` boş set,
- `{}` ise boş dictionary oluşturur.

## 23. Özet
**Set:**
- Benzersiz elemanlar saklar.
- Duplicate değerleri kaldırır.
- İndeksleme desteklemez.
- `add()` ile eleman eklenebilir.
- `update()` ile birden fazla eleman eklenebilir.
- `remove()` ve `discard()` ile eleman silinebilir.
- `pop()` ile bir eleman kaldırılabilir.
- `clear()` bütün elemanları siler.
- `union()` iki seti birleştirir.
- `intersection()` ortak elemanları bulur.
- `difference()` farklı elemanları bulur.
- `symmetric_difference()` ortak olmayan elemanları bulur.
- `issubset()` alt küme kontrolü yapar.
- `issuperset()` üst küme kontrolü yapar.
- `isdisjoint()` ortak eleman kontrolü yapar.

Temel set oluşturma:
```python
numbers = {1, 2, 3, 4}
```
Temel eleman ekleme:
```python
numbers.add(5)
```
Temel üyelik kontrolü:
```python
print(3 in numbers)
```
Set'lerin en güçlü kullanım alanlarından biri tekrar eden değerleri temizlemektir:
```python
numbers = [1, 2, 2, 3, 3, 4]

unique_numbers = set(numbers)

print(unique_numbers)
```
