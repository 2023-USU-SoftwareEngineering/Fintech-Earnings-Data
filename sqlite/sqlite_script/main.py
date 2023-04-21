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
        print("-cs: create short prediction table")
        print("-cm: create medium prediction table")
        print("-cl: create long prediction table")
        print("-ss: select all from short prediction table")
        print("-sm: select all from medium prediction table")
        print("-sl: select all from long prediction table")
        print('-ct: get count of table')
        print("-dd: clean table of dummy data")

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
                    f"CREATE TABLE IF NOT EXISTS {arg} ([date] INTEGER PRIMARY KEY, [before] REAL, [after] REAL, [oneMonth] REAL, [threeMonth] REAL, [input] TEXT);"
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
        elif sys.argv[1] == "-ct":
            total = 0
            for arg in sys.argv[2:]:
                c.execute(
                    f"SELECT * FROM {arg};"
                )
                for _ in c.fetchall():
                    total += 1
            print(total)
            connection.close()
        elif sys.argv[1] == "-n":
            c.execute(
                "SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%' AND name != 'prediction_short' AND name != 'prediction_medium' AND name != 'prediction_long';"
            )
            rows = c.fetchall()
            for row in rows:
                print(row)
            connection.close()
        elif sys.argv[1] == "-cs":
            c.execute(
                "CREATE TABLE IF NOT EXISTS prediction_short ([name] TEXT PRIMARY KEY, [prediction] REAL);"
            )
            connection.commit()
            connection.close()
        elif sys.argv[1] == "-cm":
            c.execute(
                "CREATE TABLE IF NOT EXISTS prediction_medium ([name] TEXT PRIMARY KEY, [prediction] REAL);"
            )
            connection.commit()
            connection.close()
        elif sys.argv[1] == "-cl":
            c.execute(
                "CREATE TABLE IF NOT EXISTS prediction_long ([name] TEXT PRIMARY KEY, [prediction] REAL);"
            )
            connection.commit()
            connection.close()
        elif sys.argv[1] == "-ss":
            c.execute(
                "SELECT * FROM prediction_short;"
            )
            rows = c.fetchall()
            for row in rows:
                print(row)
            connection.close()
        elif sys.argv[1] == "-sm":
            c.execute(
                "SELECT * FROM prediction_medium;"
            )
            rows = c.fetchall()
            for row in rows:
                print(row)
            connection.close()
        elif sys.argv[1] == "-sl":
            c.execute(
                "SELECT * FROM prediction_long;"
            )
            rows = c.fetchall()
            for row in rows:
                print(row)
            connection.close()
        elif sys.argv[1] == "-dd":
            c.execute(
                "SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%' AND name != 'prediction_short' AND name != 'prediction_medium' AND name != 'prediction_long';"
            )
            rows = c.fetchall()
            for row in rows:
                c.execute(
                    f"DELETE FROM {row[0]} WHERE input = 'transcript'"
                )
                connection.commit()
            connection.close()


if __name__ == '__main__':
    main()