import sqlite3
from sqlite3 import Error
import sys
import os


def main():
    if len(sys.argv) == 0:
        return
    elif sys.argv[0] == "-h" or sys.argv[0] == "-help":
        print("-a: create table if not exists")
        print("-d: drop table if exists")
        print("-s: select all from")
    connection = None
    try:
        connection = sqlite3.connect(os.getcwd()[:-13] + "db/Fintech.db")
    except Error as e:
        print(e)
    match sys.argv[0]:
        case "-c":
            if connection:
                c = connection.cursor()
                for arg in sys.argv[1:]:
                    c.execute(
                    "CREATE TABLE IF NOT EXISTS " + arg + " ([date] TEXT PRIMARY KEY, [price] INTEGER, [input] TEXT)")
                    connection.commit()
                connection.close()
            return
        case "-d":
            if connection:
                c = connection.cursor()
                for arg in sys.argv[1:]:
                    c.execute("DROP TABLE IF EXISTS" + arg)
                    connection.commit()
                connection.close()
            return
        case "-s":
            if connection:
                c = connection.cursor()
                for arg in sys.argv[1:]:
                    c.execute("SELECT * FROM " + arg)
                    rows = c.fetchall()
                    for row in rows:
                        print(row)
                connection.close()
            return



if __name__ == '__main__':
    main()
