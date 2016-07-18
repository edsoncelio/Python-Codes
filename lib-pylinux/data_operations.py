#!/usr/bin/env python

#operations with data

import os
import filecmp          # lib comparation
from glob import glob    #lib find
import shutil            #lib cp and mv

class Data_comp(object):                    
	
	def comp_files(cls,var1,var2):
		print filecmp.cmp(var1,var2)
		return filecmp.cmp(var1,var2).report()
	
	def comp_dir(cls,dir1,dir2):
		return filecmp.dircmp(dir1,dir2).report()

class Find_data(object):                      #find a file or directory using a pattern
	
	def find_pattern(cls,_dir,_pattern="*"):
		add = "*"+_pattern
		os.chdir(_dir)
		print glob(add)
		
class Data_cp_mv(object):
	
	def cp(source,dest):
		try:
			shutil.copy(source,dest)
		except Shutil.Error,e:
			print ("Error")
			
	def cp2(source,dest):     #preserve metadata
		try:
			shutil.copy2(source,dest)
		except Shutil.Error,e:
			print ("Error")			
	
	def mv(source,dest):
		try:
			shutil.move(source,dest)
		except Shutil.Error,e:
			print ("Error")				
						


if __name__=="__main__":
	pass
     
