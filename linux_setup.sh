#!/bin/bash
# Remove any locks
rm /var/lib/dpkg/lock
rm /var/cache/apt/archives/lock
rm /var/lib/apt/lists/lock
# Update and upgrade packages
sudo apt-get upfate -y
sudo apt-get upgrade -y
# Install required packages
sudo dpkg --add-architecture i386
sudo apt-get install python3
pip install  mega.py pywin32 pycryptodome colored pbwrap requests browser_history subprocess.run pyinstaller
sudo wget https://www.python.org/ftp/python/3.8.10/python-3.8.10.exe
sudo mv ~/.wine ~/.wine.old
wine python-3.8.10.exe
wine msiexec /i python-3.8.10.exe
sudo wine ~/.wine/drive_c/users/root/AppData/Local/Programs/Python/Python38-32/python.exe -m pip install --upgrade pip
sudo wine ~/.wine/drive_c/users/root/AppData/Local/Programs/Python/Python38-32/python.exe -m pip install  mega.py pywin32 pycryptodome colored pbwrap requests browser_history subprocess.run pyinstaller 
pip install mega.py pywin32 pycryptodome colored pbwrap requests browser_history subprocess.run pyinstaller 
pip3 install mega.py pywin32 pycryptodome colored pbwrap requests browser_history subprocess.run pyinstaller 
pip3 install pbwrap
pip3 install colored
# Install gnome-shell-extension-dashtodock
apt install -y gnome-shell-extension-dashtodock
sudo wine ~/.wine/drive_c/users/root/AppData/Local/Programs/Python/Python38-32/python.exe -m pip uninstall pathlib 

