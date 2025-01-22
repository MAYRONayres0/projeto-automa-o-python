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

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
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
    # inicializando o webdriver
    driver = webdriver.Chrome(options=chrome_options)
    return driver
    # Navegar até um site
driver = iniciar_driver()
driver.get("https://cursoautomacao.netlify.app/desafios.html")
sleep(1)
janela_inicial = driver.current_window_handle
driver.execute_script("window.scrollTo(0,3000);")
sleep(5)
# botao janela
bt_janela = driver.find_element(By.XPATH,"//button[text()='Abrir nova janela']")
sleep(5)
driver.execute_script('arguments[0].click()',bt_janela)
sleep(5)
janelas = driver.window_handles
for janela in janelas:
    print(janela)
    if janela not in janela_inicial:
        driver.switch_to.window(janela)
        campo_escrever = driver.find_element(By.XPATH,"//textarea[@id='opiniao_sobre_curso']")
        campo_escrever.send_keys('essa porra aí, vamo')
        sleep(4)
        bt_pesquisar = driver.find_element(By.XPATH,"//button[@id='fazer_pesquisa']")
        driver.execute_script('arguments[0].click()',bt_pesquisar)
        sleep(4)
        driver.close()
driver.switch_to.window(janela_inicial)
campo_comentario = driver.find_element(By.XPATH,"//textarea[@id='campo_desafio7']")
sleep(3)
campo_comentario.send_keys("olá meu nome é lucas, agora me diga porque você é uma de lá pueta, pommmmmmmmmmmmmmmmmmmmmbaa, pommmmmmmmmmmmmmmmmmmmba kkkk, madalena macumbeira")



input('')
driver.close()