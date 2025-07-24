import os

def kopyala_dizin_yapisi(kaynak_dizin, hedef_dizin):
    # Tüm alt dizin ve dosyaları tarar
    for root, dirs, files in os.walk(kaynak_dizin):
        # Şu anki dizinin kaynak diziye göre göreceli yolunu hesapla
        relative_path = os.path.relpath(root, kaynak_dizin)
        # Hedefteki tam dizin yolu
        hedef_dizin_yolu = os.path.join(hedef_dizin, relative_path)
        
        # Hedef dizin yolu yoksa oluştur
        if not os.path.exists(hedef_dizin_yolu):
            print(f'Oluşturuluyor: {hedef_dizin_yolu}')
            os.makedirs(hedef_dizin_yolu)
        else:
            print(f'Zaten mevcut: {hedef_dizin_yolu}')
            
# Kullanım
kaynak_dizin = 'src/views/pages'  # Kök dizin yolu buraya gelecek
hedef_dizin = 'cypress/e2e'   # Hedef dizin yolu buraya gelecek

kopyala_dizin_yapisi(kaynak_dizin, hedef_dizin)
