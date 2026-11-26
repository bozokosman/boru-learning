# Conditions

## 1. Koşullar Nedir?

Programların yalnızca verilen komutları sırayla çalıştırması her zaman yeterli değildir.

Bazı durumlarda programın bir durumu kontrol etmesi ve sonuca göre farklı bir işlem yapması gerekir.

Python'da bu karar mekanizması `if`, `elif` ve `else` yapılarıyla oluşturulur.

Örneğin:

```python
age = 20

if age >= 18:
    print("Giriş yapabilirsiniz.")
```

Burada Python önce:

```python
age >= 18
```

koşulunu değerlendirir.

Sonuç `True` ise `if` bloğunun içerisindeki kod çalışır.

---

## 2. `if`

`if`, bir koşul doğru olduğunda belirli kodların çalışmasını sağlar.

```python
age = 25

if age >= 18:
    print("Yetişkinsiniz.")
```

Koşul:

```python
age >= 18
```

`True` olduğu için mesaj yazdırılır.

Koşul `False` olsaydı `if` bloğunun içindeki kod çalışmazdı.

---

## 3. Girintileme

Python'da koşul bloğunun hangi kodlardan oluştuğu girintileme ile belirlenir.

```python
age = 25

if age >= 18:
    print("Yetişkinsiniz.")
    print("Giriş yapabilirsiniz.")
```

İki `print()` de `if` bloğunun içerisindedir.

Girintisiz bir kod ise bloğun dışında olur:

```python
age = 25

if age >= 18:
    print("Yetişkinsiniz.")

print("Program devam ediyor.")
```

Python'da girintileme yalnızca görünüş için değildir. Programın yapısının bir parçasıdır.

---

## 4. `else`

`else`, `if` koşulu yanlış olduğunda çalışacak kodu belirtir.

```python
age = 16

if age >= 18:
    print("Giriş yapabilirsiniz.")
else:
    print("Giriş yapamazsınız.")
```

Burada:

```python
age >= 18
```

`False` olduğu için `else` bloğu çalışır.

Temel yapı:

```python
if koşul:
    # koşul doğruysa
else:
    # koşul yanlışsa
```

---

## 5. `elif`

Birden fazla farklı durumu kontrol etmek için `elif` kullanılabilir.

```python
score = 75

if score >= 90:
    print("A")
elif score >= 70:
    print("B")
elif score >= 50:
    print("C")
else:
    print("F")
```

Python koşulları yukarıdan aşağıya kontrol eder.

İlk doğru koşul bulunduğunda ilgili blok çalışır ve diğer `elif` / `else` blokları değerlendirilmez.

---

## 6. Karşılaştırma Operatörleri ile Koşullar

Koşullarda karşılaştırma operatörleri sıklıkla kullanılır.

```python
age = 32

if age == 32:
    print("Yaş 32.")

if age != 20:
    print("Yaş 20 değil.")

if age > 18:
    print("Yaş 18'den büyük.")

if age >= 18:
    print("Yetişkin.")
```

Karşılaştırmalar `True` veya `False` ürettiği için `if` tarafından koşul olarak kullanılabilir.

---

## 7. Mantıksal Operatörler ile Koşullar

Birden fazla koşulu birleştirmek için `and`, `or` ve `not` kullanılabilir.

### `and`

Tüm koşulların doğru olması gerekir.

```python
age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("Giriş yapabilirsiniz.")
```

Burada iki koşul da `True` olmalıdır.

---

### `or`

Koşullardan en az birinin doğru olması yeterlidir.

```python
has_cash = False
has_card = True

if has_cash or has_card:
    print("Ödeme yapabilirsiniz.")
```

---

### `not`

Bir koşulun boolean sonucunu tersine çevirebilir.

```python
is_closed = False

if not is_closed:
    print("Açık.")
```

---

## 8. Kullanıcıdan Veri Alarak Koşul Kurmak

Koşullar kullanıcıdan alınan verilerle birlikte kullanılabilir.

```python
age = int(input("Yaşınızı giriniz: "))

if age >= 18:
    print("Giriş yapabilirsiniz.")
else:
    print("Giriş yapamazsınız.")
```

