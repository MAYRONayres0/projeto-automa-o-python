import pyautogui
from time import sleep
import os
import time




#abrir o navegador
while True:
    pyautogui.click(484,741)
    pyautogui.typewrite("chrome")
    pyautogui.sleep(seconds=1)
    pyautogui.click(536,180)
    pyautogui.sleep(seconds=2)
    pyautogui.typewrite('instagram.com')
    pyautogui.press('enter')
    pyautogui.sleep(seconds=1)
    pyautogui.press('F11')
    pyautogui.sleep(seconds=2)
    pyautogui.click(89,175)
    pyautogui.sleep(seconds=2)
    pyautogui.typewrite("larypereira_27")
    pyautogui.sleep(seconds=2)
    pyautogui.click(220,173)
    pyautogui.sleep(seconds=2)
    pyautogui.click(529,621)
    pyautogui.sleep(seconds=2)
    coracao=pyautogui.locateCenterOnScreen('./coracao3.png')
    sleep(3)
    if coracao is not None:
        sleep(80000)
    elif coracao == None:
        pyautogui.click(811,610)
        sleep(2)
        pyautogui.click(854,615)
        sleep(1)
        pyautogui.typewrite("Eu te amo princesa, agradeço a Deus por estar na sua vida.")
        sleep(1)
        pyautogui.press('enter')