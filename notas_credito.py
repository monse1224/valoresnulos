import pandas as pd
import numpy as np

df=pd.read_excel("notas_credito.xlsx")
#print(df.isnull().sum())

#Rellenamos los registros vacíos con 0, porque los registros tienen un valor númerico
df['CVE_VEND'].fillna(0, inplace=True)
#print(df.isnull().sum())

#rellenamos con guiones para indicar serie de pedido inexistente
df['CVE_PEDI'].fillna('--', inplace=True)
#print(df.isnull().sum())

#ingresamos el formato de una fecha inexistente para indicar fecha invalida.
df['FECHA_CANCELA'].fillna('00/00/0000  00:00:00 x. x.', inplace=True) 
print(df.isnull().sum())

#Convertir DataFrame a CSV
df.to_csv('notas_credito_limpio.csv')