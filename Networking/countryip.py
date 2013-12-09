import requests

def get_ip():
    r = requests.get('http://icanhazip.com/')

    return r.text


def geolocate(ip):
    print 'http://ipinfodb.com/ip_query.php?ip=%s' % ip
    r = requests.get('http://freegeoip.net/json/%s' % ip)
    r = r.json()

    print r['city']
    print r['region_name']
    print r['country_name']

    return r


ip = get_ip()
geolocate(ip)

