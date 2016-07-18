#!/usr/bin/env python
import paramiko
from optparse import OptionParser

#connect to ssh using paramiko lib
#not using private key(read the footer)

def connect_ssh(hostname,port,username,password):
	try:
	   paramiko.util.log_to_file('paramiko.log')
	   con = paramiko.SSHClient()
	   con.connect(hostname,port,username,password)
	   stdin,stdout,stderr= con.exec_command('cat /etc/os-release') #command for test
	   print stdout.read()
	   con.close()
	except:
		print ("Failed")   
	   

if __name__=="__main__":
	parser= OptionParser()
	
	parser.add_option("-n","--hostname",dest="hostname",default="localhost",
	help="Hostname for server")
	
	parser.add_option("-p","--port",dest="port",type="int",default="80",
	help="Port for server")
	
	parser.add_option("-u","--username",dest="username",
	help="Username for server")
	
	parser.add_option("-w","--password",dest="password",
	help="Password for server")
	
	(options,arg)=parser.parse_args()
	
	connect_ssh(options.hostname,options.port,options.username,options.password)
	
#If using private key, try:
'''
add the variable pkfile = <location private key>
add the variable key = paramiko.RSAKey.from_private_key_file(pkey_file)
add s.connect(hostname, port, pkey=key)
and modify the function connect_ssh to connect_ssh(hostname,port,pkfile)

'''
