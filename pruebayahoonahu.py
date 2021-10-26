import yfinance as yf
import pandas as pd
import datetime
import csv
import numpy as np

BancoSantanderSA = yf.Ticker("SAN")
print(BancoSantanderSA.info['ask']) #Precio de compra acción
print(BancoSantanderSA.info['bid']) #Precio de venta acción

Telefonica = yf.Ticker ("TEF")
print (Telefonica.info['ask'])
print (Telefonica. info['bid'])

Repsol = yf.Ticker ("REP.MC")
print (Repsol.info['ask'])
print (Repsol. info['bid'])

BancoBBVA = yf.Ticker ("BBVA")
print (BancoBBVA.info['ask'])
print (BancoBBVA. info['bid'])

dfSAN = yf.download('SAN', start='2021-09-24', end='2021-10-05') #Obtengo datos de Yahoo para cada acción
dfSAN.reset_index(inplace=True,drop=False) #Me permite transformar a Date en columna al igual que las demas
dfTEF = yf.download('TEF', start='2021-09-24', end='2021-10-05')
dfTEF.reset_index(inplace=True,drop=False)
dfREPMC = yf.download('REP.MC', start='2021-09-24', end='2021-10-05')
dfREPMC.reset_index(inplace=True,drop=False)
dfBBVA = yf.download('BBVA', start='2021-09-24', end='2021-10-05')
dfBBVA.reset_index(inplace=True,drop=False)

print(dfSAN)
print(dfTEF)
print(dfREPMC)
print(dfBBVA)

varSAN = list(dfSAN.Open - dfSAN.Close) # Creo variables en donde almaceno una lista con la diferencia entre
varTEF = list(dfTEF.Open - dfTEF.Close) # los valores de la columna Open y Close
varREP = list(dfREPMC.Open - dfREPMC.Close)
varBBVA = list(dfBBVA.Open - dfBBVA.Close)
fecha = list(dfSAN.Date)

print(varSAN)
print(varTEF)
print(varREP)
print(varBBVA)
print(fecha)

data = {'Fecha': fecha,             #Creo un diccionario con las variables que cree asi despues formo el dataframe
    'Variacion Santander': varSAN,
    'Variacion Telefonica': varTEF,
    'Variacion Repsol': varREP,
    'Variacion BBVA': varBBVA,}


df = pd.DataFrame(data) #Creo el data frame tomando como parametro el diccionario anterior
print(df)

df.to_csv('Bolsayahoo.csv') #Creo el archivo CSV

for i in df.index: #Saco los valores Maximos y Minimos correspondientes a cada dia
    print("En la fecha "+ str(df["Fecha"][i])+ " la acción que tuvo la mejor variacion: "+str(df.max(axis = 1)[i]))
    print("En la fecha "+ str(df["Fecha"][i])+ " la acción que tuvo la peor variacion: "+str(df.min(axis = 1)[i]))

'''
cabecera = np.array(df.columns[2:]) #obtengo la cebacera (listado de columnas), desde la primera accion de interes o sea la tercera columna 
print('Cabeceras: ', cabecera)
df = pd.read_csv(f)

for i in df.index: #Saco los valores Maximos y Minimos correspondientes a cada dia
    acciones = np.array(df.iloc[i][2:])
    #print(acciones)
    vmax=acciones.max()
    vmin=acciones.min()
    accmax=cabecera[np.where(acciones==vmax)]
    accmin=cabecera[np.where(acciones==vmin)]
    print("En la fecha "+ str(df["Fecha"][i])+ " la mayor variacion fue ",vmax, "para ",accmax[0])
    print("En la fecha "+ str(df["Fecha"][i])+ " la menor variacion fue ",vmin, "para ",accmin[0])

'''