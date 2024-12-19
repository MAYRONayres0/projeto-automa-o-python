from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from tkinter import Radiobutton
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from time import sleep

def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,1200', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)
        

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(options=chrome_options)

    return driver


driver = iniciar_driver()
#driver.get('https://cursoautomacao.netlify.app/')
chrome_options = Options()
chrome_options.add_argument("--force-device-scale-factor=0.100")  # Ajusta o zoom (0.8 = 80%)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://cursoautomacao.netlify.app/desafios')


nome=driver.find_element(By.ID,'dadosusuario')
nome.send_keys('mayron ayres')
sleep(3)


botao=driver.find_element(By.XPATH,"//button[@id='desafio2']")
botao.click()
sleep(5)


nome_rept=driver.find_element(By.ID,'escondido')
nome_rept.send_keys('mayron ayres')
sleep(2)


botao_validar=driver.find_element(By.ID,'validarDesafio2')
botao_validar.click()

input('')
driver.close()