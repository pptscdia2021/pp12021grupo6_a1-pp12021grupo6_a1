# Se importan las librerías necesarias para la Comparación
import matplotlib.pyplot as plt
import pandas as pd
from Graficar import grafcompar


bMadrid = pd.read_csv('TP2-WSyAPI/TP2-Nuevoprueba/CSV/bolsa_4acciones.csv')
bYahoo = pd.read_csv('TP2-WSyAPI/TP2-Nuevoprueba/CSV/Acciones_Yahoo.csv')

#se importa función de Graficar.py para comparar ambas extracciones Bolsa Madrid y Yahoo finance
grafcompar(bMadrid,bYahoo,'Variacion','Nombre',8,8)

# Maximos y minimos de Bolsa de Madrid
bolsaMadrid = bMadrid.sort_values('Variacion')
print(bolsaMadrid)
minGanancia = [bolsaMadrid['Variacion'][0],bolsaMadrid['Variacion'][1]]
maxGanancia = [bolsaMadrid['Variacion'][2],bolsaMadrid['Variacion'][3]]
AccionMinGanancia = [bolsaMadrid['Nombre'][0],bolsaMadrid['Nombre'][1]]
AccionMaxGanancia = [bolsaMadrid['Nombre'][2],bolsaMadrid['Nombre'][3]]

print(f'Las 2 mejores variaciones fueron las acciones: {AccionMaxGanancia[0]} y {AccionMaxGanancia[1]} con las variaciones {maxGanancia[0]} y {maxGanancia[1]}')
print(f'Las 2 peores variaciones fueron las acciones: {AccionMinGanancia[0]} y {AccionMinGanancia[1]} con las variaciones {minGanancia[0]} y {minGanancia[1]}')

# Maximos y minimos de Yahoo Finance
bolsaYahoo = bYahoo.sort_values('Variacion')
print(bolsaYahoo)
minGanancia1 = [bolsaYahoo['Variacion'][0],bolsaYahoo['Variacion'][1]]
maxGanancia1 = [bolsaYahoo['Variacion'][2],bolsaYahoo['Variacion'][3]]
AccionMinGanancia1 = [bolsaYahoo['Nombre'][0],bolsaYahoo['Nombre'][1]]
AccionMaxGanancia1 = [bolsaYahoo['Nombre'][2],bolsaYahoo['Nombre'][3]]

#Se imprimen dos mejores y peores variaciones de acciones de ambas bolsas por  cada accion
print(f'Las 2 mejores variaciones fueron las acciones: {AccionMaxGanancia1[0]} y {AccionMaxGanancia1[1]} con las variaciones {maxGanancia1[0]} y {maxGanancia1[1]}')
print(f'Las 2 peores variaciones fueron las acciones: {AccionMinGanancia1[0]} y {AccionMinGanancia1[1]} con las variaciones {minGanancia1[0]} y {minGanancia1[1]}')