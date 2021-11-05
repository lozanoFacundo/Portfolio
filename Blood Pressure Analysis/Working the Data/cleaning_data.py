# import the main libraries / importamos las principales bibilotecas

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("data.csv", sep=';')
df

df.info() 

"""
[ Se puede observar que los valores de altura y PA_max son objetos, esto es porque estan separados por coma y no por punto. 
Por lo tanto, como primera medida se debera cambiar la coma, para esto se cargan nuevamente los datos considerando que el separador decimal es la coma.]
"""
df = pd.read_csv("data.csv", sep = ';', decimal=",")  # now it shoud work well / ahora debería andar bien
df.info()

# Let's take a statistical look at the data / Demosle una mirada estadística a los datos

df.describe(include = 'all')

"""
[Teniendo en cuenta que se poseen muchas observaciones y que existen datos faltantes en altura y sexo se prodecera a eliminar estas observaciones. 
(Si no tuvieramos tantos datos deberíamos rescatarlos utilizando "from sklearn.impute import SimpleImputer" pero no es el objetivo del análisis)]
"""

df = df.dropna()
df.describe(include = 'all') # we still have to work this data / todavía debemos trabajar estos datos

"""
[Tambien se tienen algunas observaciones con el valor cero en la columna de peso, tambien se procedera a eliminar estas observaciones. 
Para ellos se filtran los valores del peso que no son iguales al peso y se re-escribe el df.]
"""
df = df[~(df['Peso'] == 0)] # we still have to work this data / todavía debemos trabajar estos datos
df

"""
[Existen valores irregulares en diferentes columnas como en altura que hay valores mayores a 100 metros por la falta de un separador decimal, 
tambien con el peso, hay personas con mas de 1000kg y valores de presion arterial expresados en cm y mm. Arreglamos estos valores para tener las 
columnas con valores uniformes.]
"""
df['Altura'] = np.where(df.Altura > 100, round(df.Altura/100, 2), round(df.Altura, 2))
df['Peso'] = np.where(df.Peso > 1000, round(df.Peso/1000, 2), round(df.Peso, 2))
df["PA_max"]= np.where(df.PA_max < 33, df.PA_max *10, df.PA_max)
df

"""
[Por último, podemos reducir la dimensionalidad de nuestros datos creando una nueva variable IMC que relaciona la altura con el peso y que nos brinda mayor exactitud 
al utilzarla frente a la presion arterial.]
"""
df['IMC'] = round(df['Peso'] / (df['Altura'] ** 2), 2)
df=df.drop(["Altura", "Peso"], axis=1)

df.describe() # now we are good to go / ahora si ya estamos listos





