<div align="center">

# 📡 FTP Archive Search

### FTP Downloader & Text Search / Загрузка и поиск файлов по FTP

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![FTP](https://img.shields.io/badge/Protocol-FTP-238636?style=flat-square)
![ZIP](https://img.shields.io/badge/Archives-ZIP-596579?style=flat-square)

**A Python script for downloading ZIP archives and searching files / Python-скрипт для загрузки ZIP-архивов и поиска по файлам**

</div>

---

## 📖 About / О проекте

**EN:** This repository contains an experimental script that connects to an FTP server, downloads ZIP files from a selected folder, extracts the archives and searches extracted text files for a user-provided string. The current example is configured for the public procurement FTP server (`ftp.zakupki.gov.ru`) and a regional contracts directory.

**RU:** В репозитории находится экспериментальный скрипт для подключения к FTP-серверу, скачивания ZIP-архивов из указанного каталога, распаковки и поиска заданной строки в извлечённых текстовых файлах. В примере настроен FTP-сервер госзакупок (`ftp.zakupki.gov.ru`) и каталог региональных контрактов.

## 🧩 Features / Возможности

- FTP connection / Подключение к FTP
- ZIP archive downloads / Скачивание ZIP-архивов
- Archive extraction / Распаковка архивов
- Text search through downloaded files / Поиск текста в скачанных файлах
- Progress bar using `tqdm` / Индикатор прогресса с `tqdm`

## 📁 Project Files / Файлы проекта

| File / Файл | Description / Описание |
| --- | --- |
| [`FTP.py`](FTP.py) | Downloader, extraction and search logic / Логика загрузки, распаковки и поиска |

## ⚙️ Requirements / Требования

- Python 3
- `tqdm`

```bash
pip install tqdm
```

## ▶️ Getting Started / Запуск

```bash
git clone https://github.com/PetrShestakov/ftp.git
cd ftp
python FTP.py
```

**EN:** The script asks for a local destination directory and a text search query. Server connection settings are currently specified inside `FTP.py`. Review the code and settings before use.

**RU:** Скрипт запрашивает локальную папку для сохранения и текст для поиска. Настройки подключения к серверу сейчас указаны в `FTP.py`. Перед использованием проверьте код и параметры.

> **Development status / Статус разработки:** This is an experimental script, not a production-ready downloader. The current version has issues to fix (including the destination path reference inside the download function) and may not run successfully without changes. / Это экспериментальный скрипт, а не готовое приложение. В текущем коде есть ошибки (в том числе обращение к пути сохранения внутри функции загрузки), поэтому перед полноценным запуском потребуются исправления.

> **Security / Безопасность:** Download and extract archives only from trusted sources. The script currently extracts ZIP files without validating entry paths. / Скачивайте и распаковывайте архивы только из доверенных источников. Сейчас скрипт не проверяет пути файлов внутри ZIP.

---

<div align="center">

[👤 GitHub Profile / Мой профиль](https://github.com/PetrShestakov)

</div>
