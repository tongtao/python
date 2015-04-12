#!/usr/bin/python
# -*- coding: utf-8 -*-

import SocketServer, time 
import os

import checkFiles

class MyServer(SocketServer.BaseRequestHandler):

	def __init__(self, request, client_address,server):
		self.loginInit()
		self.UpdateInfo = checkFiles.ChechFiles(self.root_path)
		print "updateInfo ***************************"
		SocketServer.BaseRequestHandler.__init__(self, request, client_address, server)
		
		
	
	#def setup(self):
		#self.loginInit()
		#self.UpdateInfo = checkFiles.ChechFiles(self.root_path)

	def loginInit(self):

		self.user = 'tt'
		self.pwd = 'tt'
		self.root_path = 'E:\code\server'   
		print ">>>**the process of reading config has done**"
		print self.user
		print self.pwd
		print self.root_path
		
	
		
	def handle(self):
		print ">>> Connected from ", self.client_address
		self.loginInit()
		self.UpdateInfo.handleFileDateCheck()
		print self.UpdateInfo.updateFileAtr
		print "*************************"
		
		while True:
			receivedData = self.request.recv(8192)
			if not receivedData:  
				continue 
			#build a connection
			elif receivedData == 'Hi, server':  
				self.request.sendall('hi, client')                      
			elif receivedData.startswith('name'):  
				#the last element of list is the name
				self.clientName = receivedData.split(':')[-1]   
				if self.user==self.clientName:  
					self.request.sendall('valid')  
				else:  
					self.request.sendall('invalid')                          
			elif receivedData.startswith('pwd'):  
				self.clientPwd = receivedData.split(':')[-1]
				if self.pwd==self.clientPwd:
					self.request.sendall('valid')  
					
					# 接受文件名字符串
					self.response = self.request.recv(8192)
					fileNameString = self.response
					print fileNameString
					fileNameList = fileNameString.split()
					# 检测发来的文件名是否需要更新
					updateNameList = self.UpdateInfo.updateFileAtr.keys()
					print updateNameList
					for fileName in fileNameList:
						if fileName in updateNameList:
							self.request.sendall(fileName)
							time.sleep(3)
							print "send file flag: "+fileName
							sfile = open(self.root_path+'\\'+fileName,'rb')
							#***************************************                        
							while True:  
								data = sfile.read(1024)  
								if not data:  
									break 
								#divide the file into segments and send respectively.
								while len(data) > 0:  
									intSent = self.request.send(data)  
									data = data[intSent:]     
							time.sleep(3)
							self.request.sendall('EOF')
							sfile.close()
							time.sleep(3)
						else:
							self.request.sendall('NoNeed')
							time.sleep(3)
							
						
							
					
				else:  
					self.request.sendall('invalid') 
											 
			elif receivedData == 'bye':  
				break    
		self.request.close()              
		print 'Disconnected from', self.client_address  
		print   
			

#class AdServerSocketServer(SocketServer.TCPServer):
	#def __init__(self, server_address, ThreadedTCPRequestHandler):
		#SocketServer.TCPServer.__init__(self, server_address, AdServerTCPRequestHandler)
		#self.FileInfoInit()
		
	#def FileInfoInit(self):
		#self.files = ChechFiles(self.root_path)
		
		
if __name__ == '__main__':  
	print 'Server is started\nwaiting for connection...\n'  
	srv = SocketServer.ThreadingTCPServer(('localhost', 50001), MyServer)
	srv.serve_forever() 
	
		
	