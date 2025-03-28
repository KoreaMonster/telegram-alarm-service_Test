#스케줄링 기능을 담당합니다. 예를 들어, 매일 특정 시간에 스크래핑 작업을 실행

from datetime import datetime
import time
import schedule
import asyncio
from time import sleep

from telegram import Bot
from config import TELEGRAM_BOT_TOKEN
from scraper import search_channels_by_keyword
from src.notifier import write_email

bot = Bot(token=TELEGRAM_BOT_TOKEN)

def run_keyword_search(keyword: str):              #키워드로 채널을 검색
    print(f"채널 검색 시작 | Keyword: {keyword}")

    matching = asyncio.run(search_channels_by_keyword(bot, keyword))

    if matching:
        print(f"키워드가 포함된 메세지를 찾았습니다.")

        for match in matching:
            print(match)

            #알림을 보내는 함수
            write_email(keyword, match)
    else:
        print(f"키워드가 포함된 메세지가 없습니다.")


def schedule_keyword_search(keyword: str, target_time_str: str):          #정해둔 시간에 채널 검색을 진행
    # target_time = datetime.strptime(target_time_str, "%H:%M") #.time() 오류 있으면 추가해보기(date와 datetime 비교의 문제
    #
    # print(target_time)
    #
    # while True:
    #     # now = datetime.now().time()
    #     # print(now)
    #
    #     schedule.every().day.at(target_time_str).do(run_keyword_search(keyword))
    #     #
    #     #     time.sleep(86400)    #하루에 한번만 실행 가능 -> 추후 수정해서 여러 시간 선택 가능으로
    #     # else:
    #     time.sleep(15)      #초반 길찾기(시간)
    schedule.every().day.at(target_time_str).do(run_keyword_search, keyword)

    print(f"⏰ 매일 {target_time_str}에 키워드 '{keyword}'로 채널을 검색합니다.")

    # 스케줄 반복 감시 루프
    while True:
        schedule.run_pending()
        time.sleep(30)