import sqlite3
from sqlite3 import Error
import sys
import os


def main():
    if len(sys.argv) == 1:
        return
    elif sys.argv[1] == "-h" or sys.argv[1] == "-help":
        print("-c: create table if not exists")
        print("-d: drop table if exists")
        print("-s: select all from")
        print("-n: names of all tables")
        print("-cp: create prediction table")
        print("-sp: select all from prediction table")
    connection = None
    try:
        connection = sqlite3.connect(os.getcwd() + "/../db/Fintech.db")
    except Error as e:
        print(e)
    if connection:
        c = connection.cursor()
        if sys.argv[1] == "-c":
            for arg in sys.argv[2:]:
                c.execute(
                    f"CREATE TABLE IF NOT EXISTS {arg} ([date] INTEGER PRIMARY KEY, [price] INTEGER, [input] TEXT);"
                )
                connection.commit()
            connection.close()
        elif sys.argv[1] == "-d":
            for arg in sys.argv[2:]:
                c.execute(
                    f"DROP TABLE IF EXISTS {arg};"
                )
                connection.commit()
            connection.close()
        elif sys.argv[1] == "-s":
            for arg in sys.argv[2:]:
                c.execute(
                    f"SELECT * FROM {arg};"
                )
                rows = c.fetchall()
                for row in rows:
                    print(row)
            connection.close()
        elif sys.argv[1] == "-n":
            c.execute(
                "SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%';"
            )
            rows = c.fetchall()
            for row in rows:
                print(row)
            connection.close()
        elif sys.argv[1] == "-cp":
            c.execute(
                "CREATE TABLE IF NOT EXISTS prediction ([name] TEXT, [prediction] INTEGER);"
            )
            connection.commit()
            connection.close()
        elif sys.argv[1] == "-sp":
            c.execute(
                "SELECT * FROM prediction;"
            )
            rows = c.fetchall()
            for row in rows:
                print(row)
            connection.close()


if __name__ == '__main__':
    main()
