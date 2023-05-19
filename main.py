import time
import requests
from threading import Thread
import os

try:
    os.environ["REPLIT_DB_URL"]
    print("""replforever is running\nhttps://github.com/0Midnite/replforeverarchive""")
except KeyError:
    print("replforever must be ran in replit")
    exit()

url = f'https://{os.environ["REPL_SLUG"]}.{os.environ["REPL_OWNER"]}.repl.co'

def pinger():
    while True:
        try:
            requests.get(url, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36", "replforever": "0Midnite#7462 https://github.com/0Midnite/replforeverarchive"})
        except Exception as e:
            print(e)
            pass
        time.sleep(5)
    
t = Thread(target=pinger)
t.start()
