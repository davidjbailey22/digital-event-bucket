"""
Digital Bucket
sqlite configuration
By D. Bailey
"""
import sqlite3
from sqlite3 import Error

# database location on local
database = "/Users/DavidBailey/db/pythonsqlite.db"

# create connection to sqlite database
def create_connection(db_file):

    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

if __name__ == '__main__':
    create_connection(database)

# create table in sqlite database
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():

    # create table and columns
    sql_create_events_table = """ CREATE TABLE IF NOT EXISTS events_pt (
                                        id integer PRIMARY KEY,
                                        event text NOT NULL,
                                        type text,
                                        complete text,
                                        lat double,
                                        long double
                                    ); """

    # create a database connection
    conn = create_connection(database)
    create_table(conn, sql_create_events_table)

if __name__ == '__main__':
    main()