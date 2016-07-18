# -*- coding: utf-8 -*-
#  log.py
#  
#  Copyright 2016 Edson Celio <edsoncelio2013.1@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
#!/usr/bin/env python

# simple log viewer using gtk
#execute with root user 
import subprocess
import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class MyWin(Gtk.Window):
	
	def __init__(self):
		Gtk.Window.__init__(self,title="Log Viewer")
		self.set_border_width(5)
		self.set_default_size(1024, 768)
		
		self.grid = Gtk.Grid()
		self.add(self.grid)
		
		self.create_header()
		self.create_text_view()
		self.create_button()
		self.create_combo()
	
	def create_text_view(self):
		scrolledwindow = Gtk.ScrolledWindow()
		scrolledwindow.set_hexpand(True)
		scrolledwindow.set_vexpand(True)
		self.grid.attach(scrolledwindow, 1, 10, 5, 10)
		
		self.textview = Gtk.TextView()
		self.textview.set_editable(False)
		self.textview.set_cursor_visible(False)
		self.textbuffer = self.textview.get_buffer()
		scrolledwindow.add(self.textview)
			
         	
	def create_header(self):                    
		header = Gtk.HeaderBar(title="Log Viewer")       
		header.set_subtitle("A simple viewer for logs ")
		header.props.show_close_button = True
		self.set_titlebar(header)
	
	def create_button(self):
		button = Gtk.Button.new_with_label("Quit")
		button.connect("clicked",self.on_click_quit)
		self.grid.attach(button,3,20,1,1)
	
	def on_click_quit(self,button):
		Gtk.main_quit()
		
	def create_combo(self):
		logs = ["Secure", "Messages", "Boot", "Firewall"]
		log_combo = Gtk.ComboBoxText()
		log_combo.set_entry_text_column(0)
		log_combo.connect("changed", self.on_log_combo_changed)
		for log in logs:
			log_combo.append_text(log)
		self.grid.attach(log_combo,15,0,5,1)           #see later
	
	def select_log(self,text="Secure"):
		if text == "Secure":
			return self.textbuffer.set_text(subprocess.check_output(['cat','/var/log/secure']))
		elif text == "Messages":
			return self.textbuffer.set_text(subprocess.check_output(['cat','/var/log/messages']))
		elif text == "Boot":
			return self.textbuffer.set_text(subprocess.check_output(['cat','/var/log/boot.log']))
		elif text == "Firewall":
			return self.textbuffer.set_text(subprocess.check_output(['cat','/var/log/firewalld']))
		else:
			exit(1)
	
	def on_log_combo_changed(self, combo):		
			text = combo.get_active_text()
			if text != None:
				#print("Selected: log type={}").format(text)
				self.select_log(text)					 	
					
			
		
	
	    
win = MyWin()
win.connect("delete-event",Gtk.main_quit)
win.show_all()
Gtk.main()


'''
Features to add :
*select why log want see (secure,message,boot.log, ...) done!
*scroll bar done !
*search entry 
*real time 
*button done !
'''

