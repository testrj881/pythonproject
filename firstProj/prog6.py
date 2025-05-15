#1. TO CHECK IF A WEBSITE IS UP OR DOWN
#ref: https://www.youtube.com/watch?v=B0p0VbgKkf0 
import requests
import time

def check_website(url):
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"{url} is up!")
            else:
                print(f"{url} is down! Status code: {response. status_code}")
            time.sleep(60)
        except requests. exceptions. RequestException:
            print(f"{url} is down!")
            time.sleep(60)