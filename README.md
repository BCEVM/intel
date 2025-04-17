# ThreatIntel - Cyber Threat Intelligence Tool

**ThreatIntel** adalah tools Cyber Threat Intelligence modular yang mampu melakukan scraping percakapan dari platform **X (Twitter)**, **Reddit**, dan **Telegram** hanya dengan memasukkan keyword tertentu. Cocok untuk tracking ancaman, aktivitas kelompok, atau percakapan mencurigakan secara real-time.

---

## Fitur Utama

- [x] Scrape percakapan berdasarkan keyword dari:
  - X (Twitter) via `snscrape`
  - Reddit via `Pushshift API`
  - Telegram via `Telethon`
- [x] Output data dalam format `JSON` dan `CSV`
- [x] Berjalan di **Termux**, Linux, atau Windows
- [x] Struktur modular dan siap dikembangkan lebih lanjut

---

## Instalasi

### 1. Clone repository
```bash
git clone https://github.com/yourusername/threatintel.git
cd threatintel
pip install -r requirements.txt
