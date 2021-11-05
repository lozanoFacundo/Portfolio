# import the main libraries
# importamos las principales bibilotecas

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("data.csv", sep=';')
df

df.info() 

"""
It can be seen that the height and PA_max values are objects, this is because they are separated by a comma and not by a period. 
Therefore, as a first measure, the comma should be changed, for this the data is loaded again considering that the decimal separator is the comma

"""

