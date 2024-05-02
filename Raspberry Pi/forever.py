from subprocess import Popen
import sys

filename = "keyboard.py"
while True :
   p = Popen("sudo nohup python3 /home/pi/Documents/keyboard.py", shell=True)
   p.wait()