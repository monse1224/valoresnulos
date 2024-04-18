import pandas as pd
import numpy as np

df=pd.read_excel("devoluciones.xlsx")
#print(df.isnull().sum())

#ingresamos el formato de una fecha inexistente para indicar fecha invalida.
df['FECHA_CANCELA'].fillna('00/00/0000  00:00:00 x. x.', inplace=True) 
#print(df.isnull().sum())

#rellenamos con el formato o composición de datos que contiene la columna, para identificarlo como inexistente
df['DOC_ANT'].fillna('X00000', inplace=True) 
print(df.isnull().sum())

#Convertir DataFrame a CSV
df.to_csv('devoluciones_limpio.csv')
