import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

class Graficos():
    def __init__(self,df1,df2): #Recibe dos dataframes
        self.df1 = df1
        self.df2 = df2
        

    def graficar(self):   
        var = self.df1['Variacion%']
        nom = self.df1['Accion']
        var1 = self.df2['Variacion%']
        nom1 = self.df2['Accion']
        fig,ax = plt.subplots(1,2,figsize=(15,9))

        barras = ax[0].bar(nom,var,width=1,ec='black',color='green')
        for barra in barras:
            height = barra.get_height()
            ax[0].annotate(round(barra.get_height(),2), xytext= (0,-8),color= 'black',xy=(barra.get_x() + barra.get_width() /2, height),textcoords= 'offset pixels', ha='center',va='top')
            ax[0].annotate(u'Máximo', xy = (np.argmax(var), np.max(var)), xycoords = 'data', xytext = (np.argmax(var) - 0.8, np.max(var) + 0.2), textcoords = 'data', arrowprops = dict(arrowstyle = "->"))
            ax[0].annotate(u'Mínimo', xy = (np.argmin(var), np.min(var)), xycoords = 'data', xytext = (np.argmin(var) + 0.8, np.min(var) + 0.4), textcoords = 'data', arrowprops = dict(arrowstyle = "->"))
            if height <0:
                barra.set_color('red')
                barra.set_edgecolor('black')
        ax[0].set_ylabel('VARIACIÓN')
        ax[0].set_xlabel('ACCIONES')
        ax[0].grid(color = 'grey', linestyle = '--', linewidth = 0.9)

        barras1 = ax[1].bar(nom1,var1,width=1,ec='black',color='green')
        for barra in barras1:
            height = barra.get_height()
            ax[1].annotate(round(barra.get_height(),2), xytext= (0,-8),color= 'black',xy=(barra.get_x() + barra.get_width() /2, height),textcoords= 'offset pixels', ha='center',va='top')
            ax[1].annotate(u'Máximo', xy = (np.argmax(var), np.max(var)), xycoords = 'data', xytext = (np.argmax(var) - 0.8, np.max(var) + 0.2), textcoords = 'data', arrowprops = dict(arrowstyle = "->"))
            ax[1].annotate(u'Mínimo', xy = (np.argmin(var), np.min(var)), xycoords = 'data', xytext = (np.argmin(var) + 0.8, np.min(var) + 0.4), textcoords = 'data', arrowprops = dict(arrowstyle = "->"))
            if height <0:
                barra.set_color('red')
                barra.set_edgecolor('black')
        ax[1].set_ylabel('VARIACIÓN')
        ax[1].set_xlabel('ACCIONES')
        ax[1].grid(color = 'grey', linestyle = '--', linewidth = 0.9)


        plt.suptitle('BOLSA DE MADRID & YAHOO FINANCE',y=1)

        plt.tight_layout()

        return plt.show()



