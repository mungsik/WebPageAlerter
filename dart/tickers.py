import pandas as pd
import glob
import os
import pymysql

"""
< --------- excel to csv 파일 변환 ---------->

xlsx = pd.read_excel("코스닥시장_티커.xlsx")
xlsx.to_csv("코스닥시장_티커.csv")
"""


"""
< --------- csv 파일 합치기 ---------->

# csv 파일들이 있는 디렉토리 위치
# r은 raw string으로 문자 그대로 받아들여달라고 요청
input_file = r"C:\Users\user\OneDrive\바탕 화면\PythonWorkspace"

# 병합하고 저장하려는 파일명
output_file = r"C:\Users\user\OneDrive\바탕 화면\PythonWorkspace\all_tickers.csv"

# glob 함수로 티커_ 로 시작하는 파일들을 모음
allFile_list = glob.glob(os.path.join(input_file, "티커_*"))
print(allFile_list)

datas = []
for file in allFile_list:
    df = pd.read_csv(file)  # for 구문으로 csv 파일들을 읽어들임
    datas.append(df)  # 빈 리스트에 읽어들인 내용 추가

# concat 함수를 이용해서 리스트의 내용을 병합
# axis = 0은 수직으로 병합함. axis = 1은 수평. ignore_index = True 는
# 인덱스 값이 기존 순서를 무시하고 순서대로 정렬되도록 함
combine_datas = pd.concat(datas, axis=0, ignore_index=True)

# to_csv 함수로 저장한다. 인덱스를 빼려면 False 로 설정
combine_datas.to_csv(output_file, index=False)
"""


# <-------------->
# MySQL로 데이터 옮기기
# <-------------->


tickers = pd.read_csv("all_tickers.csv")
tickers = tickers.drop("0", axis=1)

print(tickers.head(5))
tickers = tickers.where((pd.notnull(tickers)), None)

db = pymysql.connect(
    host=os.environ.get("DB_HOST"),
    user=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASSWORD"),
    db=os.environ.get("DB_NAME"),
    charset="utf8",
)

curs = db.cursor()

sql = "INSERT IGNORE INTO tickers(company, tickers) VALUES (%s, %s)"

for idx in range(len(tickers)):
    curs.execute(sql, tuple(tickers.values[idx]))

db.commit()
db.close()
