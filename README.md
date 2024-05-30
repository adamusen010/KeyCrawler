# URL Keyword Crawler

URL Keyword Crawler adalah alat untuk mencari URL di dalam domain atau subdomain tertentu yang mengandung kata kunci spesifik. Alat ini menggunakan `aiohttp` dan `asyncio` untuk melakukan permintaan HTTP secara asinkron, memungkinkan beberapa permintaan berjalan bersamaan, sehingga meningkatkan kecepatan pencarian URL.

## Fitur
- Crawling URL secara asinkron menggunakan `aiohttp` dan `asyncio`
- Pencarian kata kunci pada halaman yang di-crawl
- Output URL yang mengandung kata kunci spesifik

## Instalasi
Pastikan Anda telah menginstal dependensi yang diperlukan. Disarankan untuk menggunakan virtual environment.

### Langkah-langkah Instalasi
1. **Instalasi `virtualenv` (opsional, tapi disarankan)**:
    ```bash
    sudo apt install python3-virtualenv
    ```

2. **Buat dan Aktifkan Virtual Environment**:
    ```bash
    mkdir myproject
    cd myproject
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Instal Dependensi**:
    pip install -r dependensi.txt 

4. **Cara menggunakan 
    python3 crawl_tool.py -d https://example.com -k katakunci1 katakunci2 dst

		  SALAM 		HARMONI 
=============================================================================
			KeyCrawler v1.0 
