import PySimpleGUI as sg
import webbrowser
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep
# Para usar o explicito precisamos importar o WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
# Importar as exceções
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
# Fazer o import do By
from selenium.webdriver.common.by import By



def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,600', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)
        
    chrome_options.add_experimental_option('prefs', {
        # Desabilitar a confirmação de download
        'download.prompt_for_download': False,
        # Desabilitar notificações
        'profile.default_content_setting_values.notifications': 2,
        # Permitir multiplos downloads
        'profile.default_content_setting_values.automatic_downloads': 1,
    })

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    return driver



class TelaDados:
    def __init__(self):
        layout = [
            [sg.Text('NIE', size=(6,0)), sg.Input(size=(15,0), key='nie')],
            [sg.Text('Número', size=(6,0)), sg.Input(size=(15,0), key='numero')],
            [sg.Text('Año', size=(6,0)), sg.Input(size=(5,0), key='ano')],
            # [sg.Button('Salvar')],
            [sg.Button('Enviar')]
        ]
        self.janela = sg.Window('Datos de la solicitud', size = (400,200)).layout(layout)
        
    def consultar(self, dado_nie, dado_numero, dado_ano):
        pass
    
    def Iniciar(self):  
            
        self.button, self.values = self.janela.Read()
        self.nie = self.values['nie']
        self.numero = self.values['numero']
        self.ano = self.values['ano']

        # if self.button == 'Salvar':
        #     with open('dados.txt', 'w') as arquivo:
        #         arquivo.write(f'{self.nie}\n')
        #         arquivo.write(f'{self.numero}\n')
        #         arquivo.write(f'{self.ano}\n')

        if self.button == 'Enviar':
            # arquivo = open('dados.txt','r')
            # dados = arquivo.readlines()
            # dado_nie = str((dados[0]))
            # dado_numero = str((dados[1]))
            # dado_ano = str((dados[2]))
            print(self.ano)
            print(self.nie)
            print(self.numero)
            driver = iniciar_driver()
            driver.get('https://sede.mjusticia.gob.es/eConsultas/inicioNacionalidad')
            driver.maximize_window()
            sleep(5)
            campo_nie = driver.find_element(By.ID,'codigoNieCompleto')
            campo_nie.send_keys(self.nie)
            sleep(4)
            campo_numero = driver.find_element(By.ID,'numero')
            campo_numero.send_keys(self.numero)
            sleep(4)
            campo_ano = driver.find_element(By.ID,'yearSolicitud')
            campo_ano.send_keys(self.ano)
            sleep(4)
            captcha = pyautogui.locateCenterOnScreen('captcha.png')
            pyautogui.click(captcha[0], captcha[1], duration=0.5)
            sleep(4)
            pyautogui.press(['tab', 'tab', 'tab'])
            pyautogui.press('space')
            sleep(8)
            dados = driver.find_elements(By.XPATH,'//div[@class="bloqueCampoTextoInformativo"]')
            input('')
            driver.close()


tela = TelaDados()
tela.Iniciar()

