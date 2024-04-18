import pandas as pd
import numpy as np

df=pd.read_excel("clientes.xlsx")
#print(df.isnull().sum())

#rellenamos con la composición de caracteres que tiene una curp (18 digitos)
df['RFC'].fillna('XXXX-000000-X-XX-XXX-00', inplace=True) 
#print(df.isnull().sum())

#indicamos que no hay nombre en el campo, para no eliminar al cliente
df['NOMBRE'].fillna('Sin Nombre', inplace=True)
print(df.isnull().sum())

#Convertir DataFrame a CSV
df.to_csv('clientes_limpio.csv')
