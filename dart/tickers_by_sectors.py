import pandas as pd
import pymysql
import os

from dotenv import load_dotenv

data = pd.read_excel("상장법인목록.xlsx")

load_dotenv()

db = pymysql.connect(
    host=os.environ.get("DB_HOST"),
    user=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASSWORD"),
    db=os.environ.get("DB_NAME"),
    charset="utf8",
)

curs = db.cursor()

sql = "INSERT IGNORE INTO sectors_by_tickers(회사명, 종목코드, 업종) VALUES (%s, %s, %s)"

for idx in range(len(data)):
    curs.execute(sql, tuple(data.values[idx]))

db.commit()
db.close()
