# Kullanışlı Script Koleksiyonu

Bu depo, **Python** ve **Bash** ile yazılmış küçük, kullanışlı scriptlerin bir koleksiyonunu içerir. Bu scriptler basit, tekrarlayan görevleri çözmek veya yaygın işlemleri otomatikleştirmek için tasarlanmıştır.

Her script kendi klasöründe organize edilmiştir ve nasıl kullanılacağını açıklayan özel bir `README.md` dosyası ile birlikte gelir.

## Amaç

- Açık kaynak topluluğu ile faydalı araçları paylaşmak
- Sık kullanılan scriptleri tek bir yerde organize etmek
- Günlük veya tekrarlayan geliştirme/yönetim görevlerini otomatikleştirmek
- İşbirliği ve katkıları teşvik etmek

## Dizin Yapısı

```
easy-scripts/
├── <script-adı>/
│   ├── script.py / script.sh
│   ├── README.md
│   └── (opsiyonel) örnek veri / çıktı / yapılandırma
```

### Örnek:

```
easy-scripts/
└── disk-usage-check/
    ├── check_disk.sh
    └── README.md
```

## Mevcut Scriptler

### Geliştirme ve Kod Yönetimi
- **docker-kill**: Docker servislerini zorla durdurur ve sıfırlar, bağlantı sorunlarını çözer
- **git-status-recursive**: Dizin ağacındaki tüm Git depolarının durumunu özyinelemeli olarak kontrol eder
- **git-summary**: Git commit geçmişinin kapsamlı CSV raporunu oluşturur
- **javaEntityToTsGenerator**: Java JPA entity sınıflarını TypeScript arayüzlerine otomatik dönüştürür
- **javaToTxtConverter**: Java dosyalarını .txt uzantılı metin dosyalarına dönüştürür
- **openApiGenerator**: Spring Boot REST controller'ları için OpenAPI 3.0 spesifikasyonu oluşturur
- **responseRequestGenerator**: Java entity'ler için Request ve Response POJO sınıfları otomatik üretir

### Kod Formatlama ve Temizlik
- **remove-console-logs**: JavaScript/TypeScript dosyalarından console log ifadelerini kaldırır
- **remove-extra-blank-lines**: TypeScript, TSX ve Vue.js dosyalarından fazla boş satırları temizler

### Dosya ve Dizin İşlemleri
- **pageStructureCopy**: Kaynak dizinin yapısını hedef dizine kopyalar (sadece klasör hiyerarşisi)
- **split-video**: Video dosyasını belirtilen sayıda eşit parçaya böler

## Nasıl Kullanılır

1.  Bu depoyu klonlayın:
    ```bash
    git clone https://github.com/algoritimbilisim/easy-scripts.git
    cd easy-scripts
    ```

2.  İlgilendiğiniz script klasörüne gidin:
    ```bash
    cd docker-kill
    ```

3.  Scripti çalıştırmak için yerel `README.md` dosyasındaki talimatları takip edin.

## Script Kuralları

Her script kendi alt klasörüne yerleştirilmeli ve şunları içermelidir:

- Ana script dosyası (`.sh` veya `.py`)
- Kullanım detayları içeren bir `README.md` dosyası
- Herhangi bir ek kaynak veya bağımlılık (gerekirse)

## Katkıda Bulunma

Katkılar memnuniyetle karşılanır! Yeni bir script eklemek için:

- Depoyu fork edin
- `easy-scripts/` altında yeni bir klasör oluşturun
- Scriptinizi ve bir `README.md` dosyası ekleyin
- Açık bir açıklama ile Pull Request açın

## Lisans

Bu proje Apache 2.0 Lisansı altında lisanslanmıştır.