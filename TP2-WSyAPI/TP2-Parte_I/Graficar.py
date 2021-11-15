
# Se importan librerias necesarias para generar gráficos
import matplotlib.pyplot as plt
import yfinance as yf

# Se traen datos de Yahoo por ticket y periodo
def traerdato(ticker,period):
    nombre = yf.download(ticker,group_by="ticker", period=period)
    return nombre

# Función de gráfico de comparacion de 2 bolsas.
def grafcompar(dataf1,dataf2,columnavariacion,columnanombre,ancho,largo):
    data1=dataf1[columnavariacion]
    data2=dataf2[columnavariacion]
    
    macciones=dataf1[columnanombre]
    yacciones =dataf2[columnanombre]

    # Se configura tamaño del gráfico
    fig,ax=plt.subplots(2,1,figsize=(ancho,largo))

    # Se configura colores para cada mercado y así visualizar la diferencia
    ax[0].bar(macciones,data1,color='purple')
    ax[0].legend(['Bolsa de Madrid'])
    ax[1].bar(yacciones,data2,color='orange')
    ax[1].legend(['Yahoo Finance'])

    # Se recorre la figura para configurar etiquetas de gráfico
    for ax in ax.flat:
        ax.set(xlabel = 'ACCIONES', ylabel='VARIACIÓN')
    
    # Se muestra el gráfico
    plt.show()

# Se define función para graficar ganancias y pérdidas 
def grafganper(df, columnaVariacion, columnaNombre, ancho, alto): #(dataframe,ColumnaejeY,ColumnaejeX,Anchodegrafico,Altodegrafico)
    
    y = df[columnaVariacion]
    x = df[columnaNombre]

    plt.figure(figsize=(ancho,alto))
    

    valp = df[columnaVariacion] < 0
    valg = df[columnaVariacion] >= 0

    # Se configuran colores del gráfico
    ma=plt.barh(x, y, valg, color='#0000ff', label='Ganancia')
    mb=plt.barh(x, y, valp, color='#ff0000', label='Pérdida')

    # Se configuran etiquetas para el gráfico
    plt.ylabel('ACCIONES')
    plt.xlabel('VARIACIÓN')
    plt.title('VARIACIÓN DE LAS ACCIONES')
    plt.legend()

    # Devuelve mostrar el gráfico
    return plt.show()


