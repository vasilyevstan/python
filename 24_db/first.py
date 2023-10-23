import sqlite3

connection = sqlite3.connect('firstdb.sqlite')
print(connection)
cursor = connection.cursor()
print(cursor)

cursor.execute('''
DROP TABLE IF EXISTS Counts''')

cursor.execute('''
CREATE TABLE Counts(email TEXT, count INTEGER)''')

connection.commit()
