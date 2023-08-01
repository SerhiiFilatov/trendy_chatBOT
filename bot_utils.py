import aiohttp
import os


async def send_message_to_discord(message):
    data = {
        "content": message
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(os.getenv('WEBHOOK_URL1'), json=data) as response:
            if response.status == 204:
                return True
            else:
                return False

