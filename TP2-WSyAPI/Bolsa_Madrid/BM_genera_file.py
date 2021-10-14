import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import pandas as pd

url_page = 'https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000'

page = requests.get(url_page).text 
soup = BeautifulSoup(page, "lxml")

tabla = soup.find('table', attrs={'id': 'ctl00_Contenido_tblAcciones'})
tabla
name=""
price=""
var = ""
maxima = ""
minima = ""
nroFila=0
for fila in tabla.find_all("tr"):
    #for row in  tabla.find_all("td")::
    nroCelda=0
    for celda in fila.find_all('td'):
        if nroCelda==0:
            name=celda.text
            print("Accion:", name)
        if nroCelda==1:
            price=celda.text
            print("Valor:", price)
        if nroCelda==2:
            var=celda.text
            print("Variacion:", var)
        if nroCelda==3:
            maxima=celda.text
            print("Maxima:", maxima)
        if nroCelda==4:
            minima=celda.text
            print("Minima:", minima)
        nroCelda=nroCelda+1
    nroFila=nroFila+1

    with open('bolsa_acciones.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([name, price , var , maxima , minima ,datetime.now()])
        

df = pd.read_csv('bolsa_acciones.csv')
df.columns = ["Nombre", "Precio", "Variacion", "Maxima", "Minima", "Fecha"]
df.to_csv('bolsa_acciones.csv')

print(df)