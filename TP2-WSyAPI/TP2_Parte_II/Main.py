from BolsaMadridPOO import BolsaMadrid as bs
from YfinancePOO import Yfinance as yf
from GraficosPOO import Graficos as gf
import pandas as pd

if __name__ == "__main__":
    url = "https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000"
    table = {"id":"ctl00_Contenido_tblAcciones"}
    acciones = 'B.SANTANDER TELEFONICA REPSOL BBVA'

    bMadrid = bs(url,table)
    data = bMadrid.extraccion(acciones)
    data = bMadrid.crearDF()
    print('----{0}----'.format('BolsaDeMadrid'))
    print(bMadrid.maxminVar('Variacion%',2,'max'))
    print(bMadrid.maxminVar('Variacion%',2,'min'))
    bMadrid.crearCSV()

    tickers = 'SAN.MC TEF.MC REP.MC BBVA.MC'
    datayf = yf(tickers)
    data1 = datayf.crearDF()
    datayf.crearCSV()
    print('----{0}----'.format('YahooFinance'))
    print(datayf.maxminVar('Variacion%',2,'max'))
    print(datayf.maxminVar('Variacion%',2,'min'))

    graf = gf(data,data1)
    graf.graficar()
