#################################################################################################
#                      Getting COVID data through the brasil.io API to a pandas DF              #
# Autor: Cláudio Falcão                                                                         #
# Version: V1                                                                                   #
#################################################################################################

# Libs
import requests
import json
from pandas import json_normalize

# 1º REQUISITION PARAMETERS
header = {"Authorization": "Your token here"}
url = "https://api.brasil.io/v1/dataset/covid19/caso/data/"

# 2º REQUEST THE API
request = requests.get(url, headers=header)
dados = request.json()
dados_dumps = json.dumps(dados)
data_frame = json.loads(dados_dumps)

# 3º PRINT RESULT AS A DATAFRAME
df = json_normalize(data_frame["results"])
print(df[df.city.notnull()])