from datetime import datetime, timedelta
from pykrx import stock
import pandas as pd


def date_range(start, end):
    start = datetime.strptime(start, "%Y%m%d")
    end = datetime.strptime(end, "%Y%m%d")
    dates = [
        (start + timedelta(days=i)).strftime("%Y%m%d")
        for i in range((end - start).days + 1)
    ]
    dates = [stock.get_nearest_business_day_in_a_week(d) for d in dates]
    inv_dates = []
    for d in dates:
        if d not in inv_dates and (datetime.strptime(d, "%Y%m%d") - start).days >= 0:
            inv_dates.append(d)
    return inv_dates

