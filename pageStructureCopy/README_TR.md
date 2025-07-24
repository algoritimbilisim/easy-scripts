# pageStructureCopy

## Açıklama
Bu script, kaynak dizinden hedef dizine sadece klasör yapısını kopyalar, dosyaları kopyalamaz. Test, organizasyon veya şablon amaçları için dizin yapılarını çoğaltmak için kullanışlıdır.

## Gereksinimler
- Python 3.x
- os modülü (yerleşik)
- Var olan kaynak dizin
- Hedef dizin için yazma izinleri

## Kullanım
```bash
python pageStructureCopy.py
```

## Yapılandırma
Script içerisinde kaynak ve hedef dizinleri değiştirin:
```python
kaynak_dizin = 'src/views/pages'  # Kaynak dizin yolu
hedef_dizin = 'cypress/e2e'       # Hedef dizin yolu
```

## Ne yapar
1. **Dizin Gezinme**: `os.walk()` kullanarak kaynak dizini özyinelemeli olarak gezer
2. **Yol Hesaplama**: Yapıyı korumak için kaynaktan göreli yolları hesaplar
3. **Dizin Oluşturma**: Hedef konumda karşılık gelen dizinleri oluşturur
4. **Varlık Kontrolü**: Oluşturmadan önce dizinlerin zaten var olup olmadığını kontrol eder
5. **İlerleme Raporlama**: Hangi dizinlerin oluşturulduğunu veya zaten var olduğunu gösterir

## Örnek
Aşağıdaki kaynak yapınız varsa:
```
src/views/pages/
├── admin/
│   ├── users/
│   └── settings/
├── public/
│   ├── home/
│   └── about/
└── dashboard/
    ├── analytics/
    └── reports/
```

Script çalıştırıldıktan sonra hedef yapı şöyle olacaktır:
```
cypress/e2e/
├── admin/
│   ├── users/
│   └── settings/
├── public/
│   ├── home/
│   └── about/
└── dashboard/
    ├── analytics/
    └── reports/
```

## Çıktı
Her dizin işlemi için script şunları gösterir:
```
Oluşturuluyor: cypress/e2e/admin/users
Zaten mevcut: cypress/e2e/public
Oluşturuluyor: cypress/e2e/dashboard/analytics
```

## Kullanım Alanları
- **Test Yapısı Kurulumu**: Kaynak kodu yansıtan test dizin yapıları oluşturma
- **Proje Şablonları**: Önceden tanımlanmış klasör yapıları ile proje iskeleti kurma
- **Yedek Hazırlığı**: Organize yedekler için dizin yapıları oluşturma
- **Taşıma Planlaması**: Dosya taşımadan önce hedef yapıları hazırlama
- **Geliştirme Ortamı**: Ortamlar arası tutarlı klasör yapıları kurma
- **Dokümantasyon Organizasyonu**: Yapılandırılmış dokümantasyon hiyerarşileri oluşturma

## Özellikler
- **Yıkıcı Olmayan**: Sadece dizin oluşturur, mevcut olanları değiştirmez
- **Özyinelemeli İşleme**: Herhangi bir derinlikteki iç içe dizin yapılarını işler
- **Göreli Yol Koruma**: Tam dizin hiyerarşisini korur
- **Varlık Farkındalığı**: Zaten var olan dizinleri atlar
- **İlerleme Geri Bildirimi**: Gerçek zamanlı oluşturma durumunu gösterir
- **Çapraz Platform**: Windows, macOS ve Linux'ta çalışır

## Özelleştirme
- **Kaynak Yolu**: `kaynak_dizin`'i istediğiniz kaynak dizine değiştirin
- **Hedef Yolu**: `hedef_dizin`'i istediğiniz hedef dizine değiştirin
- **Filtreleme**: Belirli dizinleri atlamak için koşullar ekleyin
- **Loglama**: Daha ayrıntılı loglama ile çıktıyı geliştirin
- **Hata İşleme**: Sağlam hata işleme için try-catch blokları ekleyin

## Güvenlik Notları
- Script sadece dizin oluşturur, dosyaları kopyalamaz
- Mevcut dizinler korunur ve üzerine yazılmaz
- Hedef dizin için yazma izinleriniz olduğundan emin olun
- Çalıştırmadan önce kaynak ve hedef yollarını doğrulayın