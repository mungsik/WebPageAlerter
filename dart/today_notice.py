import requests
import schedule
import time
import csv
import pandas as pd
import os
import pymysql

from dotenv import load_dotenv
from calendar import c
from bs4 import BeautifulSoup


"""
<------------------>
    dart 분석
<------------------>
"""

url = "https://dart.fss.or.kr/dsac001/mainAll.do"
baseURL = "https://dart.fss.or.kr"

# 새로운 공시 정보를 받아오는 함수
def get_new_contents(old_contents=[]):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    data_rows = (
        soup.find("table", attrs={"class": "tbList"}).find("tbody").find_all("tr")
    )

    notices = []

    for row in data_rows:
        columns = row.find_all("td")
        # 의미 없는 데이터 skip
        # 칸 나누기용 공백 같은것
        if len(columns) <= 1:
            continue

        contents = [
            columns[1].get_text()[3:],
            columns[2].get_text(),
            columns[4].get_text(),
            baseURL + columns[2].find("a")["href"],
        ]

        # 요소에서 컨텐츠만 추출해서 리스트로 저장
        contents = [w.strip().replace("\t", "").replace("\n", "") for w in contents]

        # 기존의 컨텐츠와 신규 컨텐츠를 비교해서 새로운 컨텐츠만 저장
        new_contents = [content for content in contents if content not in old_contents]

        notices.append(new_contents)

        return notices


# 새로운 공시 정보 추출
def real_time_info():

    # 함수 내에서 처리된 리스트를 함수 외부에서 참조하기 위함
    global old_contents

    # 위에서 정의했던 함수 실행
    new_contents = get_new_contents(old_contents)

    if new_contents:
        for content in new_contents:
            print("new", content)
    # 없으면 패스
    else:
        pass

    # 기존 링크를 계속 축적하기 위함
    old_contents += new_contents.copy()
    print("old", old_contents)


# 실제 프로그램 구동
if __name__ == "__main__":  # 프로그램의 시작점일 때만 아래 코드 실행

    # 기존에 보냈던 컨텐츠를 담아둘 리스트 만들기
    old_contents = []

    # 주기적 실행과 관련된 코드 (hours는 시, minutes는 분, seconds는 초)
    job = schedule.every(10).seconds.do(real_time_info)

    while True:

        schedule.run_pending()
        time.sleep(1)

