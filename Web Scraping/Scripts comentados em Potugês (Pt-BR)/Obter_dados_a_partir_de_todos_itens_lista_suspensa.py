##########################################################################################################################
#                                       SCRAPING DE DADOS - SITE OFICIAL NBA
#                              CAPTURANDO DADOS DE TABELA A PARTIR DOS ITENS DA LISTA SUSPENSA
#
#Importante: No caso so site da NBA a opção all está disponível, porém, desenvolvemos o script para sites que não possuem
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
from selenium.webdriver.firefox.options import Options # Caso queira rodar no Firefox
#from selenium.webdriver.chrome.options import Options # Caso queira rodar no Google Crhome
from selenium.webdriver.support.ui import Select

#############################################################
# 1 - Capturando o conteudo da URL
#############################################################

url = "https://www.nba.com/stats/players/traditional/?sort=PTS&dir=-1&Season=2019-20&SeasonType=Regular%20Season"

# Instaciar o Crhome/Firefox
option = Options()
option.headless = False #True não irá mostrar a página abrindo, False irá mostrar a página abrindo
driver = webdriver.Firefox(options=option) # Caso queira rodar no firefox
#driver = webdriver.Chrome(options=option) # Caso queira rodar no Chrome


# Maximar a página
driver.maximize_window()

# Abrir a página no URL definido
driver.get(url)

# Tempo para carregar o botão de aceite dos cookies e dados da tabela
time.sleep(10)

# Clicar no botão para aceitas os Cookies
acept_buton = driver.find_element(By.ID,'onetrust-accept-btn-handler')
acept_buton.click()

###############################################################################
#                       Obtendo elementos do dropdownlist
###############################################################################

# Definindo objeto que recebera os elementos do dropdownlis
elementos = driver.find_element_by_class_name("stats-table-pagination__select")
drop_down = Select(elementos)
#drop_down.select_by_visible_text('text') # Onde text é o o texto exibido no dopdown list

# Contando a quantidade de opções disponíveis
#print(len(drop_down.options))

# Capturando todas as opções disponíveis e gravando em uma lista

todas_as_opcoes = drop_down.options # Objeto contendo as opções do dropdown list

lista_opcoes = [] # Lista que irá conter cada uma das opções disponíveis do dropdownlist
# Iteração para obter cada uma das opções, desprezando a opção all
for opcao in todas_as_opcoes:
    if opcao.text != "All":
        n_opcao = opcao.text
        lista_opcoes.append(n_opcao)
# Printar a lista com as opções do dropdown list
# print(lista_opcoes)

###############################################################################
# Capturando os dados da tabela partir das opções
###############################################################################

path = r"C:\Users\Cláudio Falcão\Google Drive\[01] - DATA SCIENCE\[05] - SCRIPTS\[01] - PYTHON\nba_"
for clicar in lista_opcoes:
    drop_down.select_by_visible_text(clicar)
    # Captura da tabela com os dados
    element = driver.find_element_by_xpath("/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[2]/div[1]/table")
    html_content = element.get_attribute('outerHTML')
    # Pasing dos dados
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find(name='table')
    # Obter os dados em um dataframe
    df = pd.read_html(str(table))[0]
    caminho_salvar = path+str(clicar)+".csv"
    df.to_csv(caminho_salvar)

###############################################################################
# Unindo em um unico arquivo csv
###############################################################################

# Lista com nome dos arquivos
nome_arquivos = []
for l_arq in lista_opcoes:
    n_arq = path+l_arq+".csv"
    nome_arquivos.append(n_arq)

# Concatenando os arquivos csv
nba_todos_dados = pd.concat([pd.read_csv(f) for f in nome_arquivos])

# Salvando o arquivo CSV completo
endereco_salvar = r"C:\Users\Cláudio Falcão\Google Drive\[01] - DATA SCIENCE\[05] - SCRIPTS\[01] - PYTHON\nba_todos_dados.csv"
nba_todos_dados.to_csv(endereco_salvar, index = False, encoding='utf-8-sig')





