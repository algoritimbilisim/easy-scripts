# openApiGenerator

## Açıklama
Bu script, Spring Boot REST controller'ları için otomatik olarak OpenAPI 3.0 spesifikasyon dosyaları oluşturur. Java controller dosyalarını analiz eder ve endpoint'ler, request/response şemaları ve parametre tanımları dahil olmak üzere YAML formatında kapsamlı API dokümantasyonu oluşturur.

## Gereksinimler
- Python 3.x
- PyYAML kütüphanesi (`pip install pyyaml`)
- Controller'ları olan Java Spring Boot projesi
- Request ve Response DTO sınıfları
- Standart REST controller yapısı

## Kullanım
```bash
python openApiGenerator.py
```

## Ne Yapar
1. **Controller Keşfi**: Projedeki Java controller dosyalarını tarar
2. **Endpoint Analizi**: REST endpoint'lerini ve HTTP metodlarını çıkarır
3. **Parametre Ayrıştırma**: Path parametrelerini, query parametrelerini ve request body'lerini tanımlar
4. **Şema Oluşturma**: Request/Response sınıflarından OpenAPI şemaları oluşturur
5. **Dokümantasyon Oluşturma**: Tam OpenAPI YAML dosyaları oluşturur
6. **Eksik Endpoint Tespiti**: Eksik olabilecek standart REST endpoint'lerini önerir

## Oluşturulan OpenAPI Özellikleri
- **Tam Spesifikasyon**: OpenAPI 3.0 uyumlu YAML dosyaları
- **Endpoint Dokümantasyonu**: Uygun HTTP metodları ile tüm REST endpoint'leri
- **Şema Tanımları**: Request ve Response nesne şemaları
- **Parametre Dokümantasyonu**: Path, query ve body parametreleri
- **Response Kodları**: Standart HTTP response kodları (200, 201, 400, 404, 500)
- **Tip Eşleme**: Java tiplerinin OpenAPI tiplerine eşlenmesi
- **Sayfalama Desteği**: Sayfalanmış response'lar için özel işleme

## Desteklenen Java Tipleri
| Java Tipi | OpenAPI Tipi | Format |
|-----------|--------------|--------|
| String | string | - |
| Integer/int | integer | int32 |
| Long/long | integer | int64 |
| Double/double | number | double |
| Float/float | number | float |
| Boolean/boolean | boolean | - |
| LocalDate | string | date |
| LocalDateTime | string | date-time |
| BigDecimal | number | - |
| UUID | string | uuid |

## Endpoint Sınıflandırması
Script, metod isimlerine ve HTTP metodlarına göre endpoint'leri otomatik olarak sınıflandırır:
- **GET All**: `getAll*`, `findAll*`, `listAll*`
- **GET By ID**: `get*ById`, `find*WithId`
- **CREATE**: `create*`, `add*`, `save*`, `store*`
- **UPDATE**: `update*`, `edit*`, `modify*`
- **DELETE**: `delete*`, `remove*`, `destroy*`
- **SEARCH**: `search*`, `find*`, `query*`, `filter*`

## Çıktı Yapısı
```
api_contracts/
├── User_api.yaml
├── Product_api.yaml
└── Order_api.yaml
```

## Örnek Oluşturulan API
```yaml
openapi: 3.0.0
info:
  title: User API
  version: 1.0.0
paths:
  /users:
    get:
      summary: Get all users
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/UserResponse'
    post:
      summary: Create user
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UserRequest'
components:
  schemas:
    UserRequest:
      type: object
      properties:
        name:
          type: string
        email:
          type: string
    UserResponse:
      type: object
      properties:
        id:
          type: integer
          format: int64
        name:
          type: string
        email:
          type: string
```

## Özellikler
- **Strateji Deseni**: Takılabilir bileşenlerle modüler tasarım
- **Tip Güvenliği**: Uygun Java'dan OpenAPI'ye tip dönüşümü
- **Sayfalama Farkındalığı**: Spring Data Page response'larını işler
- **Generic Desteği**: `List<T>`, `Page<T>` gibi generic tipleri destekler
- **Eksik Endpoint Tespiti**: Standart CRUD endpoint'lerini önerir
- **Esnek Mimari**: Genişletmesi ve özelleştirmesi kolay
- **Hata İşleme**: Ayrıştırma hatalarını zarif şekilde işler

## Mimari Bileşenler
- **EndpointClassifierStrategy**: Endpoint tiplerini sınıflandırır
- **EndpointDetectorStrategy**: Eksik standart endpoint'leri tespit eder
- **JavaTypeConverter**: Java tiplerini OpenAPI tiplerine dönüştürür
- **ParameterParser**: Metod parametrelerini ayrıştırır
- **JavaClassParser**: Java sınıf dosyalarını ayrıştırır
- **JavaControllerParser**: Controller dosyalarını ayrıştırır
- **ReturnTypeHandler**: Metod dönüş tiplerini işler

## Kullanım Alanları
- **API Dokümantasyonu**: Kapsamlı API dokümantasyonu oluşturma
- **Frontend Geliştirme**: Frontend takımları için net API sözleşmeleri sağlama
- **Test**: Otomatik test için API spesifikasyonları oluşturma
- **İstemci Oluşturma**: OpenAPI spec'lerinden API istemcileri oluşturma
- **API Yönetişimi**: Tutarlı API tasarım desenlerini sağlama
- **Entegrasyon**: Üçüncü taraf entegrasyonlarını kolaylaştırma

## Özelleştirme
- **Tip Eşlemeleri**: Özel tip eşlemeleri için `StandardJavaTypeConverter`'ı değiştirin
- **Endpoint Sınıflandırması**: Özel desenler için `RegexEndpointClassifier`'ı genişletin
- **Response İşleme**: Belirli response tipleri için `StandardReturnTypeHandler`'ı özelleştirin
- **Parametre Ayrıştırma**: Karmaşık parametre desenleri için `RegexParameterParser`'ı geliştirin

## Yapılandırma
Script aşağıdakileri değiştirerek yapılandırılabilir:
- Kök dizin yolu (varsayılan: `src/main/java`)
- Çıktı dizini (varsayılan: `api_contracts`)
- Tip dönüşüm eşlemeleri
- Endpoint sınıflandırma desenleri