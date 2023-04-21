from datetime import datetime
from sqlite3 import Error
import sqlite3
import os
import csv


def add_history(date: datetime, company_name: str, before: float, after: float, oneMonth: float, threeMonth: float,
                transcript: str):
    transcript = transcript.replace("'", "''")
    connection = None
    try:
        connection = sqlite3.connect(os.getcwd() + "/../sqlite/db/Fintech.db")
    except Error as e:
        print(e)
    if connection:
        c = connection.cursor()
        c.execute(
            f"INSERT INTO {company_name} (date, before, after, oneMonth, threeMonth, input) VALUES ({convert_date(date)}, {before}, {after}, {oneMonth}, {threeMonth}, '{transcript}');"
        )
        connection.commit()
        connection.close()


def convert_date(date: datetime):
    """
    Converts a datetime object to unix epoch time, for use in our database
    """
    # if not isinstance(date, datetime):
    #     date = datetime.strptime(date, '%Y.%m.%d')
    return int(date.timestamp())


def output_to_csv():
    connection = None
    try:
        connection = sqlite3.connect(os.getcwd() + "/../sqlite/db/Fintech.db")
    except Error as e:
        print(e)
    if connection:
        c = connection.cursor()
        result = list()
        for name in get_companies_help():
            c.execute(
                f"SELECT * FROM {name[0]};"
            )
            rows = c.fetchall()
            for row in rows:
                temp = (name[0], row[0], row[1], row[2], row[3], row[4], row[5].replace(',', ''))
                result.append(temp)
        with open(os.getcwd() + "/../sqlite/db/Fintech.csv", 'w', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in result:
                csvwriter.writerow(row)

        connection.close()


def get_companies_help():
    return_array = []
    connection = None
    try:
        connection = sqlite3.connect(os.getcwd() + "/../sqlite/db/Fintech.db")
    except Error as e:
        print(e)
    if connection:
        c = connection.cursor()
        c.execute(
            "SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%' AND name !='prediction_short' AND name !='prediction_medium' AND name !='prediction_long';"
        )
        rows = c.fetchall()
        for row in rows:
            return_array.append(row)
        connection.close()
    return return_array


def add_prediction_short(company_name: str, prediction: float):
    connection = None
    try:
        connection = sqlite3.connect(os.getcwd() + "/../sqlite/db/Fintech.db")
    except Error as e:
        print(e)
    if connection:
        c = connection.cursor()
        c.execute(
            f"INSERT INTO prediction_short (name, prediction) VALUES ('{company_name}',{prediction});"
        )
        connection.commit()
        connection.close()


def add_prediction_medium(company_name: str, prediction: float):
    connection = None
    try:
        connection = sqlite3.connect(os.getcwd() + "/../sqlite/db/Fintech.db")
    except Error as e:
        print(e)
    if connection:
        c = connection.cursor()
        c.execute(
            f"INSERT INTO prediction_medium (name, prediction) VALUES ('{company_name}',{prediction});"
        )
        connection.commit()
        connection.close()


def add_prediction_long(company_name: str, prediction: float):
    connection = None
    try:
        connection = sqlite3.connect(os.getcwd() + "/../sqlite/db/Fintech.db")
    except Error as e:
        print(e)
    if connection:
        c = connection.cursor()
        c.execute(
            f"INSERT INTO prediction_long (name, prediction) VALUES ('{company_name}',{prediction});"
        )
        connection.commit()
        connection.close()

