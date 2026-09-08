# Session 4 - Functions (Day 4)

## Topics Learned (Bugün Öğrenilenler)
- **Fonksiyon Tanımlama:** `def` anahtar kelimesi ile kod bloklarını adlandırma.
- **Parametreler:** Fonksiyonlara veri göndermek için kullanılan yapılar (örn: `def topla(a, b):`).
- **Return (Geri Döndürme):** Fonksiyonun sonucunu dışarıya vermek için `return` kullanımı. (Ekrana yazdırmak `print()` ile yapılır, `return` ile değer döndürülür).
- **`if __name__ == "__main__":`** : Kodun sadece doğrudan çalıştırıldığında (python dosya.py) başlamasını, başka dosyadan import edildiğinde ise sadece fonksiyonların içe aktarılmasını sağlayan standart Python kalıbı.

## Updated Projects (Güncellenen Projeler)
1. **Calculator (v3)**
   - `projects/01-calculator/v3_calc.py`
   - Tüm işlemler (`topla`, `çıkar`, `çarp`, `böl`) ayrı fonksiyonlara alındı.
   - Menü ve sayı alma işlemleri fonksiyonlara bölündü.
   - `main()` fonksiyonu ile yönetildi.

2. **Guessing Game (v2)**
   - `projects/02-guessing-game/v2_guess.py`
   - `get_guess()`, `check_guess()`, `play()` ve `main()` fonksiyonları oluşturuldu.
   - `check_guess()` artık ekrana yazdırmak yerine `return` ile sonuç döndürüyor.

## Key Insights (Önemli Çıkarımlar)
- `return` kullanmak, fonksiyonun çıktısını başka yerlerde tekrar kullanmayı mümkün kılar.
- `if __name__ == "__main__":` kullanmak, kodu modüler ve profesyonel hale getirir.
- Kodu fonksiyonlara bölmek okunurluğu artırır ve hata ayıklamayı kolaylaştırır.