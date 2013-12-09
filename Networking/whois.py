import requests


def whois_check(address):

    url = 'http://whoiz.herokuapp.com/lookup.json?url=' + address
    r = requests.get(url)

    return r.json()




print whois_check('google.com')


