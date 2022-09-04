from calendar import c
import requests
from bs4 import BeautifulSoup
import schedule
import time

url = "https://dart.fss.or.kr/dsac001/mainAll.do"
baseURL = "https://dart.fss.or.kr"

# 새로운 공시 링크를 받아오는 함수
def get_new_links(old_links=[]):

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    data_rows = (
        soup.find("table", attrs={"class": "tbList"}).find("tbody").find_all("tr")
    )

    for row in data_rows:
        columns = row.find_all("td")
        # 의미 없는 데이터 skip
        # 칸 나누기용 공백 같은것
        # if len(columns) <= 1:
        #     continue
        # col_parsed = [
        #     columns[0].get_text(),
        #     columns[1].get_text()[3:],
        #     columns[2].get_text(),
        # ]

        # # 불필요한 공백 제거
        # col_parsed = [w.strip().replace("\t", "").replace("\n", "") for w in col_parsed]
        # print(col_parsed)

        # 공시 링크 뽑아내기
        links = columns[2].find("a")["href"]
        notice_links = [baseURL + links]
        new_links = [link for link in notice_links if link not in old_links]
        return new_links


def real_time_links():
    global old_links

    new_links = get_new_links(old_links)

    if new_links:
        for link in new_links:
            print(link)
    else:
        pass

    old_links += new_links.copy()


if __name__ == "__main__":  # 프로그램의 시작점일 때만 아래 코드 실행

    old_links = []

    job = schedule.every(30).seconds.do(real_time_links)

    while True:

        schedule.run_pending()
        time.sleep(1)
