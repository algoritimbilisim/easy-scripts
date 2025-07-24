# Useful Scripts Collection

This repository contains a collection of small, useful scripts written in **Python** and **Bash**. These scripts are designed to solve simple, repetitive tasks or automate common operations. 

Each script is organized in its own folder and comes with a dedicated `README.md` file explaining how to use it.

## Purpose

- Share helpful utilities with the open-source community
- Organize frequently used scripts in a single place
- Automate daily or repetitive development/administration tasks
- Encourage collaboration and contributions

## Directory Structure

```
easy-scripts/
├── <script-name>/
│   ├── script.py / script.sh
│   ├── README.md
│   └── (optional) sample data / output / config
```

### Example:

```
easy-scripts/
└── disk-usage-check/
    ├── check_disk.sh
    └── README.md
```

## Available Scripts

### Development & Code Management
- **docker-kill**: Docker servislerini zorla durdurur ve sıfırlar, bağlantı sorunlarını çözer
- **git-status-recursive**: Dizin ağacındaki tüm Git depolarının durumunu özyinelemeli olarak kontrol eder
- **git-summary**: Git commit geçmişinin kapsamlı CSV raporunu oluşturur
- **javaEntityToTsGenerator**: Java JPA entity sınıflarını TypeScript arayüzlerine otomatik dönüştürür
- **javaToTxtConverter**: Java dosyalarını .txt uzantılı metin dosyalarına dönüştürür
- **openApiGenerator**: Spring Boot REST controller'ları için OpenAPI 3.0 spesifikasyonu oluşturur
- **responseRequestGenerator**: Java entity'ler için Request ve Response POJO sınıfları otomatik üretir

### Code Formatting & Cleanup
- **remove-console-logs**: JavaScript/TypeScript dosyalarından console log ifadelerini kaldırır
- **remove-extra-blank-lines**: TypeScript, TSX ve Vue.js dosyalarından fazla boş satırları temizler

### File & Directory Operations
- **pageStructureCopy**: Kaynak dizinin yapısını hedef dizine kopyalar (sadece klasör hiyerarşisi)
- **split-video**: Video dosyasını belirtilen sayıda eşit parçaya böler

## How to Use

1.  Clone this repository:
    ```bash
    git clone https://github.com/algoritimbilisim/easy-scripts.git
    cd easy-scripts
    ```

2.  Navigate to the script folder you're interested in:
    ```bash
    cd docker-kill
    ```

3.  Follow the instructions in the local `README.md` file to run the script.

## Script Guidelines

Each script should be placed in its own subfolder and must include:

- The main script file (`.sh` or `.py`)
- A `README.md` file with usage details
- Any additional resources or dependencies (if necessary)

## Contributing

Contributions are welcome! To add a new script:

- Fork the repository
- Create a new folder under `easy-scripts/`
- Add your script and a `README.md` file
- Open a Pull Request with a clear description

## License

This project is licensed under the Apache 2.0 License.
