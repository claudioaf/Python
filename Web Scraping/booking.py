##################################################################################################################
# Scraping de dados do booking V1.0
# Busca de acomodações em qualquer cidade
# Chatbot para informar sobre o processo
##################################################################################################################


# Bibliotecas

from datetime import date, timedelta, datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys
import random
import os
import requests

#################################################################################################################
#                                1 - FUNÇÃO PARA ENVIO DE MENSAGENS NO TELEGRAM
#################################################################################################################

# Função para envio de mensagem para o telegram


def enviar_mensagem(token, chat_id, mensagem):
    try:
        data = {"chat_id": chat_id, "text": mensagem}
        url = "https://api.telegram.org/bot{}/sendMessage".format(token)
        requests.post(url, data)
    except Exception as e:
        print("Erro no sendMessage:", e)


# Token
token = 'seu token'

# Chatid
chat_id = 'seu chat id'

#################################################################################################################
#                                    2 - INSTANCIANDO O CHROME
#################################################################################################################

# Definindo o diretório local do arquivo (Apenas para execução dos testes!)
#os.chdir('seu diretório de arquivos')

# Definindo endereço do site
url = "https://www.booking.com/index.pt-br.html?label=gen173nr-1BCAEoggI46AdIM1gEaCCIAQGYAS24ARfIAQzYAQHoAQGIAgGoAgO4Ar7ayf4FwAIB0gIkNjhkN2E4Y2YtMDQ2My00MDBhLTgyZWQtODZjMjZjODgzNmI42AIF4AIB;sid=5477c2732e09ae52a13f6764cbf5e754;keep_landing=1&sb_price_type=total&"

# Definindo o Web Driver
#driver = webdriver.Chrome()
driver = webdriver.Chrome(
    executable_path=os.getcwd() + os.sep + 'chromedriver.exe')  # Caso o webdriver esteja no diretório do arquivo .py

# Maximar a página
driver.maximize_window()

# Abrindo a página na url definida
driver.get(url)

#################################################################################################################
#                                3 - DEFININDO AS DATAS DE INICIO E FIM DA BUSCA
#################################################################################################################

dt_hoje = date.today()
dt_amanha = dt_hoje + timedelta(days=1)
dt_hoje_hora = datetime.now()
dt_hoje_hora_f = dt_hoje_hora.strftime('%d/%m/%Y %H:%M')

#################################################################################################################
#                                           4 - INICIANDO A BUSCA
#################################################################################################################

# Definindo cidade/região da busca das acomodações
local = 'São Paulo'

# Campo Para onde você vai? Inserindo o nome da cidade
campo_onde_vai = driver.find_element_by_xpath('//input[@type="search"]')

# sleep(random.randint(3,5))
campo_onde_vai.click()
# sleep(random.randint(3,5))
campo_onde_vai.send_keys(local)

###############################
# Definindo as datas de busca
###############################

# Definindo o xpath em relação a data atual + data amanhã
xpath_inicio = '//td[@class="bui-calendar__date bui-calendar__date--today"][@data-bui-ref="calendar-date"][@data-date="' + \
    str(dt_hoje)+'"]'
#xpath_inicio_direto_site = '//td[@class="bui-calendar__date bui-calendar__date--today"][@data-bui-ref="calendar-date"][@data-date="2020-12-12"]'
xpath_fim = '//td[@class="bui-calendar__date"][@data-bui-ref="calendar-date"][@data-date="' + \
    str(dt_amanha)+'"]'
#xpath_inicio_direto_site = '//td[@class="bui-calendar__date"][@data-bui-ref="calendar-date"][@data-date="2020-12-13"]'


# Abrindo o calendário para inserir os valores das datas inicio e fim
# sleep(random.randint(3,5))
abrir_calendario = driver.find_element_by_xpath(
    '//span[@class="sb-date-field__icon sb-date-field__icon-btn bk-svg-wrapper calendar-restructure-sb"]')
# sleep(random.randint(3,5))
abrir_calendario.click()

# Definindo data inicio
# sleep(random.randint(3,5))
data_inicio = driver.find_element_by_xpath(xpath_inicio)
# sleep(random.randint(3,5))
data_inicio.click()
# sleep(random.randint(3,5))
abrir_calendario.click()

# Definindo data fim
# sleep(random.randint(3,5))
abrir_calendario.click()
# sleep(random.randint(3,5))
data_fim = driver.find_element_by_xpath(xpath_fim)
# sleep(random.randint(3,5))
data_fim.click()

