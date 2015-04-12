#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket, time
import yaml

class MyClient:
	def __init__(self):
		print 'Prepare for connecting...'

	def readConfig(self):
		try:
			config = yaml.load(file('/home/entouch/emsys/sync_files/client/clientConfig.yaml',"r"))
		except yaml.YAMLError:
			print "error in configuration file"
		self.fileNameString = config['file']


	def connect(self):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect(('219.219.220.201', 50001))
		#connect to the server
		sock.sendall('Hi, server')
		self.response = sock.recv(8192)
		print 'Server:', self.response
		#instance's attribute
		#self.s = raw_input("Connect to the server?(y/n):")
		self.s = 'y'
		if self.s == 'y':
			while True:
				#self.name = raw_input('Server: input your name:')
				#sock.sendall('name:' + self.name.strip())
				self.name = 'tt'
				sock.sendall('name:tt')
				self.response = sock.recv(8192)
				if self.response == 'valid':
					print "user " + self.name + " accept"
					break
				else:
					print 'Server: Invalid username'
			self.readConfig()
			time.sleep(3)
			while True:
				#self.pwd = raw_input('Server: input our password:')
				#sock.sendall('pwd:' + self.pwd.strip())
				sock.sendall('pwd:tt')
				self.response = sock.recv(8192)
				if self.response == 'valid':
					print 'Welcome '+self.name+'\n'+'please wait...'

					# 发送文件名字符串
					sock.sendall(self.fileNameString)

					for fileName in self.fileNameString.split():

						self.response = sock.recv(8192)

						string = self.response
						print string + "something"
						if string == 'NoNeed':
							print "This file " + fileName + " no need to update."
							continue
						print "receive " + fileName
						fileName = "/home/entouch/emsys/sync_files/client/" + fileName
						f = open(fileName, 'wb')
						while True:
							data = sock.recv(1024)
							if data == 'EOF':
								break
							f.write(data)
						f.flush()
						f.close()

						print "receive " + fileName + " done."
						
					
					print "all file done"
					break

				else:
					print 'Server: Invalid password'


		sock.sendall('bye')
		sock.close()
		print 'Disconnected'

if __name__ == '__main__':
	client = MyClient()
	client.connect()

