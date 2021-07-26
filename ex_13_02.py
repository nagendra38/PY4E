import urllib.request
import json

url = input('Enter URL: ')
connection = urllib.request.urlopen(url)
data = connection.read().decode() #string from utf-8 to unicode
js = json.loads(data) #deserialize 'data' to a Python object
print('Retrieving', url)
print('Retrieved', len(data), 'characters')

total = 0
count = 0
for item in js['comments']:
    num = item['count']
    total = total + num
    count = count + 1

print('Count:', count)
print('Sum:', total)
