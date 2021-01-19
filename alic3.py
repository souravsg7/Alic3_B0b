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
		response=client.recv(4096).decode()
		print(response)
		message=input("$")
	client.close()

except:
	print("[*] SOMETHING WEIRD")
	sys.exit(0)
	


