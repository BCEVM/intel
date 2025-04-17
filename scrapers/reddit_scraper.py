# scrapers/reddit_scraper.py
import requests

def scrape_reddit(keyword, limit=50):
    url = f"https://api.pushshift.io/reddit/search/comment/?q={keyword}&size={limit}"
    res = requests.get(url)
    data = res.json().get("data", [])
    results = []
    for d in data:
        results.append({
            "platform": "Reddit",
            "user": d.get("author"),
            "text": d.get("body"),
            "timestamp": d.get("created_utc"),
            "link": f"https://reddit.com{d.get('permalink', '')}"
        })
    return results
