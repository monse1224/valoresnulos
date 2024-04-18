import pandas as pd
import numpy as np

df=pd.read_excel("precios_productos.xlsx")
print(df.isnull().sum())
#no contiene nulos