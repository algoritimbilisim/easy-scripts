#!/bin/bash

VIDEO_PATH="$1"
PART_COUNT="$2"

if [ -z "$VIDEO_PATH" ] || [ -z "$PART_COUNT" ]; then
  echo "Kullanım: ./split_video.sh video_dosyası.mp4 parça_sayısı"
  exit 1
fi

# Toplam süreyi saniye cinsinden al
DURATION=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$VIDEO_PATH")
DURATION=${DURATION%.*} # ondalıklı kısmı at

# Her parçanın süresi
PART_DURATION=$((DURATION / PART_COUNT))

# Geriye kalan saniyeyi (bölünemeyen kısmı) hesapla
REMAINDER=$((DURATION % PART_COUNT))

FILENAME=$(basename -- "$VIDEO_PATH")
EXT="${FILENAME##*.}"
BASENAME="${FILENAME%.*}"

for ((i = 0; i < PART_COUNT; i++)); do
  START=$((i * PART_DURATION))
  
  # Son parçaya kalan saniyeyi ekle
  if [ "$i" -eq $((PART_COUNT - 1)) ]; then
    CURRENT_DURATION=$((PART_DURATION + REMAINDER))
  else
    CURRENT_DURATION=$PART_DURATION
  fi

  OUTPUT="${BASENAME}_part$((i+1)).$EXT"
  ffmpeg -y -ss "$START" -i "$VIDEO_PATH" -t "$CURRENT_DURATION" -c copy "$OUTPUT"
done

echo "Video başarıyla $PART_COUNT parçaya bölündü."

