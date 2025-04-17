import csv
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import SearchGlobal
from getpass import getpass

# Output paths
JSON_PATH = "results.json"
CSV_PATH = "results.csv"

# Save results to JSON and CSV
def save_results(data):
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    with open(CSV_PATH, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["platform", "user", "text", "timestamp", "link"])
        writer.writeheader()
        for row in data:
            writer.writerow(row)

# Scrape Reddit
def scrape_reddit(keyword):
    print("[+] Scraping Reddit...")
    url = f"https://api.pushshift.io/reddit/search/comment/?q={keyword}&size=50"
    resp = requests.get(url)
    results = []
    if resp.status_code == 200:
        for item in resp.json().get("data", []):
            results.append({
                "platform": "Reddit",
                "user": item.get("author"),
                "text": item.get("body"),
                "timestamp": datetime.utcfromtimestamp(item["created_utc"]).isoformat(),
                "link": f"https://reddit.com{item.get('permalink', '')}"
            })
    return results

# Scrape X (Twitter) via HTML
def scrape_x(keyword):
    print("[+] Scraping X...")
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    search_url = f"https://nitter.net/search?f=tweets&q={keyword}&since=&until=&near="
    resp = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(resp.text, "html.parser")
    tweets = soup.find_all("div", class_="timeline-item")
    results = []
    for tweet in tweets[:50]:
        user = tweet.find("a", class_="username")
        content = tweet.find("div", class_="tweet-content media-body")
        time = tweet.find("span", class_="tweet-date")
        if user and content and time:
            results.append({
                "platform": "X",
                "user": user.text.strip(),
                "text": content.text.strip(),
                "timestamp": time.text.strip(),
                "link": "https://nitter.net" + time.find("a")["href"]
            })
    return results

# Scrape Telegram
def scrape_telegram(keyword, api_id, api_hash):
    print("[+] Scraping Telegram...")
    results = []
    client = TelegramClient("session", api_id, api_hash)
    client.start()
    messages = client(SearchGlobal(q=keyword, limit=50)).messages
    for msg in messages:
        results.append({
            "platform": "Telegram",
            "user": str(msg.sender_id),
            "text": msg.message,
            "timestamp": msg.date.isoformat(),
            "link": ""
        })
    client.disconnect()
    return results

# Main
def main():
    keyword = input("Masukkan keyword: ")
    api_id = int(input("Telegram API ID: "))
    api_hash = getpass("Telegram API Hash: ")

    all_data = []
    all_data += scrape_reddit(keyword)
    all_data += scrape_x(keyword)
    all_data += scrape_telegram(keyword, api_id, api_hash)

    save_results(all_data)
    print(f"\n[+] Selesai. Hasil disimpan di:\n- {JSON_PATH}\n- {CSV_PATH}")

main()
