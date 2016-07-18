#!/usr/bin/env python

#operations with tar 

import tarfile

class Verify_tar(object):
	
	def tools_tar(cls,_file,_opt):
		tar_op = tarfile.open(_file,"r")
		if _opt == "1":
			tar_op.list()
		elif _opt == "2":
			tar_op.getnames()
		elif _opt == "3":
			tar_op.members
		else:
			print ("Error")			
           









if __name__=="__main__":
	pass
