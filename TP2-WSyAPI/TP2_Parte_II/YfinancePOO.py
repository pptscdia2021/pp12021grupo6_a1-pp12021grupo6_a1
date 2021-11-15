import yfinance as yf
import pandas as pd
from yahoofinancials import YahooFinancials # Trabajamos con libreria Yahoo financials para traer la variación % de cada acción.


class Yfinance:
    def __init__(self,tickers):
        acciones = ['SANTANDER', 'TELEFONICA', 'REPSOL', 'BBVA']
        datetickers = []
        var = []
        for ticker in list(tickers.split()):
            data = yf.download(ticker, group_by="ticker", period='1d')
            data['ticker'] = ticker  # Agrego una columna con el nombre de los tickers
            datetickers.append(data)
            data_1 = YahooFinancials(ticker).get_current_percent_change() # Traemos la variación porcentual de la acción.
            var.append(round(float(data_1*100),3))
        self.tickers = pd.concat(datetickers)
        self.tickers = self.tickers.reset_index()
        colNombre = ["Fecha", "Apertura", "Maximo", "Minimo", "Ajuste", "Cierre", "Volumen", "Ticker"]
        self.tickers.columns = colNombre
        self.tickers.insert(1, 'Accion', acciones)
        self.tickers.insert(2, 'Variacion%', var)
    
    def crearDF(self): # Creacion del Dataframe.
        return self.tickers
    
    def crearCSV(self): # Creacion del CSV.
        return self.tickers.to_csv('TP2-WSyAPI/TP2_Parte_II/CSV/Yahoo.csv')
        
    # Obtencion de las acciones con mayor variacion y menor variacion.
    def maxminVar(self,columna,cantidad,maxomin): # columna = 'Variacion%', cantidad = 2, maxomin = 'Max' o 'Min'.
        if maxomin.upper() == 'MAX':
            resultado = self.tickers.sort_values(columna, ascending=False)
        elif maxomin.upper() == 'MIN':
            resultado = self.tickers.sort_values(columna)
        else:
            print('Error')
        resultado = resultado.head(cantidad)[['Accion',columna]].reset_index(drop=True)
        return resultado
