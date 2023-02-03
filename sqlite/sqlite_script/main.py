import sqlite3
from sqlite3 import Error
import sys


def main():
    connection = None
    try:
        connection = sqlite3.connect(r"~/Fintech-Earnings-Data/sqlite/db/Fintech.db")
    except Error as e:
        print(e)
    finally:
        if connection:
            c = connection.cursor()
            for arg in sys.argv:
                c.execute(
                    "CREATE TABLE IF NOT EXISTS " + arg + " ([date] TEXT PRIMARY KEY, [price] INTEGER, [input] TEXT)")
                connection.commit()
            connection.close()
    return


if __name__ == '__main__':
    main()
