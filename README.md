# Book Separable Reading Project

Bu repo, bir üniversite dersi kapsamında Python ile geliştirilmiş basit bir metin işleme/analiz çalışmasıdır. Amaç, bir veya iki kitap metni (
`book_1.txt`, `book_2.txt`) üzerinde **kelime** veya **ikili kelime (bigram)** sıklıklarını hesaplayıp sonuçları dosyaya yazmaktır.

## Özellikler

- Metni küçük harfe çevirir ve kelimelere böler
- Noktalama/özel karakterleri temizler
- Stop-word (durdurma kelimeleri) listesini çıkarır
- `Word_Order` parametresine göre analiz yapar:
  - `1`: tekil kelime frekansı
  - `2`: ardışık iki kelimeden oluşan bigram frekansı
- Sonuçları frekansa göre azalan şekilde sıralar
- Tek kitap için ilk 200 sonucu çıktı dosyasına yazar
- İki kitap için ortak kelime/bigram’ların toplam frekansını ve her kitapta ayrı ayrı frekansını raporlar

## Kullanım

Ana script: `1. python ödevimin belgeleri/temp.py`

Script içerisinde dosya adları ve çıktı dosyaları şu değişkenlerle ayarlanır:

- `Book`, `Book_1`, `Book_2`
- `Word_Order`
- `File_Output`, `File_Output2`

Çalıştırmak için (örnek):

```
bash
python "1. python ödevimin belgeleri/temp.py"
```

> Not: Script, kitap metin dosyalarının aynı dizinde/çalışma dizininde bulunmasını bekler.

## Çıktılar

- Tek kitap analizi: `python homework output of first function.txt`
- İki kitap karşılaştırması: `python homework output of second function.txt` (fonksiyon çağrısı açılırsa)

## Fonksiyonlar

- `Word_Order_Frequency_One_Book(Book, Word_Order, File_Output)`
- `Word_Order_Frequency_Two_Books(Book_1, Book_2, Word_Order, File_Output2)`
