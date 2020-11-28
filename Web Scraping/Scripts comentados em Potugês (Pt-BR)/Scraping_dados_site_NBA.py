##########################################################################################################################
#                                       SCRAPING DE DADOS - SITE OFICIAL NBA
#                                               MBA BI COM BIG DATA
# Alunos: 
#        Cláudio Anselmo Falcão
#        Haroldo Segundo
##########################################################################################################################

#############################################################
# Bibliotecas que precisaremos para realizar os procedimentos
#############################################################

import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.firefox.options import Options # Caso queira rodar no Firefox
from selenium.webdriver.chrome.options import Options # Caso queira rodar no Google Chrome

#############################################################
# 1 - Capturando o conteudo da URL
#############################################################

url = "https://www.nba.com/stats/players/traditional/?sort=PTS&dir=-1&Season=2019-20&SeasonType=Regular%20Season"

# Instaciar o Crhome ou Firefox
option = Options()
option.headless = False #True não irá mostrar a página abrindo, False irá mostrar a página abrindo
# driver = webdriver.Firefox(options=option) # Caso queira rodar no firefox
driver = webdriver.Chrome(options=option) # Caso queira rodar no Google Chrome

# Maximar a página
driver.maximize_window()

# Abrir a página no URL definido
driver.get(url)

# Tempo para carregar o botão de aceite dos cookies e dados da tabela
time.sleep(10)

#############################################################
# 1.1 Encontrar os elemento ao qual silumaremos os clicks
#############################################################

# Clicar no botão para aceitas os Cookies
acept_buton = driver.find_element(By.ID,'onetrust-accept-btn-handler')
acept_buton.click()

# Selecionar all no drop down list
driver.find_element_by_xpath("/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select/option[1]").click()

# Capturar a tabela com os dados
element = driver.find_element_by_xpath("/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[2]/div[1]/table")
html_content = element.get_attribute('outerHTML')

driver.quit() # Sair da página 

#########################################################################
# 2 - Parseando o conteúdo HTML com a biblioteca Bealtifulsoup
#########################################################################

soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(name='table')

#########################################################################
# 3 - Transformando o conteúdo HTML em um dataset com a bibliteca Pandas
#########################################################################

# Obter os dados html paseados em um dataframe
df = pd.read_html(str(table))[0]
#print(df)

# Exportanto o dataframe para um arquivo em CSV
path = r"C:\Users\Cláudio Falcão\Google Drive\[01] - DATA SCIENCE\[05] - SCRIPTS\[01] - PYTHON\nba.csv"
df.to_csv(path)
 