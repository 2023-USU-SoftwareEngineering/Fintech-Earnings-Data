from datetime import datetime
from sqlite3 import Error
import sqlite3
import os


def add_history(date: datetime, company_name: str, before: float, after: float, oneMonth: float, threeMonth: float, transcript: str):
    connection = None
    try:
        connection = sqlite3.connect(os.getcwd() + "/../sqlite/db/Fintech.db")
    except Error as e:
        print(e)
    if connection:
        c = connection.cursor()
        c.execute(
            f"INSERT INTO {company_name} (date, before, after, oneMonth, threeMonth, input) VALUES ({convert_date(date)}, {before}, {after}, {oneMonth}, {threeMonth}, '{transcript}')"
        )


def convert_date(date: datetime):
    """
    Converts a datetime object to unix epoch time, for use in our database
    """
    # if not isinstance(date, datetime):
    #     date = datetime.strptime(date, '%Y.%m.%d')
    return int(date.timestamp())
