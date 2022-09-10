from logging import PlaceHolder
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
        arquivo = open('dados.txt','r')
        dados = arquivo.readlines()
        self.dado_nie = str((dados[0]))
        self.dado_nie = (self.dado_nie.strip('\n'))
        self.dado_numero = str((dados[1]))
        self.dado_numero = (self.dado_numero.strip('\n'))
        self.dado_ano = str((dados[2]))
        self.dado_ano = (self.dado_ano.strip('\n'))
        layout = [
            [sg.Text('NIE', size=(6,0)), sg.Input(f'{self.dado_nie}', size=(15,0), key='nie'), sg.Text('Su NIE', size=(6,0))],
            [sg.Text('Número', size=(6,0)), sg.Input(f'{self.dado_numero}',size=(15,0), key='numero'), sg.Text('Ejemplo: R *500001* /2015', font=('Arial', 10, 'bold'), size=(25,0))],
            [sg.Text('Año', size=(6,0)), sg.Input(f'{self.dado_ano}', size=(5,0), key='ano'), sg.Text('Ejemplo: R500001 / *2015*', font=('Arial', 10, 'bold'), size=(25,0))],
            [sg.Button('Enviar')],
        ]
        self.janela = sg.Window('Datos de la solicitud', size = (600,200), finalize=True).layout(layout)
        
    def salvar(self):
         with open('dados.txt', 'w') as arquivo:
                arquivo.write(f'{self.nie}\n')
                # arquivo.write('\n')
                arquivo.write(f'{self.numero}\n')
                # arquivo.write('\n')
                arquivo.write(f'{self.ano}\n')

    def enviar(self):
        print(self.nie)
        print(self.numero)
        print(self.ano)
        driver = iniciar_driver()
        driver.get('https://sede.mjusticia.gob.es/eConsultas/inicioNacionalidad')
        driver.maximize_window()
        sleep(2)
        campo_nie = driver.find_element(By.ID,'codigoNieCompleto')
        campo_nie.send_keys(self.nie)
        sleep(2)
        campo_numero = driver.find_element(By.ID,'numero')
        campo_numero.send_keys(self.numero)
        sleep(2)
        campo_ano = driver.find_element(By.ID,'yearSolicitud')
        campo_ano.send_keys(self.ano)
        sleep(10)
        
        input('')
        driver.close()
    
    def Iniciar(self): 
        while True:             
            self.button, self.values = self.janela.Read()
            self.nie = self.values['nie']
            self.numero = self.values['numero']
            self.ano = self.values['ano']
            

            if self.button == 'Enviar':
                self.salvar()
                self.enviar()
            
            # if self.event == sg.WINDOW_CLOSED:
            #     self.janela.close()


tela = TelaDados()
tela.Iniciar()
