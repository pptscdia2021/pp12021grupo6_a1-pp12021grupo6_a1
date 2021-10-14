import yfinance as yf
import pandas as pd
import csv as csv


BancoSantanderSA = yf.Ticker("SAN")
print(BancoSantanderSA.info) 

#Solicito e imprimo datos que aparecen indetificados arriba

print("El precio de compra es: ", BancoSantanderSA.info['ask']) #Precio de compra acción
print("El precio de venta es: ", BancoSantanderSA.info['bid']) #Precio de venta acción


Telefonica = yf.Ticker ("TEF")
print(Telefonica.info)

print ("El precio de compra es: ",Telefonica.info['ask'])
print ("El precio de venta es: ",Telefonica. info['bid'])

Repsol = yf.Ticker ("REP.MC")
print(Repsol.info)

print ("El precio de compra es: ", Repsol.info['ask'])
print ("El precio de venta es: ",Repsol. info['bid'])

BancoBBVA = yf.Ticker ("BBVA")
print(BancoBBVA.info)

print ("El precio de compra es: ", BancoBBVA.info['ask'])
print ("El precio de venta es: ", BancoBBVA. info['bid'])

tickers = ["SAN", "TEF", "REP.MC", "BBVA"]
df = yf.download(tickers, start='2021-10-01', end='2021-10-07', group_by="ticker")
print(df)

#Cotización de BancoSantanderSA del dóa 24/09/2021
print(df.SAN)

#Cotización de TELEFONICA del dóa 24/09/2021
print(df.TEF)

#Cotización de BBVA del dóa 24/09/2021
print(df.BBVA)

#Cotización de REPSOL del dóa 24/09/2021
#print(df.REP.MC)#NO LO PUDO HACER CORRER CON ESTAS SIGLAS


#Visualizo si el dataframe esta en tabla
df.head()

#Tipo de dato
type(df.SAN)

type(df.TEF)
type(df.BBVA)
#type(df.REP.MC)

#Exporto a formato CSV



#Elijo que mi formato sea utf-8 para que se pueda leer bien en cualquier sistema operativo
df.to_csv("yahoofinance1.csv", encoding= "utf-8") #veo que el archivo que genera lo duplica, no entiendo como corregirlo


#dfyahoo=pd.read_csv('yahoofinance.csv')
#df['Open'] = df['Open'].apply(lambda x: x.replace(',','.'))

#df['Open'] = df['Open'].astype(float)
#maxs = dfyahoo['Open'].max()
#min= dfyahoo['Open'].min()

#print (df)
#pd.options.display.max_columns = None # comando para que en pandas me muestre todas las columnas y no me aparezcan puntos suspensivos al medio
#pd.set_option("max_rows", None)

'''
#Gráfico banco santander 1 año

ticker = yf.Ticker('SAN')
aapl_df = ticker.history(period="1y")
aapl_df['Close'].plot(title="SAN's stock price")

#GRÁFICO telefónica

ticker = yf.Ticker('TEF')
aapl_df = ticker.history(period="1y")
aapl_df['Close'].plot(title="TEF's stock price")

#GRÁFICO BANCO SANTANDER

ticker = yf.Ticker('BBVA')
aapl_df = ticker.history(period="1y")
aapl_df['Close'].plot(title="BBVA's stock price")

#GRÁFICO REPSOL

ticker = yf.Ticker('REP.MC')
aapl_df = ticker.history(period="1y")
aapl_df['Close'].plot(title="REP.MC's stock price")





df = yf.download("AMZN TEF", start="2021-09-03", end="2021-09-04",group_by="ticker") 
print(df)
de = yf.download("REP.MC BBVA", start="2021-09-03", end="2021-09-04",group_by="ticker") 
print(de)
'''

"""ticker = ["AAPL", "IBM", "TSLA"]
start = dt.datetime(2019, 1, 1)
end = dt.datetime(2020, 12, 31)

data = pdr.get_data_yahoo(ticker, start, end)

print(data)
"""





'''
with open('bolsa_yahoo.csv', 'a') as csv_file2:
    writer = csv.writer(csv_file2)
'''
