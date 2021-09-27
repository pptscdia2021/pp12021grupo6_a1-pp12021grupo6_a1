import yfinance as yf
import pandas as pd


BancoSantanderSA = yf.Ticker("SAN")
print(BancoSantanderSA.info) 

print(BancoSantanderSA.info['ask']) #Precio de compra acción
print(BancoSantanderSA.info['bid']) #Precio de venta acción

Telefonica = yf.Ticker ("TEF")
print(Telefonica.info)

print (Telefonica.info['ask'])
print (Telefonica. info['bid'])

Repsol = yf.Ticker ("REP.MC")
print(Repsol.info)

print (Repsol.info['ask'])
print (Repsol. info['bid'])

BancoBBVA = yf.Ticker ("BBVA")
print(BancoBBVA.info)

print (BancoBBVA.info['ask'])
print (BancoBBVA. info['bid'])



tickers = ["SAN", "TEF", "REP.MC", "BBVA"]
df = yf.download(tickers, start='2021-09-24', end='2021-09-26')
print(df)

# Problema en Generar el CSV


'''
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
