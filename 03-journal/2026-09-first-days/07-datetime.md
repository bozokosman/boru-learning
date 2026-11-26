# Session 7 - Datetime & JSON Advanced (Day 7)

## Topics Learned (Bugün Öğrenilenler)
- **`datetime` modülü:** Tarih ve saat işlemleri için kullanılır.
  - `from datetime import datetime`
  - `datetime.now()` → Şu anki tarih ve saati verir.
  - `strftime("%Y-%m-%d %H:%M:%S")` → Tarihi istediğin formatta string'e çevirir.
- **Kronometre Mantığı:**
  - Oyun başında: `start = datetime.now()`
  - Oyun sonunda: `end = datetime.now()`
  - Süre: `(end - start).total_seconds()` → saniye cinsinden float.
- **`sorted()` Fonksiyonu:**
  - `sorted(liste, key=fonksiyon)` ile özel sıralama.
  - `key` fonksiyonu bir tuple döndürürse, önce ilk elemana, sonra ikinciye göre sıralar.
  - `[:5]` dilimi ile ilk 5 elemanı alma.
- **`enumerate()` Fonksiyonu:**
  - `for i, item in enumerate(liste, 1):` → Sıra numarası ile döngü.

## Applied In (Uygulandığı Proje)
- **Guessing Game v3** (`projects/02-guessing-game/v3_guess.py`)
- `play()` → Oyuncu adı, kronometre, skor sözlüğü döndürme.
- `add_score()` → History ve high_scores güncelleme, sıralama, ilk 5'i tutma.
- `show_high_scores()` → En iyi 5 skoru listeleme.
- `show_history()` → Tüm oyun geçmişini listeleme.
- `main()` → Menülü döngü, her oyun sonunda `save_data()`.

## Key Insights (Önemli Çıkarımlar)
- `sorted()` yeni bir liste döndürür, orijinal listeyi değiştirmez.
- `datetime.now()` iki kez çağrılıp çıkarıldığında `timedelta` nesnesi verir.
- `.total_seconds()` ile süreyi saniyeye çevirebilirsin.
- JSON'da tuple olmaz, listeye dönüşür. Ama indeksleme aynı şekilde çalışır.
- Her oyun sonunda kaydetmek, veri kaybını önler.

## Next (Sırada)
- Calculator v4 (JSON ile hesap geçmişi)
- Login System v3 (JSON ile çoklu kullanıcı)
- try-except ile hata yönetimi
