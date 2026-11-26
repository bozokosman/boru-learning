# Session 6 - JSON & File I/O (Day 6)

## Topics Learned (Bugün Öğrenilenler)
- **`json` modülü:** Python sözlüklerini (dict) ve listeleri JSON formatına çevirip dosyaya kaydetmeyi sağlar.
- **`json.dump(data, file)`:** Bir Python nesnesini (dict, list) dosyaya JSON olarak yazar.
- **`json.load(file)`:** Bir JSON dosyasını okuyup Python nesnesine (dict, list) çevirir.
- **`with open(...) as f:`** : Dosyayı otomatik olarak açıp kapatan, güvenli dosya işleme yapısı.
- **Dosya Modları:**
  - `"r"` → Okuma (dosya yoksa hata verir).
  - `"w"` → Yazma (dosya yoksa oluşturur, varsa üzerine yazar).
  - `"a"` → Ekleme (dosya sonuna ekler).
- **`encoding="utf-8"`** : Türkçe karakterlerin (ş, ğ, ü, ö, ç, ı) düzgün yazılmasını sağlar.
- **`indent=4`** : JSON dosyasını okunaklı (girintili) hale getirir.
- **`ensure_ascii=False`** : Türkçe karakterlerin `\u0130` gibi kodlara dönüşmesini engeller.
- **`os.path.exists("data.json")`** : Bir dosyanın var olup olmadığını kontrol eder.
- **`global` anahtar kelimesi:** Bir fonksiyon içinden global değişkenleri değiştirmek için kullanılır.

## Applied In (Uygulandığı Proje)
- **Currency Tracker v2** (`projects/04-currency-tracker/v2_currency.py`)
- `load_data()` → `data.json` dosyasını okur, yoksa oluşturur ve varsayılan veriyi döndürür.
- `save_data()` → `rates`, `portfolio`, `history` verilerini `data.json` dosyasına yazar.
- `main()` → Başlangıçta `load_data()` çağırır, çıkışta `save_data()` çağırır.

## Key Insights (Önemli Çıkarımlar)
- `json.dump()` fonksiyonu iki zorunlu parametre alır: (1) yazılacak veri, (2) dosya nesnesi.
- `with open()` bloğu bittiğinde dosya otomatik kapanır, `close()` çağırmaya gerek yok.
- `load_data()` fonksiyonu tutarlı bir dönüş tipi kullanmalı (hep tuple veya hep dict).
- JSON'da tuple diye bir kavram yoktur; tuple'lar otomatik olarak listeye çevrilir.
- `global` anahtar kelimesi olmadan, `main()` içinde `rates = ...` yazmak yerel bir değişken oluşturur ve global'i gölgeler.

## Next (Sırada)
- try-except ile hata yönetimi
- datetime ile tarih/saat işlemleri
- API'den canlı kur çekme (Currency Tracker v3)
