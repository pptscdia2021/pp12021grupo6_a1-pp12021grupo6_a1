
# Se importan las librerías necesarias para web scraping
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from Graficar import grafganper

now = datetime.now()

# Se guarda url para el scrap en una variable
url_page = 'https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000'

# Se configuran las librerías para hacer scraping y se guardan en variables
page = requests.get(url_page).text 
soup = BeautifulSoup(page, "lxml")

# Lee el contenido de la tabla de acciones del día de la ejecución, a traves de beautiful soap
tabla = soup.find('table', attrs={'id': 'ctl00_Contenido_tblAcciones'})
tabla
name=""
price=""
var = ""
maxima = ""
minima = ""
nroFila=0

# Se recorre la tabla y se le asigna nombre a las columnas para cada dato extraído
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

# Se genera el csv con los datos de extraídos de la bolsa del día
    with open('TP2-WSyAPI/TP2-Nuevoprueba/CSV/bolsa_acciones.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([name, price , var , maxima , minima ,now.date()])
        
# Se lee el csv, con pandas, y se guarda en variable df
df = pd.read_csv('TP2-WSyAPI/TP2-Nuevoprueba/CSV/bolsa_acciones.csv')
df.columns = ["Nombre", "Precio", "Variacion", "Maxima", "Minima", "Fecha"]
df.to_csv('TP2-WSyAPI/TP2-Nuevoprueba/CSV/bolsa_acciones.csv')

# Se imprime el dataframe
print(df)

# Se toma la columna variación del csv y se aplica función recursiva lambda para que reemplace el 
# string "," por el string ".", para luego poder aplicar funciones de máximos y mínimos.
df['Variacion'] = df['Variacion'].apply(lambda x: x.replace(',','.'))

# Se convierten los datos de la columna Variación a tipo float
df['Variacion'] = df['Variacion'].astype(float)

# Se imprime la tabla de datos, ordenados por la columna Variación
print(df.sort_values(by=['Variacion']))

# Con las funciones max() y min() se guardan los valores maximos y mínimos de Variación 
maxs = df['Variacion'].max()
minimo= df['Variacion'].min()

# Se imprimen los valores máximos y mínimos encontrados
print("Maximo de Variación:")
print(maxs)
print("Mínimo de Variación:")
print(minimo)

# Se imprime el dataframe
print(df)


# Se invoca función para graficar desde Graficar.py
grafganper(df,'Variacion','Nombre', 12, 15)


maxs = df['Variacion'].max()

minimo= df['Variacion'].min()


print("Maximo de Variación:")
print(maxs)

print("Mínimo de Variación:")
print(minimo)

# Se realiza la selección de filas que se quieren mostrar, por indice
df4= df.iloc [[7,33,30,10]]
df4

# Se convierte df a csv
df4.to_csv('TP2-WSyAPI/TP2-Nuevoprueba/CSV/bolsa_4acciones.csv')

# Imprime variacion de las 4 acciones seleccionadas y extraídas del nuevo csv
grafganper(df4,'Variacion','Nombre',5,5)



