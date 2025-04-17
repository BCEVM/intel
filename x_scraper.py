import snscrape.modules.twitter as sntwitter

def scrape_x(keyword, limit=50):
    results = []
    for tweet in sntwitter.TwitterSearchScraper(f'{keyword}').get_items():
        if len(results) >= limit:
            break
        results.append({
            "platform": "X",
            "user": tweet.user.username,
            "text": tweet.content,
            "timestamp": str(tweet.date),
            "link": f"https://x.com/{tweet.user.username}/status/{tweet.id}"
        })
    return results