# javaToTxtConverter

## Açıklama
Bu script, bir dizindeki (alt dizinler dahil) tüm Java dosyalarını .txt uzantılı metin dosyalarına dönüştürür. Java kaynak kodunun dokümantasyon, analiz veya yedekleme amaçları için metin kopyalarını oluşturmak için kullanışlıdır. Yapay zeka araçlarına topku yükleme gibi ihtiyaçlarda kolaylık sağlar.

## Gereksinimler
- Bash
- find komutu
- cp komutu
- .java dosyaları olan Java projesi

## Kullanım
```bash
bash javaToTxtConverter.sh
```

## Ne Yapar
1. **Dosya Keşfi**: Tüm .java dosyalarını özyinelemeli olarak bulmak için `find` kullanır
2. **İsim Oluşturma**: .java uzantısını değiştirerek karşılık gelen .txt dosya isimlerini oluşturur
3. **Dosya Kopyalama**: Her .java dosyasını .txt karşılığına kopyalar
4. **İlerleme Raporlama**: Hangi dosyaların oluşturulduğunu gösterir

## Örnek
Aşağıdaki yapıya sahipseniz:
```
src/
├── main/
│   └── java/
│       ├── User.java
│       └── service/
│           └── UserService.java
```

Script çalıştırıldıktan sonra:
```
src/
├── main/
│   └── java/
│       ├── User.java
│       ├── User.txt
│       └── service/
│           ├── UserService.java
│           └── UserService.txt
```

## Çıktı
Dönüştürülen her dosya için script şunu gösterir:
```
Created: ./src/main/java/User.txt
Created: ./src/main/java/service/UserService.txt
```

## Kullanım Alanları
- **Dokümantasyon**: Dokümantasyon sistemleri için metin versiyonları oluşturma
- **Kod Analizi**: Metin analiz araçları için dosyaları hazırlama
- **Yedekleme**: Kaynak kodun okunabilir yedeklerini oluşturma
- **Geçiş**: .java dosyalarını işlemeyen sistemler için kod hazırlama
- **Metin İşleme**: Metin tabanlı araçların Java kodunu işlemesini sağlama
- **Arşiv Oluşturma**: Kaynak kodun metin arşivlerini oluşturma

## Özellikler
- **Özyinelemeli İşleme**: İç içe dizin yapılarını işler
- **Yapı Koruma**: Orijinal dizin hiyerarşisini korur
- **Yıkıcı Olmayan**: Orijinal .java dosyaları değişmeden kalır
- **Basit İşlem**: Yapılandırma gerektirmez
- **İlerleme Geri Bildirimi**: Dönüştürme ilerlemesini gösterir