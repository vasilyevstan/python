import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter: ')
if len(url) < 1 : url = 'http://py4e-data.dr-chuck.net/comments_441606.xml'
print('=' + url + '=')
xml = urllib.request.urlopen(url).read()

tree = ET.fromstring(xml)

comments = tree.findall('./comments/comment')

count = 0
for comment in comments :
    count = count + int(comment.find('count').text)

print(count)
