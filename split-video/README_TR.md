# split-video

## Açıklama
Bu script, FFmpeg kullanarak bir video dosyasını belirtilen sayıda eşit süreli parçalara böler. Her parçanın süresini otomatik olarak hesaplar ve kalan saniyeleri son parçaya ekleyerek işler.

## Gereksinimler
- Bash
- FFmpeg (`ffprobe` ve `ffmpeg` komutları)
- Giriş video dosyası

## Kullanım
```bash
bash split_video.sh <video_dosyası> <parça_sayısı>
```

### Parametreler
- `video_dosyası`: Giriş video dosyasının yolu
- `parça_sayısı`: Videonun bölüneceği parça sayısı

### Örnek
```bash
bash split_video.sh film.mp4 3
bash split_video.sh /yol/video.avi 5
```

## Ne Yapar
1. **Süre Tespiti**: Videonun toplam süresini almak için `ffprobe` kullanır
2. **Parça Hesaplama**: Her parça için süreyi hesaplar (toplam_süre / parça_sayısı)
3. **Kalan İşleme**: Kalan saniyeleri son parçaya ekler
4. **Video Bölme**: Kesin zamanlama ile her parçayı oluşturmak için `ffmpeg` kullanır
5. **Dosya Adlandırma**: Sıralı numaralama ile çıktı dosyaları oluşturur

## Çıktı Dosyaları
`film.mp4` adlı bir video 3 parçaya bölündüğünde:
```
film_part1.mp4
film_part2.mp4
film_part3.mp4
```

## Örnek Çıktı
```bash
$ bash split_video.sh film.mp4 3
Total duration: 150 seconds
Duration per part: 50 seconds
Remainder: 0 seconds
Creating part 1: 0 to 50 seconds
Creating part 2: 50 to 100 seconds
Creating part 3: 100 to 150 seconds
Video splitting completed!
```

## Özellikler
- **Otomatik Süre Hesaplama**: Zamanlamaları manuel olarak hesaplama gereği yok
- **Kesin Bölme**: Temiz kesimler için tam zaman damgaları kullanır
- **Kalan İşleme**: Ekstra saniyeleri son parçaya ekleyerek içerik kaybını önler
- **İlerleme Geri Bildirimi**: Her parçanın oluşturulmasını gösterir
- **Esnek Giriş**: FFmpeg tarafından desteklenen çeşitli video formatlarıyla çalışır
- **Sıralı Adlandırma**: Açıkça numaralandırılmış çıktı dosyaları oluşturur

## Kullanım Alanları
- **Dosya Boyutu Yönetimi**: Büyük videoları daha küçük, yönetilebilir parçalara bölme
- **Yükleme Hazırlığı**: Platform boyut sınırlarına uygun parçalar oluşturma
- **İçerik Dağıtımı**: Daha kolay paylaşım için içeriği bölme
- **Depolama Optimizasyonu**: Videoyu birden fazla depolama konumuna dağıtma
- **Akış Hazırlığı**: Akış uygulamaları için segmentler oluşturma
- **Yedekleme Stratejisi**: Birden fazla yedek parçası oluşturma

## Teknik Detaylar
- Video meta verilerini çıkarmak için `ffprobe` kullanır
- Hızlı, kayıpsız bölme için `-c copy` ile `ffmpeg` kullanır
- Tamsayı bölme kalanlarını otomatik olarak işler
- Orijinal video kalitesini ve formatını korur
- Kesin zaman damgası formatlaması kullanır (SS:DD:SS)

## Hata İşleme
Script temel doğrulama içerir:
- Doğru argüman sayısını kontrol eder
- Video dosyasının varlığını doğrular
- FFmpeg kurulumunu doğrular