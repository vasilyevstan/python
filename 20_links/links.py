# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter: ')
if len(url) < 1 : url = 'http://py4e-data.dr-chuck.net/known_by_Caine.html'

# Retrieve all of the anchor tags

count = 0
while count < 7 :
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

    count = count + 1
    print (tags[17])
    url = tags[17].get('href', None)
