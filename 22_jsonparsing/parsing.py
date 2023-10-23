import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter: ')
if len(url) < 1 : url = 'http://py4e-data.dr-chuck.net/comments_441607.json'
print('=' + url + '=')
data = urllib.request.urlopen(url).read()

info = json.loads(data)
print('User count:', len(info))

comments = info['comments']

count = 0
for comment in comments:
    amount = int(comment['count'])
    count = count + amount

print('Count', count)
