# 메인 프로그램 파일
import os
from scheduler import schedule_keyword_search


def main():
    print('=' * 50)
    print("🔔 Telegram Keyword Alert Service 시작")

    while True:
        keyword = input("📌 검색할 키워드를 입력하세요: ").strip()

        if keyword:
            break
        else:
            print("키워드는 필수입니다.")

    while True:
        target_time_str = input("⏰ 실행 시간을 입력하세요 (기본값: 09:00): ").strip()

        if target_time_str:
            break
        else:
            target_time_str = "09:00"

    os.system('cls')
    #Linux
    #os.system('clear')
    #print(f"-- 설정값 -- ")
    print(f"📌 키워드: '{keyword}'")
    print(f"⏰ 실행 시간: 매일 {target_time_str}")
    print("=" * 50)

    schedule_keyword_search(keyword, target_time_str)


if __name__ == "__main__":
    main()