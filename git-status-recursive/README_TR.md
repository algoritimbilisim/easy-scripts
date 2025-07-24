# git-status-recursive

## Açıklama
Bu script, belirtilen derinliğe kadar dizinleri özyinelemeli olarak keşfeder ve Git deposu içeren her dizinde `git status` komutunu çalıştırır. Bir dizin ağacındaki birden fazla Git deposunun durumuna dair kapsamlı bir genel bakış sağlar.

## Gereksinimler
- Bash
- Git
- Birden fazla Git deposu içeren dizin yapısı

## Kullanım
```bash
bash git_status_recursive.sh <derinlik>
```

### Parametreler
- `<derinlik>`: Keşfedilecek maksimum dizin derinliği (zorunlu)

### Örnekler
```bash
# Mevcut dizin ve 1 seviye derinlikte Git durumunu kontrol et
bash git_status_recursive.sh 1

# Mevcut dizin ve 2 seviye derinlikte Git durumunu kontrol et
bash git_status_recursive.sh 2
```

## Ne Yapar
1. **Dizin Gezinme**: Belirtilen derinliğe kadar dizinleri özyinelemeli olarak keşfeder
2. **Git Algılama**: `.git` klasörleri içeren dizinleri tanımlar
3. **Durum Gösterimi**: Bulunan her Git deposunda `git status` çalıştırır
4. **Yol Vurgulama**: Daha iyi görünürlük için mevcut depo yolunu sarı renkte gösterir
5. **Derinlik Kontrolü**: Aşırı özyinelemeyi önlemek için keşfi sınırlar

## Çıktı Formatı
- Depo yolları **sarı** renkte gösterilir
- Her yolun ardından standart `git status` çıktısı gelir
- Git olmayan dizinler sessizce atlanır

## Kullanım Alanları
- Çalışma alanında birden fazla Git deposunu yönetme
- Projeler arası commit edilmemiş değişikliklere hızlı genel bakış
- Büyük işlemlerden önce depo durumunu toplu kontrol etme
- Geliştirme ortamı sağlık kontrolleri
- Proje portföyü yönetimi

## Özellikler
- **Renkli Çıktı**: Renkli dizin yolları ile gelişmiş okunabilirlik
- **Derinlik Sınırlama**: Karmaşık dizin yapılarında sonsuz özyinelemeyi önler
- **Sessiz Atlama**: Sadece gerçek Git depoları için çıktı gösterir
- **Kullanım Yardımı**: Yanlış parametreler için yerleşik kullanım talimatları