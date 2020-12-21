##########################
# OBTENDO DATA ATUAL
##########################


# Abaixo iremos demonstrar algumas dicas para obter a data e hora atual utilizando a biblioteca datetime

# Nosso roteiro:
# 1 - Imprimindo a data atual
# 2 - Mostrando a data no formato dd/mm/aaaa
# 3 - Mostrando a data no formato dd/mm/aaaa + a hora atual
# 4 - Garantir que o programa mostrará a data de acordo com determinado fuso horário
# 5 - Imprimindo resultado baseado no fusohorario definido


# Biblioteca
from datetime import date
from datetime import datetime, timezone, timedelta

# 1 - Imprimindo a data atual

data_hoje = date.today()
print('A data atual é: '+str(data_hoje))
# O formado impresso da data será aaaa/mm/dd

# 2 - Mostrando a data no formato dd/mm/aaaa

data_hoje_formatada = data_hoje.strftime('%d/%m/%Y')
print('A data atual é: '+str(data_hoje_formatada))

# Caso queira imprimir a data como dd/mm/aa, devemos apenas modificar o Y para y dentro do strftime
# Ficaria assim:
# data_hoje_formatada = data_hoje.strftime('%d/%m/%y')
# print(data_hoje_formatada)

# 3 - Mostrando a data no formato dd/mm/aaaa + a hora atual

data_hoje_hora = datetime.now()
data_hoje_hora_formatada = data_hoje_hora.strftime('%d/%m/%Y %H:%M')
print('A data e hora atual são: '+str(data_hoje_hora_formatada))

# 4 - Garantir que o programa mostrará a data de acordo com determinado fuso horário
# Utilizando o fuso +0 (Londres)

dif_fuso = timedelta(hours=0)
fuso = timezone(dif_fuso)
print('O fuso horário selecionado é: '+str(fuso))

# 5 - Imprimindo resultado baseado no fusohorario definido

data_hora_fuso_brasilia = data_hoje_hora.astimezone(fuso)
data_hora_fuso_brasilia_formatada = data_hora_fuso_brasilia.strftime('%d/%m/%Y %H:%M')
print('A data e hora atual baseao no fuso definido são: '+str(data_hora_fuso_brasilia_formatada))