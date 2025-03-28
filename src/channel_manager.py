# 텔레그램 채널을 검색하여 매일 자동으로 검색하거나, 사용자가 수동으로 채널을 추가할 수 있는 기능을 구현합니다.

import json
from telegram import Bot
from telegram.error import TelegramError

channels = []  # 채널 목록을 저장하는 리스트 -> 추후 DB로 확장


def load_channels(file= 'channels.json'):      # 채널 목록을 파일에서 불러오기
    try:
        with open(file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_channels(file= "channels.json"):      # 채널을 파일에 저장하기
    with open(file, 'w') as f:
        json.dump(channels, f)


def add_channels(channel_id: str):              #채널을 리스트에 추가하기
    channel_exists = False

    for i in range (len(channels)):
        if channels[i] == channel_id:
            channel_exists = True
            break
    if channel_exists == False:
        channels.append(channel_id)
        save_channels()

        print(f"채널 {channel_id}가 추가되었습니다.")
    else:
        print(f"채널 {channel_id}는 이미 존재합니다.")


def remove_channel(channel_id: str):            #리스트에 있는 채널을 삭제하기
    channel_exists = False

    for i in range (len(channels)):
        if channels[i] == channel_id:
            channel_exists = True
            break

    if channel_exists == True:
        channels.remove(channel_id)
        save_channels()

        print(f"채널 {channel_id}가 삭제되었습니다.")
    else:
        print(f"채널 {channel_id}가 존재하지 않습니다")


def print_channels():                           # 리스트에 있는 채널을 전부 출력하기
    print(f"등록된 Channels: ")

    if channels:
        for i in range (len(channels)):
            print(f"{channels[i]}")
    else:
        print("등록된 Channel이 없습니다.")

#
# def search_channels_by_keyword(bot: Bot, keyword: str):  #각 채널 내에서 키워드를 검색
#     match_messages = []
#
#     for channel_id in channels:
#         updates = bot.getUpdates()  #updates 모든 업데이트
#
#         for update in updates:
#             if update.message and keyword in update.message.text:
#                 match_messages.append(update.message.text)
#
#     return match_messages

async def check_bot_access(bot: Bot):
    channels = load_channels()

    if not channels:
        print("등록된 채널이 없습니다.")
        return

    print("🔍 채널 접근 가능 여부 확인 중...\n")

    for channel in channels:
        try:
            chat = await bot.get_chat(channel)  # 봇이 채널 정보 가져올 수 있는지 테스트
            print(f"접근 가능: {channel} (title: {chat.title})")
        except TelegramError as e:
            print(f"접근 실패: {channel} | 이유: {e.message}")