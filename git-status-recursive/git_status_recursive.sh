#!/bin/bash

# Sarı renk tanımlaması
YELLOW='\033[1;33m'
NC='\033[0m' # Renk sıfırlama

# Kullanım talimatı
usage() {
  echo "Kullanım: $0 <derinlik> (Örnek: $0 2)"
  exit 1
}

# Parametre kontrolü
if [ -z "$1" ]; then
  usage
fi

# Derinlik parametresini al
DEPTH=$1

# Bulunduğunuz dizinden itibaren belirtilen derinliğe kadar olan alt dizinlerde dolaş
explore_directory() {
  local current_depth=$1
  local dir_path=$2

  if [ $current_depth -le $DEPTH ]; then

    # Eğer git dizini varsa git status komutunu çalıştır
    if [ -d ".git" ]; then
      # Mevcut dizinin yolunu sarı renkte yazdır
      echo -e "${YELLOW}$(pwd)${NC}"
      git status
    #else
     # echo "Bu dizin bir git deposu değil."
    fi

    # Eğer derinlik sınırına ulaşmadıysak, bir alt dizinlere git
    for dir in */; do
      if [ -d "$dir" ]; then
        cd "$dir"
        explore_directory $((current_depth + 1)) "$(pwd)"
        cd ..
      fi
    done
  fi
}

# Script'in çalışmaya başladığı dizin
start_dir=$(pwd)

# Dizini keşfetmeye başla (0 derinlikten başla)
explore_directory 0 "$start_dir"