# Clicar no botão buscar
# sleep(random.randint(3,5))
botao_pesquisar = driver.find_element_by_xpath('//button[@data-sb-id="main"]')
botao_pesquisar.click()

# Envio da primeira mensagem
mensagem_1 = ("-----------------------------------------------------------------\nCaptura de dados iniciado com sucesso em " +
              str(dt_hoje_hora_f)+"\n**Local das acomodações:** "+local+"\n-----------------------------------------------------------------")
enviar_mensagem(token, chat_id, mensagem_1)

#################################################################################################################
#                                       5 - ORDENANDO A PÁGINA DE RESULTADOS
#################################################################################################################

sleep(random.randint(4, 5))
bt_preco_mais_baixo = driver.find_element_by_xpath(
    '//ul/li[@class=" sort_category   sort_price "]')
bt_preco_mais_baixo.click()

#################################################################################################################
#                                   6 - CAPTURANDO ELEMENTOS IMPORTANTES DAS ACOMODAÇÕES
#################################################################################################################

###############################
# Laço para ir a próxima página
###############################

total_acomodacoes = []

i = 1  # Contador da página

while True:
    try:
        # Título da acomodação
        sleep(random.randint(3, 5))
        titulo_acomodacao = driver.find_elements_by_xpath(
            '//div[@id="hotellist_inner"]/div/div/div/div/div/h3/a/span[1]')

        # Distância do centro
        # sleep(random.randint(3,5))
        dist_centro = driver.find_elements_by_xpath(
            '//span[@data-bui-component="Tooltip"][@data-tooltip-position="top"][ @data-tooltip-follow=""][@data-tooltip-light=""][@data-tooltip-text="Esta é uma distância em linha reta no mapa. A distância pode ser um pouco maior se você estiver de carro ou utilizando transporte público."]')

        # Preço da acomodação
        sleep(random.randint(3, 5))
        precos = driver.find_elements_by_xpath(
            '//div[@class="bui-price-display__value prco-inline-block-maker-helper "]')

        # Tipo cama
        sleep(random.randint(3, 5))
        tipo_camas = driver.find_elements_by_xpath(
            '//div[@class="c-beds-configuration"]')
    except:
        mensagem_erro = "O processo de captura dos dados não foi executado, verifique os possíveis problemas"
        print(mensagem_erro)
        # Mensagem de erro do processo
        enviar_mensagem(token, chat_id, mensagem_erro)

    #################################################################################################################
    #                           7 - CRIANDO ARQUIVO DE TEXTO COM OS DADOS CAPTURADOS
    #################################################################################################################

    lista_titulos = []
    for titulo, distancia, preco, cama in zip(titulo_acomodacao, dist_centro, precos, tipo_camas):

        # Criando as listas que irão informar a quantidade de acomodações
        lista_titulos.append(titulo)
        total_acomodacoes.append(titulo)

        # Criando o arquivo de texto
        with open('acomodacoes.txt', 'a', newline='', encoding='utf-8') as busca_titulo:
            busca_titulo.write(local + ',' + titulo.text + ',' + cama.text + ',' + distancia.text +
                               ',' + preco.text + ',' + str(dt_hoje_hora_f) + os.linesep)

        print("Arquivo da pagina "+str(i)+" criado!\n" +
              str(len(lista_titulos)) + " Acomodações foram adicionadas")

    # Mensagens de status do Loop da captura de dados das páginas
    mensagem_n = "Arquivo da pagina " + \
        str(i)+" criado!\n" + str(len(lista_titulos)) + \
        " Acomodações foram adicionadas"
    enviar_mensagem(token, chat_id, mensagem_n)

    #################################################################################################################
    #                             8 - NAVEGANDO PARA A PRÓXIMA PÁGINA
    #################################################################################################################

    try:
        sleep(random.randint(3, 5))
        # Rolar a página até o final da página:
        # driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        botao_proximo = driver.find_element_by_xpath(
            '//*[@id="search_results_table"]/div[4]/nav/ul/li[3]/a')
        sleep(random.randint(3, 5))
        botao_proximo.click()
        i = i + 1
    except:
        print(str(len(total_acomodacoes)) +
              ' Acomodações foram adicionados ao aquivo')
        mensagem_final = ("Processo finalizado com sucesso!\n"+str(i)+" Páginas foram varridas\n"+str(len(total_acomodacoes)) +
                          " Acomodações foram adicionados ao aquivo")
        print(mensagem_final)
        enviar_mensagem(token, chat_id, mensagem_final)
        sys.exit()
