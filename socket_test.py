#Socket programming excercise

import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error message: ' + str(msg[1])
    sys.exit()
    
print 'Socket Created'

host = 'localhost'
try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print 'Hostname could not be resolved. Exiting.'
    sys.exit()
ip = '192.168.100.41'
port = 5555
s.connect((remote_ip, port))
print 'Socket connected to ' + host

 
