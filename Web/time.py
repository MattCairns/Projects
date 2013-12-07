import requests
import time


def atomic_time():
    """Returns the true atomic time from time.is"""
    url = 'http://time.is/just'
    r = requests.get(url)

    time_html = r.text

    print time_html[10753+14:10753+22]

    time.sleep(30)


while True:
    atomic_time()

