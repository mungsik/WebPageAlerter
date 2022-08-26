import csv
import random
import time
import FinanceDataReader as fdr
import pandas as pd
import pymysql
import business_day
import os

from dotenv import load_dotenv
from pykrx import stock
from dateutil.relativedelta import relativedelta
from sqlalchemy import create_engine

interval = 1


def get_korean_stock_ohlcv():

    # DB와 연결 및 데이터 불러오기
    pymysql.install_as_MySQLdb()
    load_dotenv()

    table_name = "stocks"
    db_connection_path = "mysql+mysqldb://{user}:{password}@localhost/{db}".format(
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        db=os.environ.get("DB_NAME"),
        encoding="utf8",
    )
    db_connection = create_engine(db_connection_path)

    conn = db_connection.connect()

    # 20220819
    business_day_list = business_day.date_range("20220601", "20220819")
    for date in business_day_list:
        print(date)
        datas = stock.get_market_ohlcv(date, market="ALL")
        time.sleep(interval + random.uniform(0, 1))

        # 인덱스 칼럼으로 바꾸기
        datas["ticker"] = datas.index

        # 날짜 추가
        df = pd.DataFrame(datas)
        modify_date = date[0:4] + "-" + date[4:6] + "-" + date[6:8]
        df = df.assign(registration_date=modify_date)

        # 데이터 적재
        df.to_sql(name=table_name, con=db_connection, if_exists="append", index=False)

        # 저장된 데이터 확인

        format_datas = pd.read_sql_table("stocks", con=conn)
        # print(format_datas)


get_korean_stock_ohlcv()

