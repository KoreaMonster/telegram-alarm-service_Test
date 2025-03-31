#텔레그램 채널에서 메시지를 스크래핑하고 키워드를 검색하는 기능
from pyexpat.errors import messages
from telegram import Bot
from telegram.error import TelegramError
import time
import asyncio

from config import TELEGRAM_BOT_TOKEN

bot = Bot(token=TELEGRAM_BOT_TOKEN)

async def search_channels_by_keyword (bot, keyword):                  #키워드를 포한하는 메세지 검색
    try:

        updates = await bot.get_updates()
        for update in updates:
            print("gma"+update.message.text)  # 각 메시지 출력


        #updates = await bot.get_updates()                               #비동기 -> 작업이 오래 걸리니까 동시 실행
        matching_messages = []

        for update in updates:
            # 확인용
            if update.message:
                print(f"[채널] {update.message.chat.username}")
                print(f"[내용] {update.message.text}")
            # 메시지가 있고, 메시지 텍스트가 키워드를 포함하는 경우
            if update.message and keyword.lower() in update.message.text.lower():
                matching_messages.append(update.message.text)  # 메시지 추가

        # print(f"search_ch_by_keyw{matching_messages}")

        return matching_messages

    except TelegramError as e:
        print(f"텔레그램 API 오류: {e}")

        return []


async def search_recent_message(bot, channel):
    try:
        messages = await bot.get_chat_history(channel, limit=10)

        for message in messages:
            print(f"channel: {channel}\nmessage: {message}")
            return [ messages]
    except Exception as e:
        print(f"Error: {e}")

        return []