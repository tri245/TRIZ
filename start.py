import sys
import subprocess
import os
from time import sleep
from config import *

w1 = "EDIT YOUR CONFIG.PY BEFORE USING!\n"

def worker(file,token):
    print(token + " " + file)
    subprocess.call(file, shell=True)

for char in w1:
    sleep(0.01)
    sys.stdout.write(char)
    sys.stdout.flush()
sleep(0.5)
print(".")
print("1 : Image Spammer - Spam random images in a selected folder")
print("2 : trinho")
print("3 : trinho")

in_pick = float(input("Select a bot: "))

if in_pick == 1:
    for token in userToken:
        p = subprocess.Popen(['python', 'discord_image_spam.py', token],shell=True)
            
if in_pick == 2:
    for token in userToken:
        p = subprocess.Popen(['python','discord_insult_spam.py', token],shell=True)
        
if in_pick == 3:
    spam_text = input("Write spam text : ")
    print('python discord_text_spam.py ' + "'"+spam_text+"'")
    for token in userToken:
        print('Loading Token')
        p = subprocess.Popen(['python','discord_text_spam.py',token,spam_text],shell=True)
        sleep(1)
        print("Token Loaded.")
        print(' ')
p.wait()
