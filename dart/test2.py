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

notice_url = "https://dart.fss.or.kr/dsac001/mainAll.do"
baseURL = "https://dart.fss.or.kr"

# 새로운 공시 정보를 받아오는 함수
def get_new_contents(notice_url):
    response = requests.get(notice_url)
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
        # with open("today_notice.csv", "w", encoding="utf-8-sig", newline="") as f:
        #     writer = csv.writer(f)
        #     writer.writerow(contents)

        return contents
    
while True:
    dart_contents = get_new_contents(notice_url)

    with open("today_notice.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            old_contents = row

    new_contents = []

    for new in dart_contents:
        if new not in old_contents:
            new_contents.append(new)
        else:
            pass

    for content in new_contents:
        print("새로운 content", content)
        new_contents = get_new_contents(notice_url)
        print(new_contents)
        # with open("today_notice.csv", "a", encoding="utf-8-sig", newline="") as f:
        #     writer = csv.writer(f)
        #     writer.writerow(f)
        # print("새로운 리스트 추가")
    time.sleep(20)
