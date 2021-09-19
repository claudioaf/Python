#################################################################################################
#                      Getting COVID data through the brasil.io API                             #
# Autor: Cláudio Falcão                                                                         #
# Version: V1                                                                                   #
#################################################################################################

# Libs
import requests
import csv

# 1º REQUISITION PARAMETERS
header = {"Authorization": "Your token here"}
url = "https://api.brasil.io/v1/dataset/covid19/caso/data/"

# 2º NAME OF THE CSV FILE
fname = "covid.csv"

# 3º REQUEST THE API
request = requests.get(url, headers=header)
dados = request.json()
# print(dados["next"])
# print(dados["results"])

# Counter to show the page (We will not use it here)
#i = 1

# 4º CREATING THE FIRST FILE 
with open(fname, "w") as file:
    csv_file = csv.writer(file)
    csv_file.writerow(["city", "date", "confirmed", "deaths"])
    for item in dados["results"]:
        csv_file.writerow([item['city'], item['date'],
                           item['confirmed'], item['deaths']])
# print(f"Página{i}")

# 5º PARAMETERS OF THE REQUISITION IN THE LOOP
url_2 = dados["next"]
request = requests.get(url_2, headers=header)
dados = request.json()

# 6º GETTING DATA FROM THE NEXT PAGES
while url_2 != "null":

    # ADDING DATA FROM THE FOLLOWING PAGES
    with open(fname, "a") as file:
        csv_file = csv.writer(file)
        for item in dados["results"]:
            csv_file.writerow([item['city'], item['date'],
                               item['confirmed'], item['deaths']])

    i = i + 1
    print(f"Página{i}")

    url_2 = dados["next"]
    request = requests.get(url_2, headers=header)
    dados = request.json()

else:
    print("Import finished")
