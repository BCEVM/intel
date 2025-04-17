from scrapers.x_scraper import scrape_x
from scrapers.reddit_scraper import scrape_reddit
from scrapers.telegram_scraper import scrape_telegram
import asyncio, json, csv, os

keyword = input("Masukkan keyword pencarian: ")

x_data = scrape_x(keyword)
reddit_data = scrape_reddit(keyword)
telegram_data = asyncio.run(scrape_telegram(keyword))

all_data = x_data + reddit_data + telegram_data

with open("output/results.json", "w") as f:
    json.dump(all_data, f, indent=2)

with open("output/results.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=all_data[0].keys())
    writer.writeheader()
    writer.writerows(all_data)

print(f"[+] Selesai! Total hasil: {len(all_data)}. Cek folder output.")