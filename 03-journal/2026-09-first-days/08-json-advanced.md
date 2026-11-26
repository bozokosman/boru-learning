# Session 8 - JSON Advanced & Multiple Projects (Day 8-9)

## Topics Learned (Bugün Öğrenilenler)
- **JSON ile veri kalıcılığı:** Farklı projelerde (Guessing Game, Currency Tracker, Calculator, Login System) JSON kullanımı.
- **Ortak fonksiyon yapısı:** `load_data()`, `save_data(data)`.
- **`datetime` ile kayıt tarihi:** Her işleme otomatik tarih ekleme (`datetime.now().strftime(...)`).
- **Menüye yeni seçenek ekleme:** `'h'` ile geçmiş görüntüleme.
- **Kod tekrarını azaltma:** İşlem sembolünü (`progress`) doğrudan `add_history`'ye gönderme.
- **JSON ile çoklu kullanıcı yönetimi:** `data_login.json` içinde `{"users": {"username": "password"}}` yapısı.
- **Register ve Login ayrımı:** Menüde ayrı seçenekler, her biri kendi fonksiyonunda.
- **`return` ile sonuç döndürme:** `login` fonksiyonu `"success"`, `"not_found"`, `"blocked"` döndürüyor; `main()` bunları yorumluyor.
- **`print` vs `return`:** Döngü içinde anlık geri bildirim için `print`, nihai sonuç için `return`.
- **`get_username` ve `get_password` ayrımı:** Kullanıcı adı `.lower()` ile normalize edilirken, şifre büyük/küçük harf duyarlı kalıyor.

## Applied In (Uygulandığı Projeler)

### 1. Calculator v4 (`projects/01-calculator/v4_calc.py`)
- `load_data()` → `data_calc.json` okur, yoksa `{"history": []}` oluşturur.
- `save_data(data)` → geçmişi dosyaya yazar.
- `add_history(data, num1, num2, operation, result)` → tarihli kayıt ekler.
- `show_history(data)` → geçmişi okunaklı listeler.
- `show_menu()` → `'h'` seçeneği eklendi.
- İşlem fonksiyonları sayı döndürecek şekilde güncellendi.

### 2. Login System v3 (`projects/03-login-system/v3_login.py`)
- `load_data()` → `data_login.json` okur, yoksa `{"users": {}}` oluşturur.
- `save_data(data)` → kullanıcıları dosyaya yazar.
- `register(data, username, password)` → kullanıcı ekler, `"created"` veya `"exists"` döndürür.
- `login(data)` → 3 hak, `"success"`, `"not_found"`, `"blocked"` döndürür.
- `main()` → menülü döngü (Login, Register, Exit).

## Key Insights (Önemli Çıkarımlar)
- `data = load_data()` döngünün **dışında** olmalı, yoksa her turda veri sıfırlanır.
- `if __name__ == "__main__": main()` yapısından sonra fazladan `main()` çağırmak, programın iki kez başlamasına neden olur.
- JSON'da `result` alanına sayısal değer kaydetmek, ileride hesaplama yapmak için önemlidir (string değil).
- Aynı JSON yapısını farklı projelerde kullanmak, konuyu pekiştirir.
- `print` ve `return` farklı amaçlar için kullanılır: `print` anlık mesaj, `return` fonksiyon sonucu.
- Şifreler düz metin olarak saklanıyor (güvenlik riski, ileride hash'leme öğrenilecek).

## Next (Sırada)
- try-except (Hata Yönetimi)
- API'lerle çalışma (`requests`)
