#!/bin/bash

# Çıktı dosyası adı
OUTPUT_FILE="git_commit_summary.csv"

# Başlık satırı
echo "tarih,commit,eklenen,cikartilan,mesaj" > "$OUTPUT_FILE"

# Git log'dan veriyi al ve CSV formatında dosyaya ekle
git log --pretty=format:"@@@%ad|%h|%s" --date=short --numstat | awk -v OFS="," -v outfile="$OUTPUT_FILE" '
/^@@@/ {
  if (printed) {
    print date, hash, added, removed, "\"" msg "\"" >> outfile
  }
  split(substr($0, 4), a, "|")
  date = a[1]
  hash = a[2]
  msg = a[3]
  added = 0
  removed = 0
  printed = 1
  next
}
NF == 3 {
  added += $1
  removed += $2
}
END {
  if (printed) {
    print date, hash, added, removed, "\"" msg "\"" >> outfile
  }
}'

