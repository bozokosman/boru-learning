# Session 3 - Loops and Calculator v2 (Day 3)

## Topics Learned
- `while True` ile sonsuz döngü oluşturma
- Kullanıcı `0` tuşlayana kadar programı çalıştırma
- Menü akışını optimize etme (çıkışta sayı sormama)

## Code
- [v2_calc.py](../projects/01-calculator/v2_calc.py)

## Key Insights
- Döngü içinde `break` ile çıkış kontrolü yapmak çok önemli.
- Kullanıcıdan sayıları, işlemi seçtikten SONRA almak daha iyi UX sağlıyor.

## Uygulama: Sayı Tahmin Oyunu (Guessing Game)
- `projects/02-guessing-game/v1_guess.py` dosyası oluşturuldu.
- `while move > 0:` döngüsü ile 5 hak üzerinden çalışan bir tahmin oyunu yazıldı.
- Kullanıcı doğru tahmin ederse `break` ile çıkıyor, hakkı biterse `while-else` bloğu ile kayıp mesajı gösteriliyor.
- `random.randint()` ile hedef sayı üretildi.
