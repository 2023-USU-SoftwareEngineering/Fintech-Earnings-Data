import datetime
import requests
import math
from datetime import date, timedelta, datetime
import pandas as pd
from IPython.display import display
from StockPricePull import StockData
from sql_functions import add_history


temp = [
    [datetime.today(), "Google", 1.0, 2.0, 3.0, 4.0, "transcript"],
    [datetime.today(), "Apple", 1.0, 2.0, 3.0, 4.0, "transcript"],
    [datetime.today(), "Microsoft", 1.0, 2.0, 3.0, 4.0, "transcript"],
    [datetime.today(), "AMD", 1.0, 2.0, 3.0, 4.0, "transcript"],
    [datetime.today(), "Intel", 1.0, 2.0, 3.0, 4.0, "transcript"],
]

for item in temp:
    add_history(item[0], item[1], item[2], item[3], item[4], item[5], item[6])