import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage

from bot_config import settings
from bot_handlers import take_message

storage: RedisStorage = RedisStorage.from_url('redis://localhost:6379/0')


async def main():

    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
    dp = Dispatcher(storage=storage)
    dp.include_router(take_message.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

