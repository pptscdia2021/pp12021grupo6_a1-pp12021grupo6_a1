import requests
import csv
import pandas as pd

class BolsaMadrid:
    def __init__(self, url, table): # Obtenemos todos los datos de la tabla de Bolsa de Madrid.
        self.url = url
        self.table_id = table
        self.csv = 'CSV/BolsaMadrid.csv'
        self.df = pd.read_html(url, attrs=self.table_id, thousands='.', decimal=',', flavor=None)[0]
        columnsName = ["Accion", "Cierre", "Variacion%", "Maximo", "Minimo", "Volumen", "Efectivo(miles €)", "Fecha", "Hora"]
        self.df.columns = columnsName
    
    def extraccion(self,acciones): # Hacemos la extraccion de las acciones que queremos obtener a partir de su nombre.
        df_list = list()
        for accion in list(acciones.split()):
            resultado = self.df.where(self.df.Accion == accion)
            resultado = resultado.dropna()
            df_list.append(resultado)
        self.df = pd.concat(df_list)
    
    def crearDF(self): # Creacion del Dataframe.
        return self.df
    
    def crearCSV(self): # Creacion del CSV.
        return self.df.to_csv('CSV/BolsaMadrid.csv')
    
    # Obtencion de las acciones con mayor variacion y menor variacion.
    def maxminVar(self,columna,cantidad,maxomin): # columna = 'Variacion%', cantidad = 2, maxomin = 'Max' o 'Min'.
        if maxomin.upper() == 'MAX':
            resultado = self.df.sort_values(columna, ascending=False)
        elif maxomin.upper() == 'MIN':
            resultado = self.df.sort_values(columna)
        else:
            print('Error')
        resultado = resultado.head(cantidad)[['Accion',columna]].reset_index(drop=True)
        return resultado

