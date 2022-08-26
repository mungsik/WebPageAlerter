import random
import pandas as pd
import csv
import pymysql
import time
import requests
import os

from dotenv import load_dotenv
from selenium import webdriver
from lib2to3.pgen2 import driver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# connection 에러 처리
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)

# 브라우저 최대화
browser.maximize_window()

# URL 및 기다리는 간격
baseURL = "https://dart.fss.or.kr/dsab007/main.do?option=corp"
interval = 3

"""
<------------------>
    csv파일로 변환
<------------------>
"""

fileName = "supply_contract_conclusion.csv"
f = open(fileName, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)


"""
<------------------>
    dart 분석
<------------------>
"""


def dartData(url):

    """
    1. 셀레니움으로 공급계약 페이지 불러오기
    """

    browser.get(url)
    time.sleep(interval)
    browser.find_element_by_xpath('//*[@id="option"]/option[3]').click()
    time.sleep(interval)
    browser.find_element_by_id("reportName").send_keys("공급계약체결")
    browser.find_element_by_id("btnReport").click()

    # 공급계약 보고서 상세 검색
    # 모달창 기다리기
    maxInterval = 5
    WebDriverWait(browser, maxInterval).until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='reportContents']/div/div[2]/table/tbody")
        )
    )
    for i in range(1, 5):
        xpath_tr = '//*[@id="reportContents"]/div/div[2]/table/tbody/tr[{}]/td[1]/input'.format(
            i
        )
        browser.find_element_by_xpath(xpath_tr).click()
    browser.find_element_by_xpath(
        '//*[@id="winFindReport"]/div[2]/div[2]/div[3]/a[1]'
    ).click()
    time.sleep(interval + random.uniform(0, 1))

    browser.find_element_by_xpath('//*[@id="date5"]').click()
    time.sleep(interval + random.uniform(0, 1))

    browser.find_element_by_xpath(
        "//*[@id='searchForm']/div[1]/div/ul/li/div[3]/a"
    ).click()
    time.sleep(interval + random.uniform(0, 1))

    # 조회건수 100으로 증가시키기
    browser.find_element_by_xpath("//*[@id='maxResultsCb']/option[4]").click()
    browser.find_element_by_xpath("//*[@id='searchForm']/div[2]/div[2]/a[1]").click()
    time.sleep(maxInterval)

    for num in range(3, 13):
        url_n = '//*[@id="psWrap"]/div[2]/ul/li[{}]/a'.format(num)
        browser.find_element_by_xpath(url_n).click()
        print(f"페이지 {num - 2}번째 page 접속 중")
        time.sleep(maxInterval)
        soup = BeautifulSoup(browser.page_source, "lxml")
        data_rows = (
            soup.find("table", attrs={"class": "tbList"}).find("tbody").find_all("tr")
        )
        for row in data_rows:
            columns = row.find_all("td")

            # 의미 없는 데이터 skip
            if len(columns) <= 1:
                continue

            # 기재정정 제외
            val = "기재정정" in columns[2].get_text()
            if val:
                continue
            else:
                col_parsed = [
                    columns[1].get_text()[3:],
                    columns[2].get_text(),
                    columns[3].get_text(),
                    columns[4].get_text(),
                    columns[5].get_text(),
                ]

            # 불필요한 공백 제거
            col_parsed = [
                w.strip().replace("\t", "").replace("\n", "") for w in col_parsed
            ]
            print(col_parsed)
            writer.writerow(col_parsed)
    browser.find_element_by_xpath('//*[@id="psWrap"]/div[2]/ul/li[13]/a').click()
    print("페이지넘김")
    time.sleep(maxInterval)

    for num in range(3, 13):
        url_n = '//*[@id="psWrap"]/div[2]/ul/li[{}]/a'.format(num)
        browser.find_element_by_xpath(url_n).click()
        print(f"second 페이지 {num - 2}번째 page 접속 중")
        time.sleep(maxInterval)
        soup = BeautifulSoup(browser.page_source, "lxml")
        data_rows = (
            soup.find("table", attrs={"class": "tbList"}).find("tbody").find_all("tr")
        )
        for row in data_rows:
            columns = row.find_all("td")

            # 의미 없는 데이터 skip
            if len(columns) <= 1:
                continue

            # 기재정정 제외
            val = "기재정정" in columns[2].get_text()
            if val:
                continue
            else:
                col_parsed = [
                    columns[1].get_text()[3:],
                    columns[2].get_text(),
                    columns[3].get_text(),
                    columns[4].get_text(),
                    columns[5].get_text(),
                ]

            # 불필요한 공백 제거
            col_parsed = [
                w.strip().replace("\t", "").replace("\n", "") for w in col_parsed
            ]
            print(col_parsed)
            writer.writerow(col_parsed)
    browser.find_element_by_xpath('//*[@id="psWrap"]/div[2]/ul/li[13]/a').click()
    print("두 번째 페이지넘김")
    time.sleep(maxInterval)

    for num in range(3, 13):
        url_n = '//*[@id="psWrap"]/div[2]/ul/li[{}]/a'.format(num)
        browser.find_element_by_xpath(url_n).click()
        print(f"third 페이지 {num - 2}번째 page 접속 중")
        time.sleep(maxInterval)
        soup = BeautifulSoup(browser.page_source, "lxml")
        data_rows = (
            soup.find("table", attrs={"class": "tbList"}).find("tbody").find_all("tr")
        )
        for row in data_rows:
            columns = row.find_all("td")

            # 의미 없는 데이터 skip
            if len(columns) <= 1:
                continue

            # 기재정정 제외
            val = "기재정정" in columns[2].get_text()
            if val:
                continue
            else:
                col_parsed = [
                    columns[1].get_text()[3:],
                    columns[2].get_text(),
                    columns[3].get_text(),
                    columns[4].get_text(),
                    columns[5].get_text(),
                ]

            # 불필요한 공백 제거
            col_parsed = [
                w.strip().replace("\t", "").replace("\n", "") for w in col_parsed
            ]
            print(col_parsed)
            writer.writerow(col_parsed)
    browser.find_element_by_xpath('//*[@id="psWrap"]/div[2]/ul/li[13]/a').click()
    print("세 번째 페이지넘김")
    time.sleep(maxInterval)

    for num in range(3, 13):
        url_n = '//*[@id="psWrap"]/div[2]/ul/li[{}]/a'.format(num)
        browser.find_element_by_xpath(url_n).click()
        print(f"forth 페이지 {num - 2}번째 page 접속 중")
        time.sleep(maxInterval)
        soup = BeautifulSoup(browser.page_source, "lxml")
        data_rows = (
            soup.find("table", attrs={"class": "tbList"}).find("tbody").find_all("tr")
        )
        for row in data_rows:
            columns = row.find_all("td")

            # 의미 없는 데이터 skip
            if len(columns) <= 1:
                continue

            # 기재정정 제외
            val = "기재정정" in columns[2].get_text()
            if val:
                continue
            else:
                col_parsed = [
                    columns[1].get_text()[3:],
                    columns[2].get_text(),
                    columns[3].get_text(),
                    columns[4].get_text(),
                    columns[5].get_text(),
                ]

            # 불필요한 공백 제거
            col_parsed = [
                w.strip().replace("\t", "").replace("\n", "") for w in col_parsed
            ]
            print(col_parsed)
            writer.writerow(col_parsed)
    browser.find_element_by_xpath('//*[@id="psWrap"]/div[2]/ul/li[13]/a').click()
    print("네 번째 페이지넘김")
    time.sleep(maxInterval)

    for num in range(3, 13):
        url_n = '//*[@id="psWrap"]/div[2]/ul/li[{}]/a'.format(num)
        browser.find_element_by_xpath(url_n).click()
        print(f"fifth 페이지 {num - 2}번째 page 접속 중")
        time.sleep(maxInterval)
        soup = BeautifulSoup(browser.page_source, "lxml")
        data_rows = (
            soup.find("table", attrs={"class": "tbList"}).find("tbody").find_all("tr")
        )
        for row in data_rows:
            columns = row.find_all("td")

            # 의미 없는 데이터 skip
            if len(columns) <= 1:
                continue

            # 기재정정 제외
            val = "기재정정" in columns[2].get_text()
            if val:
                continue
            else:
                col_parsed = [
                    columns[1].get_text()[3:],
                    columns[2].get_text(),
                    columns[3].get_text(),
                    columns[4].get_text(),
                    columns[5].get_text(),
                ]

            # 불필요한 공백 제거
            col_parsed = [
                w.strip().replace("\t", "").replace("\n", "") for w in col_parsed
            ]
            print(col_parsed)
            writer.writerow(col_parsed)
    browser.find_element_by_xpath('//*[@id="psWrap"]/div[2]/ul/li[13]/a').click()
    print("다섯 번째 페이지넘김")
    time.sleep(maxInterval)

    for num in range(3, 13):
        url_n = '//*[@id="psWrap"]/div[2]/ul/li[{}]/a'.format(num)
        browser.find_element_by_xpath(url_n).click()
        print(f"sixth 페이지 {num - 2}번째 page 접속 중")
        time.sleep(maxInterval)
        soup = BeautifulSoup(browser.page_source, "lxml")
        data_rows = (
            soup.find("table", attrs={"class": "tbList"}).find("tbody").find_all("tr")
        )
        for row in data_rows:
            columns = row.find_all("td")

            # 의미 없는 데이터 skip
            if len(columns) <= 1:
                continue

            # 기재정정 제외
            val = "기재정정" in columns[2].get_text()
            if val:
                continue
            else:
                col_parsed = [
                    columns[1].get_text()[3:],
                    columns[2].get_text(),
                    columns[3].get_text(),
                    columns[4].get_text(),
                    columns[5].get_text(),
                ]

            # 불필요한 공백 제거
            col_parsed = [
                w.strip().replace("\t", "").replace("\n", "") for w in col_parsed
            ]
            print(col_parsed)
            writer.writerow(col_parsed)
    browser.find_element_by_xpath('//*[@id="psWrap"]/div[2]/ul/li[13]/a').click()
    print("여섯 번째 페이지넘김")
    time.sleep(maxInterval)

    for num in range(3, 13):
        url_n = '//*[@id="psWrap"]/div[2]/ul/li[{}]/a'.format(num)
        browser.find_element_by_xpath(url_n).click()
        print(f"seventh 페이지 {num - 2}번째 page 접속 중")
        time.sleep(maxInterval)
        soup = BeautifulSoup(browser.page_source, "lxml")
        data_rows = (
            soup.find("table", attrs={"class": "tbList"}).find("tbody").find_all("tr")
        )
        for row in data_rows:
            columns = row.find_all("td")

            # 의미 없는 데이터 skip
            if len(columns) <= 1:
                continue

            # 기재정정 제외
            val = "기재정정" in columns[2].get_text()
            if val:
                continue
            else:
                col_parsed = [
                    columns[1].get_text()[3:],
                    columns[2].get_text(),
                    columns[3].get_text(),
                    columns[4].get_text(),
                    columns[5].get_text(),
                ]

            # 불필요한 공백 제거
            col_parsed = [
                w.strip().replace("\t", "").replace("\n", "") for w in col_parsed
            ]
            print(col_parsed)
            writer.writerow(col_parsed)
    browser.find_element_by_xpath('//*[@id="psWrap"]/div[2]/ul/li[13]/a').click()
    print("일곱 번째 페이지넘김")
    time.sleep(maxInterval)

    for num in range(3, 5):
        url_n = '//*[@id="psWrap"]/div[2]/ul/li[{}]/a'.format(num)
        browser.find_element_by_xpath(url_n).click()
        print(f"eigth 페이지 {num - 2}번째 page 접속 중")
        time.sleep(maxInterval)
        soup = BeautifulSoup(browser.page_source, "lxml")
        data_rows = (
            soup.find("table", attrs={"class": "tbList"}).find("tbody").find_all("tr")
        )
        for row in data_rows:
            columns = row.find_all("td")

            # 의미 없는 데이터 skip
            if len(columns) <= 1:
                continue

            # 기재정정 제외
            val = "기재정정" in columns[2].get_text()
            if val:
                continue
            else:
                col_parsed = [
                    columns[1].get_text()[3:],
                    columns[2].get_text(),
                    columns[3].get_text(),
                    columns[4].get_text(),
                    columns[5].get_text(),
                ]

            # 불필요한 공백 제거
            col_parsed = [
                w.strip().replace("\t", "").replace("\n", "") for w in col_parsed
            ]
            print(col_parsed)
            writer.writerow(col_parsed)
    print("마지막 페이지")
    f.close()
    browser.close()


dartData(baseURL)

"""
<-------------->
MySQL로 데이터 옮기기
<-------------->
"""

csv_data = pd.read_csv("supply_contract_conclusion.csv")
csv_data.head(5)
csv_data = csv_data.where((pd.notnull(csv_data)), None)

load_dotenv()

db = pymysql.connect(
    host=os.environ.get("DB_HOST"),
    user=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASSWORD"),
    db=os.environ.get("DB_NAME"),
    charset="utf8",
)

curs = db.cursor()

sql = "INSERT IGNORE INTO supply_contract_conclusion(company, report_head, submission_company, reception_date, market) VALUES (%s, %s, %s, %s, %s)"

for idx in range(len(csv_data)):
    curs.execute(sql, tuple(csv_data.values[idx]))

db.commit()
db.close()
