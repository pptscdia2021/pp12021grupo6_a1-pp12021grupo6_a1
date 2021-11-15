# Se importan las librerias necesarias para extraer datos por API a Yahoo Finance
import yfinance as yf
import pandas as pd
from matplotlib import pyplot as plt
from yahoofinancials import YahooFinancials
from Graficar import grafganper,traerdato

# Mediante lista, se lista el nombre de acciones a extraer desde yfinance
tickerStrings = ['SAN', 'TEF', 'REP.MC', 'BBVA']
acciones = ['SANTANDER', 'TELEFONICA', 'REPSOL', 'BBVA']
for ticker in tickerStrings:
    data = yf.download(ticker, group_by="Ticker", period='1d')
    data['ticker'] = ticker  # Agrego una columna con el nombre de los tickers
    data.to_csv(f'TP2-WSyAPI/TP2-Nuevoprueba/CSV/ticker_{ticker}.csv')  # creacion del CSV file

# Se leen los csv's generados por cada acción para convertirlo en dataframes diferentes
df1 = pd.read_csv('TP2-WSyAPI/TP2-Nuevoprueba/CSV/ticker_SAN.csv')
df2 = pd.read_csv('TP2-WSyAPI/TP2-Nuevoprueba/CSV/ticker_TEF.csv')
df3 = pd.read_csv('TP2-WSyAPI/TP2-Nuevoprueba/CSV/ticker_REP.MC.csv')
df4 = pd.read_csv('TP2-WSyAPI/TP2-Nuevoprueba/CSV/ticker_BBVA.csv')

# Se concatenan los df de cada acción y se guarda en otra variable
data = pd.concat([df1, df2, df3, df4], ignore_index=True)
data

# Se define función para que retorne los datos en tipo float
def varYahoo(ticker):
    data1 = YahooFinancials(ticker).get_current_change()
    return float(data1)

# Se utilza función varYahoo para cada acción
varYahoo = [varYahoo('SAN'),varYahoo('TEF'),varYahoo('REP.MC'),varYahoo('BBVA')]

data.insert(1, "Nombre", acciones)
data.insert(2, "Variacion", varYahoo)
print(data)

# Se convierte df data a csv
data.to_csv('TP2-WSyAPI/TP2-Nuevoprueba/CSV/Acciones_Yahoo.csv')

# Gráfico del valor de apertura de las acciones ultimos 5 dias.
bbva_df= traerdato('SAN','5d')
tel_df = traerdato('TEF','5d')
rep_df = traerdato('REP.MC','5d')
bbva_df = traerdato('BBVA','5d')

# Se configura gráfico de matplotlib para cada acción de los últimos 5 días
plt.figure(figsize=(12,10))
plt.subplot(2,2,1)
bbva_df['Open'].plot(title="SANTANDER", marker="d", color='#01b8aa', label="Valor apertura acción");
plt.xlabel('DÍAS',fontsize=10)
plt.ylabel('VALOR',fontsize=10)
plt.legend()

plt.subplot(2,2,2)
tel_df['Open'].plot(title="TELEFÓNICA", marker="d",color='#01b8aa', label="Valor apertura acción");
plt.xlabel('DÍAS',fontsize=10)
plt.ylabel('VALOR',fontsize=10)
plt.legend()

plt.subplot(2,2,3)
rep_df['Open'].plot(title="REPSOL", marker="d", color='#01b8aa', label="Valor apertura acción");
plt.xlabel('DÍAS',fontsize=10)
plt.ylabel('VALOR',fontsize=10)
plt.legend()

plt.subplot(2,2,4)
bbva_df['Open'].plot(title="BBVA", marker="d",color='#01b8aa', label="Valor apertura acción");
plt.xlabel('DÍAS',fontsize=10)
plt.ylabel('VALOR',fontsize=10)
plt.legend()
plt.tight_layout()
plt.savefig('TP2-WSyAPI/TP2-Nuevoprueba/PNG/AccionesOpenYahoo.png')

# Grafico de variaciones de precios actual
grafganper(data,'Variacion','Nombre',4,4)


