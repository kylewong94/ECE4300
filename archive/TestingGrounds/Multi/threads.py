#!/usr/bin/python3.7
import threading
import time


class Thread(threading.Thread):
	def __init__(self, threadID, Function, Args):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.Args = []
		self.Args = Args
		self.threadLock = threading.Lock()
		self.Funct = Function
		
	def start(self):
		print ("Starting ThreadNo: " + str(self.threadID))
		self.threadLock.acquire()
		if (self.Args == None):
			self.Funct()	
		else:
			self.Funct(self.Args)
 
		self.threadLock.release()
	
