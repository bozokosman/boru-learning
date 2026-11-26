🇬🇧 [English](ROADMAP.md)

# Yol Haritası

> **Kısaca:** Tek plan bu dosya. Önce CS50P, tamamı ve sadece o. Bitince boru-learning'e yüklenme dönemi: Mini Library, CS50P'de öğrendiklerimle V4'ten V9'a büyür. Sonra SQL, backend, yapay zekâ ve iş başvurusu. Mini Library her aşamada büyüyen ana proje. İlk işten sonra "Old School" derinlik aşaması başlar. Yeni bir yol haritası görürsen bu dosyayı değiştirmeden önce bir hafta bekle ve mentorunla konuş.

**Hedef:** Junior backend geliştirici (Python + yapay zekâ entegrasyonu), 2028 başında işe hazır.
**Odak kuralı:** Her seferinde tek şey. Önce CS50P, tamamen. Geri kalan her şey bekler.
**Zaman bütçesi:** Tam zamanlı işin yanında haftada ~3-5 saat, genelde 60-120 dakikalık 2-4 oturum. 10 dakika da sayılır.
**Her aşamada büyüyen tek proje:** [Mini Library](02-projects/06-mini-library/), sözlük menüsünden (Temmuz 2026) yapay zekâ aramalı, canlıya alınmış bir API'ye kadar. Omurga bu, kafes değil: her aşamada küçük bir yan proje de olabilir.
**Neredeyim?** [NEXT.md](NEXT.md) her zaman tek sonraki adımı tutar.

## Aşama 1: İşe hazır

| # | Ne zaman (tahmin) | Öğren | Mini Library | Çıktı |
|---|---|---|---|---|
| 1 | şimdi → Mart 2027 | **CS50P** (Harvard), 3-9. haftalar + final projesi. Sadece CS50P. | bekler | CS50P sertifikası, final projesi reposu |
| 2 | Nisan → Mayıs 2027 | **Bu repoda Python sprinti**: her CS50P konusu kendi koduma uygulanır, notlar `01-python/04-09` içinde | V3 → V9 (aşağıya bak) | Mini Library V9, kendi cümlelerimle konu notları |
| 3 | Haziran → Temmuz 2027 | **SQL**: SQLite, sonra CS50 SQL dersleri | V10: SQLite depolama | Elle yazılmış sorgular, henüz ORM yok |
| 4 | Ağustos → Ekim 2027 | **Backend**: FastAPI, PostgreSQL, pytest, Docker, canlıya alma (deploy) | V11: REST API, kendi reposu, canlıda | Testleri ve README'si olan canlı bir API |
| 5 | Kasım → Aralık 2027 | **Yapay zekâ entegrasyonu**: LLM API'lerini doğrudan kullanma (yapılandırılmış çıktı, araç çağırma, embedding'ler) | V12: doğal dille arama / öneriler | Gerçekten çalışan küçük bir yapay zekâ özelliği |
| 6 | Ocak 2028 | **Portfolyo**: CV, LinkedIn, GitHub profili, mülakat pratiği, başvurular | - | Başvurular gönderildi |

Başvurular daha erken başlayabilir (2027 sonbaharından), o ana kadar canlıya alınmış olanla.

### CS50P sonrası Mini Library (2. aşama sprinti)

| Öğrendiğim CS50P haftası | Konu | Mini Library sürümü |
|---|---|---|
| 3 | İstisnalar (Exceptions) | V3: `search_book()` işlevini bitir. V4: hatalı girdiyi `try/except` ile ele al |
| 4 | Kütüphaneler | V5: bir kütüphane kullan (ör. `random` ile "günün kitabı" ya da `requests` ile herkese açık bir kitap API'si) |
| 5 | Birim testleri (Unit tests) | V6: ilk `pytest` testleri |
| 6 | Dosya G/Ç (File I/O) | V7: kitapları kaydet ve yükle (JSON ya da CSV) |
| 7 | Düzenli ifadeler (Regular expressions) | V8: ISBN ve e-posta doğrula |
| 8 | Nesne yönelimli programlama (OOP) | V9: `Librarian`, `Member`, `Loan` sınıfları |
| 9 | Et cetera | yeniden düzenle (refactor), temizle, V1 → V9 hikâyesini `PROJECT_EVOLUTION.md` içine yaz |

CS50P problem setleri ayrı bir özel repoda kalır (CS50'nin akademik dürüstlük kuralları). Burada yalnızca kendi projelerim ve notlarım var.

## Aşama 2: Old School (ilk işten sonra)

Derin temeller, acele yok, ömür boyu bir proje:
bilgisayar mimarisi, işletim sistemleri ve Linux, ağ, veri yapıları ve algoritmalar, sistem tasarımı, bir sistem dili (C ya da Rust), açık kaynak katkıları.
1. Aşama'daki notlarım (neyi yanlış anladım ve nasıl düzelttim) gelecekteki bir kitabın ham maddesi: *"sıfırdan yeniden başlayan biri tarafından yazılmış."*

## Kurallar

1. Kodu ben yazarım. Yapay zekâ öğretmen ve gözden geçirendir, yazar değil: ipucu ve soru verir, kod vermez. 15 dakikadır takıldın mı? Cevabı değil, ipucunu iste.
2. Her konu, izlediğim değil, yaptığım bir şeyle biter. Yeni bir konu, zaten bildiğim bir projeyi yeni araçla yeniden yazmak demektir (Calculator v1-v4 böyle oldu).
3. Bir gün kaçırmak sorun değil; üst üste iki gün kaçırmamaya çalış. Uzun bir aradan sonra küçük başla: son kodu çalıştır, `NEXT.md`'yi oku, suçluluk yok.
4. Klasör iskeleti önceden hazır, böylece zamanım yapıya değil öğrenmeye gider.
5. Eski sürümler asla silinmez: v1, v2, v3... nasıl öğrendiğimi gösterir.
6. Her sürüme kendi cümlelerimle kısa bir `NOTES.md` girdisi yazılır: neyi yanlış yaptım, nasıl düzelttim.
7. Tek yol haritası bu. Yeni bir yol haritası ya da video, burada bir şeyi değiştirebilmek için bir hafta bekler.
8. İş, uyku ve aile önce gelir. Bunları bozan plan kötü plandır.
9. Her oturum `NEXT.md` içinde tek bir satırla biter.
10. Yeni araçlar ve kurulumlar bir saatlik kutu alır. Hiçbir zaman bir öğrenme gününü yemez; bir saatte çalışmazsa bırak.
11. API anahtarları ve parolalar asla bir sohbete yapıştırılmaz. Sızan anahtar hemen iptal edilir.

## Kontrol Noktaları

- **31 Aralık 2026:** CS50P 5. hafta başladı mı?
- **31 Mart 2027:** CS50P sertifikası (CS50'nin kesin son tarihi: 30 Haziran 2027).
- **31 Mayıs 2027:** Mini Library V9.
- **31 Ekim 2027:** Mini Library V11 canlıda.
- **31 Ocak 2028:** Başvurular çıktı.
