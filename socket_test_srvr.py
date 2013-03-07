#Server side socket programming excercise

import socket
import sys
from thread import * 

HOST = ''
PORT = 5555
def clientthread(conn):
    #Vastataan yhteyteen
    conn.sendall('Saatana mie tahtosin nukkua! Mutta leikkik‰‰!')
    while True:
        print 'Connected with host on ' + addr[0] + ':' + str(addr[1])
        reply = conn.recv(1024)
        print reply
        if not reply:
            break
    conn.close()
    
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
s.listen(10)
print 'Socket now listening'

conn, addr = s.accept() #Accept incoming connection
while True:
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + '\n'
    start_new_thread(clientthread, (conn,))
s.close()

