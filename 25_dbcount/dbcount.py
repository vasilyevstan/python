import sqlite3

connection = sqlite3.connect('emailcount.sqlite')
print(connection)
cursor = connection.cursor()
print(cursor)

cursor.execute('''
DROP TABLE IF EXISTS Counts''')
cursor.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')
connection.commit()

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue

    email = line.split()[1]
    domain = email.split('@')[1]

    cursor.execute('SELECT count FROM Counts WHERE org = ? ', (domain,))
    row = cursor.fetchone()

    if row is None:
        cursor.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (domain,))
    else:
        cursor.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (domain,))

    connection.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'

for row in cursor.execute(sqlstr):
    print(str(row[0]), row[1])

cursor.close()
