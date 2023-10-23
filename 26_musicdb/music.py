import xml.etree.ElementTree as ET
import sqlite3
import createdb

def create_artist(artist, cursor) :
    if artist is None : return None

    print('Inserting artist', artist)
    cursor.execute('''
    INSERT OR IGNORE INTO Artist (name) VALUES (?)''', (artist, ))
    cursor.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))

    return cursor.fetchone()[0]

def create_genre(genre, cursor) :
    if genre is None : return None

    print('Inserting genre', genre)
    cursor.execute('''
    INSERT OR IGNORE INTO Genre (name) VALUES (?)''', (genre, ))
    cursor.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))

    return cursor.fetchone()[0]

def create_album(album, artistId, cursor) :
    if album is None : return None

    print('Inserting album', album, artistId)
    cursor.execute('''
    INSERT OR IGNORE INTO Album (artist_id, title) VALUES (?, ?)''', (artistId, album, ))
    cursor.execute('SELECT id FROM Album WHERE artist_id = ? AND title = ? ', (artistId, album, ))

    return cursor.fetchone()[0]

def create_track(title, albumId, genreId, totalTime, rating, size , cursor) :
    if title is None : return None

    print('Inserting track', title, albumId, genreId, totalTime, rating, size)
    cursor.execute('''
    INSERT OR IGNORE INTO Track (title, album_id, genre_id, len, rating, count) VALUES (?, ?, ?, ?, ?, ?)''', (title, albumId, genreId, totalTime, rating, size))
    cursor.execute('SELECT id FROM Track WHERE title = ? AND count = ? ', (title, size, ))

    return cursor.fetchone()[0]

connection = sqlite3.connect('musicdb.sqlite')
cursor = connection.cursor()

createdb.drop(cursor)
print('Tables dropped')

createdb.create(cursor)
connection.commit()
print('Tables created')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'Library.xml'
fh = open(fname)

xml = fh.read()
tree = ET.fromstring(xml)

tracks = tree.findall('dict/dict/dict')

listOfTracks = list()
for track in tracks :
    #if track[0].text != 'Track ID' : continue
    dictTrack = dict()

    count = 0;
    while count < len(track) :
        dictTrack[track[count].text] = track[count+1].text
        count = count + 2

    listOfTracks.append(dictTrack)

print(len(listOfTracks))

for track in listOfTracks :

    genre = track.get('Genre', None)
    artist = track.get('Artist', None)
    title = track['Name']
    album = track.get('Album', None)
    #trackId = track['Track ID']
    totalTime = track.get('Total Time', None)
    rating = track.get('Rating', None)
    size = track.get('Size', None)

    print(title, artist, genre, totalTime, rating, size)

    artistId = create_artist(artist, cursor)
    genreId = create_genre(genre, cursor)
    albumId = create_album(album, artistId, cursor)
    trackId = create_track(title, albumId, genreId, totalTime, rating, size , cursor)

    connection.commit()

cursor.close()
