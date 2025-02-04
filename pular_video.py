from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from tkinter import Radiobutton
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import pyautogui 
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as condicao_esperada
from selenium import webdriver
def iniciar_driver():
    # Fonte de opções de switches https://chromium.googlesource.com/chromium/src/+/master/chrome/common/chrome_switches.cc e  https://peter.sh/experiments/chromium-command-line-switches/
    chrome_options = Options()
    caminho_dwonload='E\\Storage\\Desktop'
    '''
    --start-maximized # Inicia maximizado
    --lang=pt-BR # Define o idioma de inicialização, # en-US , pt-BR
    --incognito # Usar o modo anônimo
    --window-size=800,800 # Define a resolução da janela em largura e altura
    --headless # Roda em segundo plano(com a janela fechada)
    --disable-notifications # Desabilita notificações
    --disable-gpu # Desabilita renderização com GPU
    '''
    arguments = ['--lang=pt-BR', '--window-size=1366,768', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    # Lista de opções experimentais(nem todas estão documentadas) https://chromium.googlesource.com/chromium/src/+/master/chrome/common/pref_names.cc
    # Uso de configurações experimentais
    chrome_options.add_experimental_option('prefs', {
        # Alterar o local padrão de download de arquivos
        'download.default_directory': caminho_dwonload,
        # notificar o google chrome sobre essa alteração
        'download.directory_upgrade': True,
        # Desabilitar a confirmação de download
        'download.prompt_for_download': False,
        # Desabilitar notificações
        'profile.default_content_setting_values.notifications': 2,
        # Permitir multiplos downloads
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    # inicializando o webdrive
            
    driver = webdriver.Chrome(options=chrome_options)
    wait=WebDriverWait(
        driver,
        999999999999999999999999,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException
        ]
    )
    return driver , wait
    # Navegar até um site
driver , wait= iniciar_driver()


driver.get('https://www.youtube.com/watch?v=r9P08bbllno')
pyautogui.press('enter')
while True:
        try:
            # Procurar pelo botão "Pular Anúncio"
            pular_video = ular_video = wait.until(condicao_esperada.visibility_of_element_located((By.XPATH,"//div[text()='Pular']")))
            pular_video.click()
            print("Anúncio pulado!")
        except:
            # Se não encontrar o botão, aguardar um pouco e tentar novamente
            print("Nenhum botão de pular anúncio encontrado. Verificando novamente...")
            time.sleep(2)
input('')
driver.close()