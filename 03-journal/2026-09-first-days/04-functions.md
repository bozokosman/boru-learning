# Session 4 - Functions (Day 4)

## Topics Learned (Bugün Öğrenilenler)
- **Fonksiyon Tanımlama:** `def` anahtar kelimesi ile kod bloklarını adlandırma.
- **Parametreler:** Fonksiyonlara veri göndermek için kullanılan yapılar (örn: `def topla(a, b):`).
- **Return (Geri Döndürme):** Fonksiyonun sonucunu dışarıya vermek için `return` kullanımı. (Ekrana yazdırmak `print()` ile yapılır, `return` ile değer döndürülür).
- **`if __name__ == "__main__":`** : Kodun sadece doğrudan çalıştırıldığında (python dosya.py) başlamasını, başka dosyadan import edildiğinde ise sadece fonksiyonların içe aktarılmasını sağlayan standart Python kalıbı.

## Updated Projects (Güncellenen Projeler)

### 1. Calculator (v3)
- `projects/01-calculator/v3_calc.py`
- Tüm işlemler (`addition`, `subtraction`, `multiplication`, `division`) ayrı fonksiyonlara alındı.
- Menü ve sayı alma işlemleri (`show_menu`, `get_number`) fonksiyonlara bölündü.
- `main()` fonksiyonu ile yönetildi.
- `if __name__ == "__main__":` yapısı eklendi.

### 2. Guessing Game (v2)
- `projects/02-guessing-game/v2_guess.py`
- `get_guess()`, `check_guess()`, `play()` ve `main()` fonksiyonları oluşturuldu.
- `check_guess()` artık ekrana yazdırmak yerine `return` ile sonuç döndürüyor.
- `if __name__ == "__main__":` eklendi.

### 3. Login System (v2)
- `projects/03-login-system/v2_login.py`
- `check_credentials(username, password)`, `get_credentials(prompt)`, `login()` ve `main()` fonksiyonları oluşturuldu.
- `check_credentials()` sonucu `return` ile döndürüyor (`both_wrong`, `wrong_username`, `wrong_password`, `correct`).
- `login()` içinde her turda `username` ve `password` değişkenlere atanıp `check_credentials`'a gönderiliyor.
- `if __name__ == "__main__":` eklendi.

## Key Insights (Önemli Çıkarımlar)
- `return` kullanmak, fonksiyonun çıktısını başka yerlerde tekrar kullanmayı mümkün kılar.
- `if __name__ == "__main__":` kullanmak, kodu modüler ve profesyonel hale getirir.
- Kodu fonksiyonlara bölmek okunurluğu artırır ve hata ayıklamayı kolaylaştırır.
- String karşılaştırmalarında alt çizgi (`_`) ve boşluk (` `) farkına dikkat etmek gerekir.
