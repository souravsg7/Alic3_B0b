#!/usr/bin/env python
import socket
import subprocess
import sys

host=sys.argv[1]
port=int(sys.argv[2])
try:
	client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	client.connect((host,port))
	message=input("$")
	while True:	
		client.send(message.encode())
		response=s.recv(4096).decode()
		print(response)
	client.close()

except:
	print("[*] SOMETHING WEIRD")
	sys.exit(0)
	


