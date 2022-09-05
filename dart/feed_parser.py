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
        contents = [w.strip().replace("\t", "").replace("\n", "") for w in contents]

        new_contents = [content for content in contents if content not in old_contents]

        return [new_contents]


# 새로운 공시 정보 추출
def real_time_info():

    # 함수 내에서 처리된 리스트를 함수 외부에서 참조하기 위함
    global old_contents

    # 위에서 정의했던 함수 실행
    new_contents = get_new_contents(old_contents)

    if new_contents:
        for content in new_contents:
            print(content)

    # 없으면 패스
    else:
        pass

    # 기존 링크를 계속 축적하기 위함
    old_contents += new_contents.copy()

    load_dotenv()

    db = pymysql.connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        db=os.environ.get("DB_NAME"),
        charset="utf8",
    )

    curs = db.cursor()

    # curs.execute("DROP TABLE IF EXISTS today_notice")

    # curs.execute(
    #     "CREATE TABLE today_notice (id INT, company VARCHAR(100), report_head VARCHAR(100), date DATE, url VARCHAR(2048))"
    # )
    i = 1

    for item in new_contents:
        curs.execute(
            f'INSERT INTO today_notice VALUES({i},"{item[0]}","{item[1]}","{item[2]}","{item[3]}")'
        )
        i += 1

    db.commit()
    db.close()


# 실제 프로그램 구동
if __name__ == "__main__":  # 프로그램의 시작점일 때만 아래 코드 실행

    # 기존에 보냈던 링크를 담아둘 리스트 만들기
    old_contents = []

    # 주기적 실행과 관련된 코드 (hours는 시, minutes는 분, seconds는 초)
    job = schedule.every(30).seconds.do(real_time_info)

    while True:

        schedule.run_pending()
        time.sleep(1)

