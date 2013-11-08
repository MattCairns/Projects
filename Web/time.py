import requests


def atomic_time():
    """Returns the true atomic time from time.is"""
    url = 'http://time.is/just'
    r = requests.get(url)

    print r.text

atomic_time()

