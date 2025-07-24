#!/bin/bash

# Mevcut dizindeki tüm .java dosalarını bulur (alt dizinlerle birlikte)
find . -type f -name "*.java" | while read java_file; do
  # .java dosyasının tam yolundan .txt dosyasının adını üret
  txt_file="${java_file%.java}.txt"

  # .java dosyasını .txt dosyası olarak kopyala
  cp "$java_file" "$txt_file"

  echo "Created: $txt_file"
done
