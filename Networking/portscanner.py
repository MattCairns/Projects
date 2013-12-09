import socket


def port_scanner(ip, low, high):
    for i in range(low, high):
        s = socket.socket()
        s.settimeout(0.01)
        response = s.connect_ex((ip, i))

        if response:
            print str(i) + ' OPEN'
        else:
            print str(i) + ' CLOSED'


port_scanner('google.com', 1, 1000)