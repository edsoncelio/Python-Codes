#!/usr/bin/env python

import socket
from optparse import OptionParser     #formated output

#tcp/ip checker with sockets
def checker_tcp(address,port):
	soc = socket.socket()
	print ("trying connect to adress {} with port {}").format(address,port)
	try:
		soc.connect((address,port))
		print ("Sucessfull!")
		return True
	except socket.error, e:
		print ("Failed connection")	
        return False
        
        
        
if __name__=="__main__":
	parser = OptionParser()
	
	parser.add_option("-a","--address",dest="address",default="localhost",
	help="Address for server")
	
	parser.add_option("-p","--port",dest="port",type="int",default="80",
	help="Port for server")
	
	(options,args) = parser.parse_args()
	
	checker_tcp(options.address,options.port)