Program artık kullanıcının verdiği bilgiye göre farklı sonuçlar üretmektedir.

Bu, programların yalnızca sabit işlemler yapan kodlardan karar verebilen sistemlere dönüşmesinde önemli bir adımdır.

---

## 9. İç İçe Koşullar

Bir `if` bloğunun içerisinde başka bir `if` kullanılabilir.

```python
age = 25
has_ticket = True

if age >= 18:
    if has_ticket:
        print("Giriş yapabilirsiniz.")
    else:
        print("Biletiniz yok.")
else:
    print("Yaşınız yeterli değil.")
```

Burada ikinci koşul yalnızca ilk koşul doğru olduğunda kontrol edilir.

Ancak bazı durumlarda aynı mantık `and` kullanılarak daha kısa şekilde ifade edilebilir:

```python
if age >= 18 and has_ticket:
    print("Giriş yapabilirsiniz.")
```

Hangi yaklaşımın kullanılacağı problemin yapısına ve okunabilirliğe bağlıdır.

---

## 10. Koşulların Sırası Önemlidir

`if` ve `elif` kullanırken koşullar yukarıdan aşağıya değerlendirilir.

Örneğin:

```python
score = 95

if score >= 50:
    print("Geçti.")
elif score >= 90:
    print("A.")
```

Burada `score >= 50` zaten `True` olduğu için ikinci koşula ulaşılmaz.

Bu nedenle daha spesifik koşulların sıralaması önemlidir:

```python
score = 95

if score >= 90:
    print("A.")
elif score >= 50:
    print("Geçti.")
else:
    print("Kaldı.")
```

Bu yapı beklenen sonucu verir.

---

## 11. Koşullar ve `bool`

Koşulların temelinde `bool` değerleri bulunur.

Örneğin:

```python
age = 20

result = age >= 18

print(result)
print(type(result))
```

Sonuç:

```text
True
<class 'bool'>
```

Dolayısıyla:

```python
if age >= 18:
```

ifadesini kavramsal olarak:

```python
if True:
```

gibi düşünebiliriz.

Koşul yanlış olduğunda ise sonuç `False` olur.

---

## 12. Koşulların Program Akışındaki Rolü

Koşullar programın hangi kod yolunu izleyeceğini belirler.

Basit bir program:

```text
Veriyi al
    ↓
Koşulu kontrol et
    ↓
Doğru mu?
 ↙       ↘
Evet     Hayır
 ↓         ↓
İşlem A   İşlem B
```

Bu yapı ileride döngüler, fonksiyonlar, dosyalar ve sınıflarla birlikte daha karmaşık programların temelini oluşturacaktır.

---

## 13. Öğrenme Notu

Koşulları öğrenirken önemli olan yalnızca `if` yazabilmek değildir.

Asıl amaç:

> Bir problemin hangi durumlarda farklı davranması gerektiğini kod içerisinde ifade edebilmek.

Örneğin:

> Kullanıcı 18 yaşından büyükse giriş yapabilir.

kod olarak:

```python
if age >= 18:
    print("Giriş yapabilirsiniz.")
```

şeklinde ifade edilir.

Daha karmaşık bir durumda:

> Kullanıcı 18 yaşından büyük ve bileti varsa giriş yapabilir.

```python
if age >= 18 and has_ticket:
    print("Giriş yapabilirsiniz.")
```

şeklinde ifade edilebilir.

Bu düşünce biçimi, ileride program tasarlarken kullanılan temel karar verme mantığıdır.

---

## Özet

Python'da temel koşul yapıları:

| Yapı   | Görevi                                                 |
| ------ | ------------------------------------------------------ |
| `if`   | Koşul doğruysa çalışır                                 |
| `elif` | Önceki koşullar yanlışsa başka bir koşulu kontrol eder |
| `else` | Önceki koşulların hiçbiri doğru değilse çalışır        |
| `and`  | Tüm koşulların doğru olmasını ister                    |
| `or`   | En az bir koşulun doğru olmasını ister                 |
| `not`  | Boolean sonucu tersine çevirir                         |

Koşullar, programların verilen duruma göre karar verebilmesini sağlar.

