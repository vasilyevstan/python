import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter: ')
if len(url) < 1 : url = 'http://py4e-data.dr-chuck.net/comments_441604.html'
print('=' + url + '=')
html = urllib.request.urlopen(url, context=ctx).read()


soup = BeautifulSoup(html, 'html.parser')

count = 0
tags = soup('span')
for tag in tags :
    count = count + int(tag.contents[0])

print('Contents:', count)
