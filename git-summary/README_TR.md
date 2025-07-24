# git-summary

## Açıklama
Bu script, her commit için eklenen ve çıkarılan satır istatistikleri dahil olmak üzere Git commit geçmişinin kapsamlı bir CSV raporunu oluşturur. Elektronik tablo uygulamalarında veya veri analizi araçlarında kolayca analiz edilebilecek yapılandırılmış bir özet oluşturur.

## Gereksinimler
- Bash
- Git deposu (Git deposu içinde çalıştırılmalıdır)
- awk komutu

## Kullanım
```bash
bash git_summary.sh
```

## Çıktı
Aşağıdaki sütunları içeren `git_commit_summary.csv` adlı bir dosya oluşturur:
- **tarih**: YYYY-AA-GG formatında commit tarihi
- **commit**: Kısa commit hash'i
- **eklenen**: Commit'te eklenen satır sayısı
- **cikartilan**: Commit'te çıkarılan satır sayısı
- **mesaj**: Commit mesajı (CSV uyumluluğu için tırnak içinde)

## Ne Yapar
1. **Veri Çıkarma**: Detaylı commit bilgisi almak için `git log` komutunu `--numstat` ile kullanır
2. **İstatistik Hesaplama**: Her commit için eklenen ve çıkarılan satırları toplar
3. **CSV Formatı**: Verileri uygun tırnak işaretleri ile virgülle ayrılmış değerler olarak formatlar
4. **Dosya Oluşturma**: Analiz için kullanıma hazır CSV dosyası oluşturur

## Örnek Çıktı
```csv
tarih,commit,eklenen,cikartilan,mesaj
2024-01-15,a1b2c3d,45,12,"Kullanıcı kimlik doğrulama özelliği eklendi"
2024-01-14,e4f5g6h,23,8,"Veritabanı bağlantı sorunu düzeltildi"
2024-01-13,i7j8k9l,67,34,"Ödeme işleme modülü refactor edildi"
```

## Kullanım Alanları
- **Proje Analizi**: Geliştirme kalıplarını ve verimliliği anlama
- **Kod İncelemesi**: Daha yakın inceleme gerektirebilecek büyük commit'leri tanımlama
- **Takım Metrikleri**: Takım üyeleri arasında katkı kalıplarını analiz etme
- **Sürüm Planlama**: Sürümler arası değişikliklerin kapsamını anlama
- **Dokümantasyon**: Geliştirme raporları ve özetleri oluşturma

## Özellikler
- **Kapsamlı Veri**: Hem nicel (değiştirilen satırlar) hem de nitel (commit mesajı) bilgileri içerir
- **CSV Formatı**: Excel, Google Sheets veya veri analizi araçlarına kolayca aktarılabilir
- **Uygun Kaçış**: Özel karakterler içeren commit mesajlarını doğru şekilde işler
- **Kronolojik Sıra**: Commit'ler en yeniden en eskiye doğru listelenir