from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

from app import iniciar_driver


driver = iniciar_driver()
driver.get('https://sede.mjusticia.gob.es/eConsultas/inicioNacionalidad')
driver.maximize_window()
site_key = driver.find_element(By.XPATH,'//*[@id="captchaTramite"]/div/div/div').get_attribute('outerHTML')