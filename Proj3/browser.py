'''Eric Adams ea11c'''
from __future__ import print_function
import string
from socket import *

class HTTPConnection:
	def __init__(self, host, port = 80):
		self.s = socket()
		self.addr = (host, port)
		self.hostname = host
		self.s.connect(self.addr)

	def connect(self):
		self.s.connect(self.addr)

	def request(self, method, url, headers = None):
		data_str = method + ' ' + url + " HTTP/1.1\nHost: " + self.hostname + "\n"
		if headers == None:
			data_str = data_str + "\n"
			self.s.send(data_str)		
		else:
			t = str(headers)
			for item in t:
				if item not in ["{", ",", "'", "}"]:
					data_str = data_str + item
				elif item == ',':
					data_str = data_str + "\n"
			data_str = data_str + "\n\n"
			self.s.send(data_str)

	def getresponse(self):
		return HTTPResponse(self.s)

	def close (self):
		self.s.close()

class HTTPResponse:
	def __init__(self, sock):
		self.sock = sock
		self.data =''
		self.headers = {}
		self.version = ''
		self.status = ''
		self.reason = ''
		self.datafile = self.sock.makefile()
		templine = self.datafile.readline()
		temp = tuple(templine.split())
		if len(temp) == 3:
			self.version = temp[0]
			self.version = self.version[5] + self.version[6] + self.version[7]
			self.status = temp[1]
			self.reason = temp[2]
		else:
			self.version = temp[0]
			self.version = self.version[5] + self.version[6] + self.version[7]
			self.status = temp[1]
			self.reason = temp[2] + temp[3]
		for line in self.datafile:
			print(line)
			if line.isspace():
				break
			else:
				k, v = line.split(": ")
				v = v.strip()
				self.headers[k] = v
	def read(self, amt = 0):
		if amt == 0:
			return self.datafile.read()
		else:
			return self.datafile.read(amt)

	def getheader(self, name):
		if name in self.headers:
			return self.headers[name]
		else:
			return None

	def getheaders(self):
		return self.headers

