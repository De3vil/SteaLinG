def build_hs(email, Password):
	with open("dump_History.py","w+") as file:
		file.write("from Uptomage import upToMaGeHIS\n")
		file.write("from time import sleep\n")
		file.write("""
def run():
	if __name__ == "__main__":
		while 1:
			try:
	""")
		file.write(""" 
				history = upToMaGeHIS()
				""")
		file.write(""+"history.up("+"'"+email + "'" +"," + "'" + Password +"'" + ")" + "\n")
		file.write("				"+"break")
		file.write("""
			except Exception:
				sleep(20)
	""")
		file.write(""" 
run()
	""")
		file.close()
