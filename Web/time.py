"""
Get Atomic Time from Internet Clock - This program will get
the true atomic time from an atomic time clock on the Internet.
Use any one of the atomic clocks returned by a simple Google search.
"""

import re
from urllib2 import urlopen


def main():
    url = 'http://time.is/just'

