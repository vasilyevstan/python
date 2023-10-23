
def create (cursor) :
    cursor.execute('''
    CREATE TABLE Artist (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE
    )''')

    cursor.execute('''
    CREATE TABLE Genre (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE
    )''')

    cursor.execute('''
    CREATE TABLE Album (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        artist_id  INTEGER,
        title   TEXT
    )''')

    cursor.execute('''
    CREATE TABLE Track (
        id  INTEGER NOT NULL PRIMARY KEY
            AUTOINCREMENT UNIQUE,
        title TEXT,
        album_id  INTEGER,
        genre_id  INTEGER,
        len INTEGER, rating INTEGER, count INTEGER
    )''')

def drop(cursor) :
    cursor.execute('''
    DROP TABLE IF EXISTS Artist''')
    cursor.execute('''
    DROP TABLE IF EXISTS Genre''')
    cursor.execute('''
    DROP TABLE IF EXISTS Album''')
    cursor.execute('''
    DROP TABLE IF EXISTS Track''')
