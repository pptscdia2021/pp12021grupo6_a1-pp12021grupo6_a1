
import matplotlib.pyplot as plt
import yfinance as yf

#Traer datos de Yahoo por ticket y periodo
def traerdato(ticker,period):
    nombre = yf.download(ticker,group_by="ticker", period=period)
    return nombre

# Grafico de comparacion de 2 bolsas.
def grafcompar(dataf1,dataf2,columnavariacion,columnanombre,ancho,largo):
    data1=dataf1[columnavariacion]
    data2=dataf2[columnavariacion]
    

    macciones=dataf1[columnanombre]
    yacciones =dataf2[columnanombre]

    fig,ax=plt.subplots(2,1,figsize=(ancho,largo))

    ax[0].bar(macciones,data1,color='purple')
    ax[0].legend(['Bolsa de Madrid'])
    ax[1].bar(yacciones,data2,color='orange')
    ax[1].legend(['Yahoo Finance'])

    for ax in ax.flat:
        ax.set(xlabel = 'ACCIONES', ylabel='VARIACIÓN')
    

    plt.show()


def grafganper(df, columnaVariacion, columnaNombre, ancho, alto): #(dataframe,ColumnaejeY,ColumnaejeX,Anchodegrafico,Altodegrafico)
    
    y = df[columnaVariacion]
    x = df[columnaNombre]

    plt.figure(figsize=(ancho,alto))
    

    valp = df[columnaVariacion] < 0
    valg = df[columnaVariacion] >= 0


    ma=plt.barh(x, y, valg, color='#0000ff', label='Ganancia')
    mb=plt.barh(x, y, valp, color='#ff0000', label='Pérdida')

    plt.ylabel('ACCIONES')
    plt.xlabel('VARIACIÓN')
    plt.title('VARIACIÓN DE LAS ACCIONES')
    plt.legend()

    return plt.show()


