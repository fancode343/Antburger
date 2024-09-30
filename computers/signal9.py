import requests
import time
import logging


logging.basicConfig(level=logging.INFO)


url = "http://panas2.lmnet.cf/status9"


interval = 500  

def send_signal():
    try:
      
        response = requests.post(url, data={'status': 'online'})
        
        if response.status_code == 200:
            logging.info("Signal sent successfully, server response: %s", response.text)
        else:
            logging.error("Failed to send signal, server response: %s", response.text)
    
    except requests.exceptions.RequestException as e:
        logging.error("Error sending signal: %s", str(e))

if __name__ == "__main__":
    while True:
        send_signal()
        time.sleep(interval)
