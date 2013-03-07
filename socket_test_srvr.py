#Server side socket programming excercise

import socket
import sys

HOST = ''
PORT = 5555

#Create socket s
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error message: ' + str(msg[1])
    sys.exit()

#Bind socket s to an abritary host and port    
try:
    s.bind((HOST, PORT))
except socket.error, msg:
    print 'Bind failer, error message: ' + msg[1]
    sys.exit()
print 'Bind successfull'

#Set socket to listen for connections
s.listen(2)
print 'Socket now listening'
conn, addr = s.accept() #Accept incoming connection
print 'Connected with host on ' + addr[0] + ':' + str(addr[1])
