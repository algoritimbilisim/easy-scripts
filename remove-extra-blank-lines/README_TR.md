# remove-extra-blank-lines

## Açıklama
Bu script, TypeScript, TSX ve Vue.js dosyalarından aşırı ardışık boş satırları kaldırır ve birden fazla boş satırı tek boş satırla değiştirir. Projenizde temiz ve tutarlı kod formatı korunmasına yardımcı olur.

## Gereksinimler
- Python 3.x
- os ve re modülleri (yerleşik)
- Hedef dosyaları içeren kaynak dizin
- Dosyalar için yazma izinleri

## Kullanım
```bash
python remove_extra_blank_lines.py
```

## Yapılandırma
Script içerisinde kaynak dizini değiştirin:
```python
src_dir = 'src'  # Bunu kaynak dizininize değiştirin
```

## Ne yapar
1. **Dizin Gezinme**: Belirtilen kaynak dizini özyinelemeli olarak gezer
2. **Dosya Filtreleme**: Sadece `.ts`, `.tsx` ve `.vue` dosyalarını işler
3. **İçerik Analizi**: Dosya içeriğini okur ve ardışık boş satırları tanımlar
4. **Kalıp Değiştirme**: 3+ ardışık yeni satırı 2 yeni satırla değiştirmek için regex kullanır
5. **Dosya Güncelleme**: Değişiklik yapıldıysa temizlenmiş içeriği dosyaya geri yazar
6. **İlerleme Raporlama**: Hangi dosyaların değiştirildiğini ve toplam sayıyı gösterir

## Desteklenen Dosya Türleri
- **TypeScript**: `.ts` dosyaları
- **TypeScript React**: `.tsx` dosyaları
- **Vue.js**: `.vue` dosyaları

## Örnekler

### Önce
```typescript
function calculateTotal(items: Item[]) {
  let total = 0;



  for (const item of items) {
    total += item.price;




    console.log(`Added ${item.name}`);
  }


  return total;
}
```

### Sonra
```typescript
function calculateTotal(items: Item[]) {
  let total = 0;

  for (const item of items) {
    total += item.price;

    console.log(`Added ${item.name}`);
  }

  return total;
}
```

## Özellikler
- **Seçici İşleme**: Sadece belirli dosya türlerini işler
- **Yıkıcı Olmayan**: Tek boş satırları ve içerik yapısını korur
- **Verimli**: Sadece gerçekten değişiklik gereken dosyalara yazar
- **İlerleme Takibi**: Gerçek zamanlı işleme durumunu gösterir
- **Hata İşleme**: Dosya erişim hatalarını zarif şekilde işler
- **Kodlama Desteği**: UTF-8 kodlu dosyaları düzgün işler
- **Özyinelemeli İşleme**: İç içe dizin yapılarını işler

## Algoritma Detayları
1. **Kalıp Eşleştirme**: 3 veya daha fazla ardışık yeni satır bulmak için `r'\n{3,}'` regex'i kullanır
2. **Değiştirme**: Eşleşmeleri tam olarak 2 yeni satırla (`\n\n`) değiştirir
3. **Değişiklik Tespiti**: Orijinal ve değiştirilmiş içeriği karşılaştırır
4. **Koşullu Yazma**: Sadece içerik gerçekten değiştiyse dosyaya yazar

## Çıktı
Script ayrıntılı geri bildirim sağlar:
```
Modified: src/components/UserPanel.vue
Modified: src/services/ApiService.ts
Modified: src/types/User.tsx
Completed! Modified 3 files.
```

## Kullanım Alanları
- **Kod Temizliği**: Eski koddan aşırı boşlukları kaldırma
- **Pre-commit Hook'ları**: Commit'lerden önce tutarlı formatı sağlama
- **Kod İnceleme Hazırlığı**: İnceleme gönderimlerinden önce kodu temizleme
- **Proje Taşıma**: Projeleri taşırken formatı standartlaştırma
- **Takım Standartları**: Takım genelinde tutarlı boş satır kullanımını zorlama
- **Build Süreci**: Otomatik temizlik için build pipeline'larına entegrasyon
- **IDE Entegrasyonu**: Geliştirme ortamlarında harici araç olarak kullanma

## Proje Yapısı
```
project/
├── src/
│   ├── components/
│   │   ├── UserPanel.vue
│   │   └── ProductList.tsx
│   ├── services/
│   │   └── ApiService.ts
│   └── types/
│       └── User.ts
└── remove_extra_blank_lines.py
```

## Güvenlik Özellikleri
- **Yedek Önerisi**: Çalıştırmadan önce her zaman dosyaları yedekleyin veya git kullanıyorsanız `git diff` komutunu kullanarak değişiklikleri kontrol edin
- **Hata İşleme**: Bireysel dosyalar başarısız olsa bile işlemeye devam eder
- **İçerik Koruma**: Sadece aşırı boş satırları kaldırır, diğer tüm içeriği korur
- **Kodlama Güvenliği**: UTF-8 kodlamasını düzgün işler
- **Değişiklik Doğrulama**: Sadece gerçekten değişiklik gereken dosyaları değiştirir

## Özelleştirme
- **Kaynak Dizin**: Farklı dizinleri hedeflemek için `src_dir`'i değiştirme
- **Dosya Uzantıları**: Koşuldaki dosya uzantısı filtresini değiştirme
- **Boş Satır Politikası**: Farklı boş satır kuralları için regex kalıbını ayarlama
- **Çıktı Ayrıntısı**: İlerleme mesajlarını ekleme veya kaldırma
- **Toplu İşleme**: Birden fazla dizini işlemek için genişletme
- **Yedek Oluşturma**: Otomatik yedek işlevselliği ekleme

## Entegrasyon
Bu script şunlarla entegre edilebilir:
- **Git Hook'ları**: Otomatik formatlama için pre-commit hook'ları
- **CI/CD Pipeline'ları**: Build süreçlerinde otomatik kod temizliği
- **IDE Araçları**: Geliştirme ortamlarında harici araçlar
- **Build Script'leri**: Proje build ve deployment script'lerinin parçası
- **Kod Kalite Araçları**: Linting ve formatlama araçlarıyla entegrasyon
- **Takım İş Akışları**: Standartlaştırılmış geliştirme süreçleri

## Performans
- **Verimli İşleme**: Sadece değişiklik gereken dosyaları okur ve yazar
- **Bellek Optimizasyonu**: Dosyaları tek tek işler, hepsini aynı anda değil
- **Hızlı Regex**: Kalıp eşleştirme için optimize edilmiş düzenli ifadeler kullanır
- **Minimal I/O**: Değişiklik tespiti yoluyla dosya sistemi işlemlerini azaltır

## Hata İşleme
Script çeşitli hata senaryolarını işler:
- **Dosya Erişim Hataları**: İzin sorunları veya kilitli dosyalar
- **Kodlama Sorunları**: UTF-8 olmayan dosyalar veya kodlama problemleri
- **Dizin Erişimi**: Eksik veya erişilemeyen dizinler
- **Disk Alanı**: Dosya değişiklikleri için yetersiz alan

## Sınırlamalar
- **Dosya Türü Özel**: Sadece `.ts`, `.tsx` ve `.vue` dosyalarını işler
- **UTF-8 Kodlama**: Tüm dosyalar için UTF-8 kodlaması varsayar
- **Tek Dizin**: Aynı anda bir kaynak dizini işler
- **Yedek Yok**: Otomatik yedek oluşturmaz (manuel yedek önerilir)