# remove-console-logs

## Açıklama
Bu script, JavaScript/TypeScript dosyalarından console loglama ifadelerini kaldırır. Tek satırlı ve çok satırlı console ifadelerini (`console.log`, `console.error`, `console.warn`, ve `console.info`) akıllıca işlerken kod yapısını ve formatını korur.

## Gereksinimler
- Python 3.x
- re modülü (yerleşik)
- Hedef JavaScript/TypeScript dosyaları
- Dosyalar için yazma izinleri

## Kullanım
```bash
python remove_console_logs.py
```

## Yapılandırma
Script içerisinde dosya yolunu değiştirin:
```python
file_path = 'path/to/your/file.js'  # Bunu hedef dosyanıza değiştirin
```

## Ne yapar
1. **Dosya Okuma**: Belirtilen dosyanın tüm içeriğini okur
2. **Kalıp Tespiti**: Regex kalıpları kullanarak console loglama ifadelerini tanımlar
3. **Çok Satır İşleme**: Birden fazla satıra yayılan console ifadelerini düzgün işler
4. **Parantez Sayma**: İfade sınırlarını belirlemek için parantez sayma kullanır
5. **Noktalı Virgül Temizliği**: Console ifadeleriyle ilişkili noktalı virgülleri kaldırır
6. **Dosya Yazma**: Temizlenmiş içeriği dosyaya geri yazar

## Desteklenen Console Metodları
Script şu console metodlarını kaldırır:
- `console.log()`
- `console.error()`
- `console.warn()`
- `console.info()`

## Örnekler

### Önce
```javascript
function calculateTotal(items) {
  console.log('Hesaplama başlıyor');
  let total = 0;
  
  for (let item of items) {
    console.log('Öğe işleniyor:', item);
    total += item.price;
  }
  
  console.error('Debug bilgisi:', {
    itemCount: items.length,
    total: total
  });
  
  console.warn('Hesaplama tamamlandı');
  return total;
}
```

### Sonra
```javascript
function calculateTotal(items) {
  let total = 0;
  
  for (let item of items) {
    total += item.price;
  }
  
  return total;
}
```

## Çok Satırlı Console İşleme
Script karmaşık çok satırlı console ifadelerini düzgün işler:

### Önce
```javascript
console.log(
  'Karmaşık nesne:',
  {
    user: userData,
    timestamp: new Date(),
    nested: {
      value: someValue
    }
  }
);
```

### Sonra
```javascript
// Tamamen kaldırıldı
```

## Özellikler
- **Akıllı Ayrıştırma**: Doğru ifade tespiti için parantez sayma kullanır
- **Çok Satır Desteği**: Birden fazla satıra yayılan console ifadelerini işler
- **Noktalı Virgül Temizliği**: Sözdizimi hatalarını önlemek için ilişkili noktalı virgülleri kaldırır
- **Format Koruma**: Orijinal kod girintisini ve yapısını korur
- **Güvenli Kaldırma**: Sadece tam console ifadelerini kaldırır, kısmi eşleşmeleri değil
- **Çoklu Metodlar**: Tüm yaygın console loglama metodlarını destekler
- **Regex Tabanlı**: Kalıp eşleştirme için verimli düzenli ifadeler kullanır

## Algoritma Detayları
1. **İlk Tespit**: Console metod çağrılarını bulmak için regex kullanır
2. **Sınır Tespiti**: Açılış ve kapanış parantezlerini sayar
3. **Çok Satır Takibi**: Parantezler dengelenene kadar ayrıştırmaya devam eder
4. **İçerik Çıkarma**: Tam console ifadesini çıkarır
5. **Noktalı Virgül İşleme**: Noktalı virgülleri kontrol eder ve kaldırır
6. **Değiştirme**: Tüm ifadeyi boş string ile değiştirir

## Kullanım Alanları
- **Üretim Temizliği**: Üretim dağıtımından önce debug ifadelerini kaldırma
- **Kod Optimizasyonu**: Daha iyi performans için geliştirme kodunu temizleme
- **Güvenlik**: Console loglarından potansiyel hassas bilgileri kaldırma
- **Kod İncelemesi**: Debug ifadelerini kaldırarak kodu incelemeye hazırlama
- **Build Süreci**: Otomatik temizlik için build pipeline'larına entegrasyon
- **Eski Kod**: Aşırı loglama içeren eski kod tabanlarını temizleme
- **Performans**: Gereksiz console çağrılarını kaldırarak bundle boyutunu azaltma

## Desteklenen Dosya Türleri
- JavaScript dosyaları (`.js`)
- TypeScript dosyaları (`.ts`)
- Vue.js dosyaları (`.vue`) - JavaScript bölümleri
- React JSX dosyaları (`.jsx`)
- JavaScript console ifadeleri içeren herhangi bir metin dosyası

## Güvenlik Özellikleri
- **Yedek Önerisi**: Çalıştırmadan önce her zaman dosyaları yedekleyin veya git kullanıyorsanız `git diff` komutunu kullanarak değişiklikleri kontrol edin
- **Tam İfade Kaldırma**: Sadece tam, geçerli console ifadelerini kaldırır
- **Sözdizimi Koruma**: Kaldırma sonrası geçerli JavaScript sözdizimini korur
- **Mantığa Zarar Vermeme**: Sadece loglama kaldırır, iş mantığını korur

## Sınırlamalar
- **String Literalleri**: String literalleri içindeki console ifadelerini kaldırmaz
- **Dinamik Çağrılar**: Dinamik olarak oluşturulan console çağrılarını işleyemeyebilir
- **Minified Kod**: Minified/obfuscated kod için tasarlanmamıştır

## Özelleştirme
- **Dosya Yolu**: Hedef dosya yolunu değiştirme
- **Console Metodları**: Hedeflenecek console metodlarını ekleme veya kaldırma
- **Kalıp Eşleştirme**: Özel gereksinimler için regex kalıplarını değiştirme
- **Çıktı İşleme**: Loglama veya ilerleme raporlama ekleme
- **Toplu İşleme**: Birden fazla dosyayı işlemek için genişletme
- **Yedek Oluşturma**: Otomatik yedek işlevselliği ekleme

## Entegrasyon
Bu script şunlara entegre edilebilir:
- **Build Sistemleri**: Webpack, Rollup, Vite eklentileri
- **CI/CD Pipeline'ları**: Otomatik kod temizliği
- **Git Hook'ları**: Otomatik temizlik için pre-commit hook'ları
- **IDE Uzantıları**: Özel editör uzantıları
- **Linting Araçları**: ESLint özel kuralları