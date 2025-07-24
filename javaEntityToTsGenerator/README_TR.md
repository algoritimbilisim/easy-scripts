# javaEntityToTsGenerator

## Açıklama
Bu script, Java JPA entity sınıflarını otomatik olarak TypeScript interface'lerine dönüştürür, aynı paket yapısını korur ve karmaşık tip eşlemelerini işler. Büyük kod tabanlarının daha hızlı dönüştürülmesi için multiprocessing desteği sağlar.

## Gereksinimler
- Python 3.x
- JPA entity sınıfları olan Java projesi
- multiprocessing desteği

## Kullanım
```bash
python javaEntityToTsGenerator.py
```

Script, kök dizin için (örn. `src/main/java`) sorgu yapacaktır.

## Ne Yapar
1. **Entity Keşfi**: `@Entity` annotation'ı olan Java dosyalarını tarar
2. **Alan Çıkarma**: Regex kullanarak private alanları ve tiplerini çıkarır
3. **Tip Eşleme**: Java tiplerini TypeScript karşılıklarına dönüştürür
4. **Import Oluşturma**: Entity ilişkileri için uygun import ifadeleri oluşturur
5. **Yapı Koruma**: TypeScript'te aynı paket yapısını korur
6. **Paralel İşleme**: Daha hızlı dönüştürme için multiprocessing kullanır

## Tip Eşlemeleri
- `String` → `string`
- `Integer`, `int`, `Long`, `long`, `Double`, `double`, `Float`, `float` → `number`
- `Boolean`, `boolean` → `boolean`
- `LocalDate`, `LocalDateTime`, `Date` → `Date`
- `List<T>`, `Set<T>` → `T[]`
- Özel entity tipleri → İçe aktarılan TypeScript interface'leri

## Çıktı Yapısı
```
ts_models/
├── com/
│   └── example/
│       └── entity/
│           ├── User.ts
│           ├── Order.ts
│           └── Product.ts
```

## Örnek Dönüştürme

### Java Entity
```java
package com.example.entity;

@Entity
public class User {
    private Long id;
    private String name;
    private LocalDate birthDate;
    private List<Order> orders;
}
```

### Oluşturulan TypeScript
```typescript
import type { Order } from './Order';

export interface User {
  id?: number;
  name?: string;
  birthDate?: Date;
  orders?: Order[];
}
```

## Özellikler
- **Otomatik Import'lar**: Entity ilişkileri için göreceli import yolları oluşturur
- **Opsiyonel Alanlar**: Tüm alanlar `?` ile opsiyonel olarak işaretlenir
- **Generic Desteği**: `List<T>`, `Set<T>` gibi generic tipleri işler
- **Paket Yapısı**: Java paket hiyerarşisini korur
- **Multiprocessing**: Büyük projeler için daha hızlı işleme
- **İlişki İşleme**: İlgili entity'leri uygun şekilde içe aktarır

## Kullanım Alanları
- Frontend-backend tip senkronizasyonu
- API client oluşturma
- Tip güvenli frontend geliştirme
- Dokümantasyon oluşturma
- Kod geçiş projeleri