""" Module providing function for creatin a SQL DB"""
import sqlite3zzzzzzzz

''' Creates a connection to sqlite3 database'''
connection = sqlite3.connect("practice_data.sqlite3")
cursor = connection.cursor()

c = connection.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS
    demo
    ([S] TEXT PRIMARY KEY,
     [X] INTEGER,
     [Y] INTEGER) ''')

# c.execute("INSERT INTO demo VALUES ('g', 3, 9)")
# c.execute("INSERT INTO demo VALUES ('v', 5, 7)")
# c.execute("INSERT INTO demo VALUES ('f', 8, 7)")

# SQL query displaying the total of rows in the database
row_count = '''
    SELECT COUNT(*)
    FROM demo;'''

# SQL query for how many times 5 is in the X and Y column at the same time
xy_at_least_5 = '''
    SELECT COUNT(*)
    FROM demo
    WHERE X >= 5 AND Y >= 5;'''

# SQL query displying how many uniques values in the Y columnn
unique_y = '''
    SELECT COUNT(DISTINCT Y)
    FROM demo;'''

ROW = cursor.execute(row_count).fetchall()
# [(3,)]

XY = cursor.execute(xy_at_least_5).fetchall()
# [(2,)]

UNIQUE = cursor.execute(unique_y).fetchall()
# [(2,)]


print(ROW, XY, UNIQUE)

connection.commit()
connection.close()
