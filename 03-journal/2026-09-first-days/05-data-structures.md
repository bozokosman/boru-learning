# Session 5 - Data Structures (Day 5)

## Topics Learned (Bugün Öğrenilenler)
- **Dict (Sözlük):** Anahtar-değer çiftleri. Hızlı erişim, güncelleme, ekleme.
  - `rates = {"USD": 48.50, "EUR": 56.57}`
  - `rates["USD"]` ile değere erişim
  - `rates.items()` ile anahtar-değer çiftlerini döngüleme
  - `if key in dict` ile varlık kontrolü
- **Set (Küme):** Benzersiz elemanlar. Tekrarsız veri.
  - `symbols = set(rates.keys())`
  - `if symbol in symbols` ile hızlı kontrol
- **Tuple (Demet):** Değiştirilemez sıralı veri.
  - `(source, target, amount, goal)` gibi birden fazla değeri tek pakette döndürme.
- **List (Liste):** Sıralı, değiştirilebilir veri.
  - `history = []` ile geçmiş tutma
  - `history.append(record)` ile ekleme

## Applied In (Uygulandığı Proje)
- **Currency Tracker v1** (`projects/04-currency-tracker/v1_currency.py`)
- `rates` dict → kurları saklama
- `portfolio` dict → kullanıcının varlıklarını saklama
- `history` list → çevrim geçmişi
- `symbols` set → geçerli birimler (kullanılmadı ama öğrenildi)
- `convert` tuple döndürüyor

## Key Insights (Önemli Çıkarımlar)
- `return None` ile hata durumunu ayırt etmek, string karşılaştırmadan daha sağlam.
- `for key in dict:` ile `for key, value in dict.items():` arasındaki fark.
- Dict'te bir değeri güncellerken anahtarı kullanmak (değeri değil).
- `.upper()` ile kullanıcı girişini normalize etmek.

## Next (Sırada)
- JSON ile verileri dosyaya kaydetme (v2)
- API'den canlı kur çekme (v3)
- try-except ile hata yönetimi (v4)
