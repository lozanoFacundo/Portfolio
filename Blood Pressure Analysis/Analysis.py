# import the main libraries / importamos las principales bibilotecas

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("data.csv", sep=';')
df

df.info() 

"""
[ It can be seen that the height and PA_max values are objects, this is because they are separated by a comma and not by a period. 
Therefore, as a first measure, the comma should be changed, for this the data is loaded again considering that the decimal separator is the comma. ]

[ Se puede observar que los valores de altura y PA_max son objetos, esto es porque estan separados por coma y no por punto. 
Por lo tanto, como primera medida se debera cambiar la coma, para esto se cargan nuevamente los datos considerando que el separador decimal es la coma.]

"""
df = pd.read_csv("data.csv", sep = ';', decimal=",")  # now it shoud work well / ahora debería andar bien
df.info()

# Let's take a statistical look at the data / Demosle una mirada estadística a los datos

df.describe(include = 'all')

"""
[ Taking into account that there are many observations and that there are missing data on height and sex, we will proceed to eliminate these observations. 
(If we do not have so much data we should rescue it using "from sklearn.impute import SimpleImputer" but it is not the objective of the analysis) ]

[Teniendo en cuenta que se poseen muchas observaciones y que existen datos faltantes en altura y sexo se prodecera a eliminar estas observaciones. 
(Si no tuvieramos tantos datos deberíamos rescatarlos utilizando "from sklearn.impute import SimpleImputer" pero no es el objetivo del análisis)]

"""




