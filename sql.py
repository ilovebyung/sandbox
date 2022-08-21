import sqlite3
from datetime import datetime
from dateutil import parser

try:
    conn = sqlite3.connect("database.db")
    # conn = sqlite3.connect("d:/tmp/database.db")
    print("Database opened successfully")
except:
    print('failed to open database')

try:
    cur = conn.cursor()
    cur.execute("select * from Post")
    rows = cur.fetchall()
    for row in rows:
        print(row)
except:
    print('an error has occured')

start = ((rows[0][3]))
end = ((rows[2][3]))
start_date = parser.parse(start)
end_date = parser.parse(end)

try:
    cur = conn.cursor()
    cur.execute(
        f"select * from TB where date_created between '{start}' and '{end}'")
    rows = cur.fetchall()
    for row in rows:
        print(row)
except:
    print('an error has occured')


name = 'game'
try:
    conn = sqlite3.connect("database.db")
    conn.execute("insert into TB (name) values (name)")
except:
    print("transaction was successfully")
    conn.close()

'''
drop table
conn = sqlite3.connect("c:/source/clean_flask/database.db")  
'''
