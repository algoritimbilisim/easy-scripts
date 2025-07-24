# responseRequestGenerator

## Açıklama
Bu script, Java entity'leri için Request ve Response POJO (Plain Old Java Object) sınıflarını otomatik olarak oluşturur. `@Entity` annotasyonlu sınıfları tarar ve Spring Boot en iyi uygulamalarını takip ederek Lombok'un `@Data` annotasyonunu kullanan karşılık gelen Request ve Response DTO'larını oluşturur.

## Gereksinimler
- Python 3.x
- os ve re modülleri (yerleşik)
- JPA entity'leri olan Java projesi
- `@Entity` ile annotate edilmiş entity'ler
- Projede Lombok kütüphanesi
- Hedef dizin için yazma izinleri

## Kullanım
```bash
python responseRequestGenerator.py
```

Script, entity'leri aramak için kök dizini girmenizi isteyecektir.

## Ne yapar
1. **Entity Keşfi**: `@Entity` annotasyonlu Java dosyalarını özyinelemeli olarak arar
2. **Package Çıkarma**: Entity dosyalarından package deklarasyonunu çıkarır
3. **Sınıf Analizi**: Sınıf adını ve alan tanımlarını tanımlar
4. **Alan Ayrıştırma**: Private alanları tipleri ve isimleriyle birlikte çıkarır
5. **POJO Üretimi**: Lombok annotasyonları ile Request ve Response sınıfları oluşturur
6. **Dosya Oluşturma**: Üretilen POJO'ları uygun package yapısına kaydeder

## Üretilen POJO Yapısı

### Request Sınıfı
```java
package com.example.dto.request;

import lombok.Data;

@Data
public class EntityNameRequest {
    private String fieldName;
    private Integer fieldNumber;
    private Boolean fieldFlag;
    // ... diğer alanlar
}
```

### Response Sınıfı
```java
package com.example.dto.response;

import lombok.Data;

@Data
public class EntityNameResponse {
    private String fieldName;
    private Integer fieldNumber;
    private Boolean fieldFlag;
    // ... diğer alanlar
}
```

## Entity Gereksinimleri
Entity'leriniz bu yapıyı takip etmelidir:
```java
package com.example.entity;

import javax.persistence.*;

@Entity
@Table(name = "users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;
    
    private String username;
    private String email;
    private Boolean active;
    
    // getter ve setter'lar...
}
```

## Özellikler
- **Otomatik Keşif**: Belirtilen dizin ağacındaki tüm entity'leri bulur
- **Package Koruma**: DTO'lar için uygun package yapısını korur
- **Alan Çıkarma**: Tüm private alanları otomatik olarak çıkarır
- **Tip Desteği**: Generics dahil çeşitli Java tiplerini işler
- **Lombok Entegrasyonu**: Otomatik getter/setter'lar için `@Data` annotasyonu kullanır
- **İkili Üretim**: Hem Request hem Response sınıfları oluşturur
- **Uygun Import'lar**: Gerekli import ifadelerini içerir
- **İsimlendirme Konvansiyonu**: Standart DTO isimlendirme kalıplarını takip eder

## Desteklenen Alan Tipleri
Script otomatik olarak şunları tespit eder ve destekler:
- İlkel tipler: `int`, `long`, `boolean`, `double`, `float`
- Wrapper tipler: `Integer`, `Long`, `Boolean`, `Double`, `Float`
- String tipi: `String`
- Generic tipler: `List<String>`, `Set<Integer>`, vb.
- Özel nesne tipleri
- Tarih ve zaman tipleri

## Örnek

### Girdi Entity
```java
package com.example.entity;

import javax.persistence.*;
import java.time.LocalDateTime;
import java.util.List;

@Entity
@Table(name = "products")
public class Product {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;
    
    private String name;
    private Double price;
    private Boolean available;
    private LocalDateTime createdAt;
    private List<String> tags;
    
    // getter ve setter'lar...
}
```

### Üretilen Request
```java
package com.example.dto.request;

import lombok.Data;
import java.time.LocalDateTime;
import java.util.List;

@Data
public class ProductRequest {
    private Long id;
    private String name;
    private Double price;
    private Boolean available;
    private LocalDateTime createdAt;
    private List<String> tags;
}
```

### Üretilen Response
```java
package com.example.dto.response;

import lombok.Data;
import java.time.LocalDateTime;
import java.util.List;

@Data
public class ProductResponse {
    private Long id;
    private String name;
    private Double price;
    private Boolean available;
    private LocalDateTime createdAt;
    private List<String> tags;
}
```

## Proje Yapısı
```
project/
├── src/main/java/
│   ├── entity/
│   │   ├── User.java
│   │   ├── Product.java
│   │   └── Order.java
│   └── dto/
│       ├── request/
│       │   ├── UserRequest.java      # Üretilen
│       │   ├── ProductRequest.java   # Üretilen
│       │   └── OrderRequest.java     # Üretilen
│       └── response/
│           ├── UserResponse.java     # Üretilen
│           ├── ProductResponse.java  # Üretilen
│           └── OrderResponse.java    # Üretilen
└── responseRequestGenerator.py
```

## Kullanım Alanları
- **API Geliştirme**: REST API endpoint'leri için DTO'lar üretme
- **Veri Transferi**: Katmanlar arası veri transferi için nesneler oluşturma
- **Kod Tutarlılığı**: Tüm DTO'ların aynı kalıbı takip etmesini sağlama
- **Boilerplate Azaltma**: Manuel DTO oluşturmayı ortadan kaldırma
- **Proje Kurulumu**: Yeni projeler için DTO katmanını bootstrap etme
- **Refaktoring**: Yeni kalıplarla birden fazla DTO'yu güncelleme
- **Takım Standardizasyonu**: Tutarlı DTO yapısını zorlama

## Çıktı
Bulunan her entity için script:
- İşlenen entity'yi gösterir
- Üretilen Request ve Response dosya yollarını gösterir
- Başarılı POJO oluşturmayı raporlar

```
Processing entity: User
Generated: /path/to/dto/request/UserRequest.java
Generated: /path/to/dto/response/UserResponse.java

Processing entity: Product
Generated: /path/to/dto/request/ProductRequest.java
Generated: /path/to/dto/response/ProductResponse.java
```

## Özelleştirme
- **Package Yapısı**: DTO package isimlendirme konvansiyonlarını değiştirme
- **Sınıf Şablonları**: Üretilen sınıf yapısını özelleştirme
- **Alan Filtreleme**: Belirli alanları hariç tutmak için mantık ekleme
- **Annotasyon Desteği**: Ek annotasyonlar dahil etme
- **Import Yönetimi**: Import ifadelerini özelleştirme
- **İsimlendirme Kalıpları**: DTO isimlendirme konvansiyonlarını ayarlama

## Güvenlik Özellikleri
- **Dizin Doğrulama**: Hedef dizinlerin var olduğundan emin olur
- **Package Yapısı**: Uygun package hiyerarşisi oluşturur
- **Hata İşleme**: Dosya sistemi hatalarının zarif işlenmesi
- **Alan Doğrulama**: Çıkarılan alan bilgilerini doğrular


## Sınırlamalar
- **Alan Tespiti**: Belirli alan deklarasyon kalıplarına dayanır
- **Package Konvansiyonu**: Belirli package isimlendirmesini takip eder
- **Lombok Bağımlılığı**: Projede Lombok kütüphanesi gerektirir
- **Tek Entity Dosyası**: Dosya başına bir entity işler
- **Standart Annotasyonlar**: Standart JPA annotasyonları bekler