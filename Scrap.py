from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt


url = "https://www.fravega.com/l/celulares/celulares-liberados/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

# Equipos

eq = soup.find_all("span", class_="sc-6321a7c8-0 jIfrVg")
equipos = list()

for i in eq:
    equipos.append(i.text)

#celulares = list()

#for i in equipos:
#    if "Celular" in i:
#        celulares.append(i)
#  Este ciclo For se tuvo que implementar dado que en la página aparecía en el scraping algunos modelos de televisores
#  como la página se fue actualizando lo voy a mantener para aplicarlo de ser necesario.

# Precios
pr = soup.find_all("span", class_="sc-ad64037f-0 Ojxif")

precios = list()

for i in pr:
    precios.append(i.text)

#precioCelulares = precios[16:29]
# Misma razón que el for anterior, aparecían modelos de televisores que no eran de mi interés, Lo conservo por si llegara a ser necesario.

ssl = len(precios)
fsl = len(precios) - len(equipos)

df = pd.DataFrame({"Nombres equipos": equipos, "Precios": precios}, index = list(range(fsl,ssl)))




def difMarcas():
    Samsung = 0
    Motorola = 0
    Xiaomi = 0
    iPhone = 0
    otros = 0
    Samsung = []
    Motorola = []
    Xiaomi = []
    iPhone = []
    otros = []
    for i in equipos:
        if "Samsung" in i:
            Samsung.append(i),
        if "Motorola" in i:
            Motorola.append(i),
        if "Xiaomi" in i:
            Xiaomi.append(i),
        if "iPhone" in i:
            iPhone.append(i),
        else:
            otros.append(i),
            return
    print("Samsung: ", (len(Samsung)))
    print("Motorola: ", (len(Motorola)))
    print("Xiaomi: ", (len(Xiaomi)))
    print("iPhone", (len(iPhone)))
    print("Otros: ", (int(len(otros) - len(Samsung) - len(Motorola) - len(Xiaomi) - len(iPhone))))





print(df)
print("Cantidad de modelos por marca: ")
difMarcas()

df.to_csv("CelularesFravega.csv", index=False)