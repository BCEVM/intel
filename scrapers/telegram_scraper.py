# scrapers/telegram_scraper.py
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import SearchGlobalRequest
import asyncio

api_id = YOUR_API_ID
api_hash = 'YOUR_API_HASH'

async def scrape_telegram(keyword, limit=30):
    results = []
    async with TelegramClient('session_name', api_id, api_hash) as client:
        messages = await client(SearchGlobalRequest(
            q=keyword,
            limit=limit,
            offset_date=None,
            offset_id=0,
            offset_peer=None,
            filter=None,
            min_date=None,
            max_date=None,
            hash=0
        ))
        for msg in messages.messages:
            if hasattr(msg, 'message'):
                results.append({
                    "platform": "Telegram",
                    "user": msg.sender_id,
                    "text": msg.message,
                    "timestamp": str(msg.date),
                    "link": "N/A"
                })
    return results
