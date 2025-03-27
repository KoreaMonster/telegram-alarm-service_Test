#스케줄링 기능을 담당합니다. 예를 들어, 매일 특정 시간에 스크래핑 작업을 실행

from datetime import datetime
import time
from time import sleep

from telegram import Bot
from config import TELEGRAM_BOT_TOKEN
from channel_manager import search_channels_by_keyword


bot = Bot(token=TELEGRAM_BOT_TOKEN)

def matching_job(keyword: str):              #키워드로 채널을 검색
    print(f"채널 검색 시작 | Keyword: {keyword}")

    matching = search_channels_by_keyword(bot, keyword)

    if matching:
        print(f"키워드가 포함된 메세지를 찾았습니다.")
        for match in matching:
            print(match)

            #알림을 보내는 함수
    else:
        print(f"키워드가 포함된 메세지가 없습니다.")


def search_channels(keyword: str, target_time_str: str):          #정해둔 시간에 채널 검색을 진행
    target_time = datetime.strptime(target_time_str, "%H:%M") #.time() 오류 있으면 추가해보기(date와 datetime비교의 문제

    while True:
        now = datetime.datetime.now().time()

        if target_time == now:
            matching_job(keyword)

            time.sleep(86400)    #하루에 한번만 실행 가능 -> 추후 수정해서 여러 시간 선택 가능으로
        else:
            time.sleep(15)      #초반 길찾기(시간)
