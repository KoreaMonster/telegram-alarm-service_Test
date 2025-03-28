#텔레그램 채널에서 메시지를 스크래핑하고 키워드를 검색하는 기능

from telegram import Bot
from telegram.error import TelegramError
import time
import asyncio

from config import TELEGRAM_BOT_TOKEN

bot = Bot(token=TELEGRAM_BOT_TOKEN)

async def search_channels_by_keyword (bot, keyword):                  #키워드를 포한하는 메세지 검색
    try:
        updates = await bot.get_updates()                               #비동기 -> 작업이 끝날 떄까지 기다림
        matching_messages = []

        for update in updates:
            # 메시지가 있고, 메시지 텍스트가 키워드를 포함하는 경우
            if update.message and keyword.lower() in update.message.text.lower():
                matching_messages.append(update.message.text)  # 메시지 추가

        print(matching_messages)

        return matching_messages

    except TelegramError as e:
        print(f"텔레그램 API 오류: {e}")

        return []