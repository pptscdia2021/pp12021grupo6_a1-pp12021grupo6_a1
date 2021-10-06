import pandas as pd

df=pd.read_csv('bolsa_acciones.csv')

df['Variacion'] = df['Variacion'].apply(lambda x: x.replace(',','.'))

df['Variacion'] = df['Variacion'].astype(float)

#print(df.sort_values(by=['Variacion']))

maxs = df['Variacion'].max()
min= df['Variacion'].min()

print("Maximo de Variación:")
print(maxs)
print("Mínimo de Variación:")
print(min)
