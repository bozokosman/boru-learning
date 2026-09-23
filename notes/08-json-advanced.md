# Session 8 - JSON Advanced & Calculator v4 (Day 8)

## Topics Learned (Bugün Öğrenilenler)
- **JSON ile veri kalıcılığı:** Farklı projelerde (Guessing Game, Currency Tracker, Calculator) JSON kullanımı.
- **Ortak fonksiyon yapısı:** `load_data()`, `save_data(data)`, `add_history(data, ...)`, `show_history(data)`.
- **`datetime` ile kayıt tarihi:** Her işleme otomatik tarih ekleme (`datetime.now().strftime(...)`).
- **Menüye yeni seçenek ekleme:** `'h'` ile geçmiş görüntüleme.
- **Kod tekrarını azaltma:** İşlem sembolünü (`progress`) doğrudan `add_history`'ye gönderme.

## Applied In (Uygulandığı Proje)
- **Calculator v4** (`projects/01-calculator/v4_calc.py`)
- `load_data()` → `data_calc.json`'u okur, yoksa `{"history": []}` oluşturur.
- `save_data(data)` → Geçmişi dosyaya yazar.
- `add_history(data, num1, num2, operation, result)` → Tarihli kayıt ekler.
- `show_history(data)` → Geçmişi okunaklı listeler.
- `main()` → Menülü döngü, her işlemden sonra `add_history`, çıkışta `save_data`.

## Key Insights (Önemli Çıkarımlar)
- `data = load_data()` döngünün **dışında** olmalı, yoksa her turda veri sıfırlanır.
- `if __name__ == "__main__": main()` yapısından sonra fazladan `main()` çağırmak, programın iki kez başlamasına neden olur.
- JSON'da `result` alanına sayısal değer kaydetmek, ileride hesaplama yapmak için önemlidir (string değil).
- Aynı JSON yapısını farklı projelerde kullanmak, konuyu pekiştirir.

## Next (Sırada)
- Login System v3 (JSON ile çoklu kullanıcı)
- try-except (Hata Yönetimi)
