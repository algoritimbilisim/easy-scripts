# docker-kill (Docker Sıfırlama)

## Açıklama
Bu script, macOS'ta Docker servislerini zorla durdurur ve sıfırlar. Docker işlemlerini sonlandırır, servis binary'lerini kaldırır ve Docker uygulamasından yeniden yükler. Docker bağlantı sorunlarını veya bozuk kurulumları düzeltmek için kullanışlıdır.

## Gereksinimler
- Bash
- macOS
- `/Applications/Docker.app` konumunda yüklü Docker Desktop
- sudo yetkileri

## Kullanım
```bash
bash docker-kill.sh
```

## Ne Yapar
1. **Docker İşlemlerini Durdur**: pkill kullanarak Docker ile ilgili tüm işlemleri sonlandırır
2. **Servisleri Durdur**: Docker vmnetd ve socket servislerini launchctl'den kaldırır
3. **Binary'leri Kaldır**: Sistem dizinlerinden mevcut Docker yardımcı binary'lerini siler
4. **Binary'leri Yeniden Yükle**: Docker.app kurulumundan yeni binary'leri kopyalar

## Etkilenen Servisler
- `com.docker.vmnetd` - Docker sanal ağ daemon'u
- `com.docker.socket` - Docker socket servisi

## Değiştirilen Dosyalar
- `/Library/PrivilegedHelperTools/com.docker.vmnetd`
- `/Library/PrivilegedHelperTools/com.docker.socket`

## Ne Zaman Kullanılır
- Docker başlamıyor veya bağlanamıyor
- Container'larla ağ bağlantısı sorunları
- Düzgün tamamlanmayan Docker güncellemelerinden sonra
- Docker servisleri yanıt vermediğinde

## Uyarı
Bu script sudo yetkileri gerektirir ve Docker işlemlerini zorla sonlandırır. Çalıştırmadan önce çalışan container'lardaki işlerinizi kaydettiğinizden emin olun.