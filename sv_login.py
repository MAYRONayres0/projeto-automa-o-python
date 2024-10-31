import pyautogui 
import time
import os
email = pyautogui.prompt("seu email")
senha=pyautogui.password("sua senha")
os.system("notepad.exe")
pyautogui.sleep(seconds=1)
pyautogui.write(f"seu e-mail: {email} sua senha: {senha}", interval=0.2)