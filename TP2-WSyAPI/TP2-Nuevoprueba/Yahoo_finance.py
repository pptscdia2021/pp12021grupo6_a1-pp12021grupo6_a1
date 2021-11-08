
import yfinance as yf
import pandas as pd
from matplotlib import pyplot as plt
from yahoofinancials import YahooFinancials
from Graficar import grafganper,traerdato


tickerStrings = ['SAN', 'TEF', 'REP.MC', 'BBVA']
acciones = ['SANTANDER', 'TELEFONICA', 'REPSOL', 'BBVA']
for ticker in tickerStrings:
    data = yf.download(ticker, group_by="Ticker", period='1d')
    data['ticker'] = ticker  # Agrego una columna con el nombre de los tickers
    data.to_csv(f'CSV/ticker_{ticker}.csv')  # creacion del CSV file

df1 = pd.read_csv('CSV/ticker_SAN.csv')
df2 = pd.read_csv('CSV/ticker_TEF.csv')
df3 = pd.read_csv('CSV/ticker_REP.MC.csv')
df4 = pd.read_csv('CSV/ticker_BBVA.csv')

data = pd.concat([df1, df2, df3, df4], ignore_index=True)
data

def varYahoo(ticker):
    data1 = YahooFinancials(ticker).get_current_change()
    return float(data1)

varYahoo = [varYahoo('SAN'),varYahoo('TEF'),varYahoo('REP.MC'),varYahoo('BBVA')]

data.insert(1, "Nombre", acciones)
data.insert(2, "Variacion", varYahoo)
print(data)

data.to_csv('CSV/Acciones_Yahoo.csv')

# Gráfico del valor de apertura de las acciones ultimos 5 dias.
bbva_df= traerdato('SAN','5d')
tel_df = traerdato('TEF','5d')
rep_df = traerdato('REP.MC','5d')
bbva_df = traerdato('BBVA','5d')

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
plt.savefig('PNG/AccionesOpenYahoo.png')

# Grafico de variaciones de precios actual
grafganper(data,'Variacion','Nombre',4,4)


