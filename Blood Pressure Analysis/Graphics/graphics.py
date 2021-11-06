import plotly.express as px
import pandas
import numpy
"""
Como primer acercamiento, sabemos que la presión arterial aumenta con la edad y varía dependiendo el sexo por ende en base a esto graficaremos nuestros datos 
para tener un mejor entendimiento:
"""
df1=df.groupby(['Edad', 'Sexo'],as_index=False)['PA_max'].mean() 
# agrupamos en base a la edad y el sexo para tener por cada año de edad y el promedio de presion por genero
df1


fig_1 = px.scatter(df1, x=df1.Edad, y=df1.PA_max, color=df1.Sexo ,labels={"x": "Edad", "y": "Presion Arterial", "color": "Sexo" }, title="Edad-Sexo-PA_max promedios")
fig_1.show() # Graph_1

"""
[Podemos ver como a medida que aumenta la edad, los promedios de PA van creciendo por ende podemos confirmar que hay una relación directa entre Edad y PA.
Por otro lado podemos ver como no es tan notable una ralación entre el Sexo y la PA ya que los picos van variando entre M y F, no vemos una tendencia hacia ninguno de los Sexos.]
"""
"""
[Hacemos una analisis más detallado según la condición respecto a la Presion Arterial (Bajo - Normal - Alta - Hipertensión 1 - Hipertension 2 - Emergencia)]
"""
# we create intervals / creamos intervalos

intervalos_PA=[0,90,120,140,160,180,300]
etiquetas_PA=["Bajo", "Normal", "Alta", "Hipertensión-1", "Hipertensión-2", "Emergencia"]
df['Condicion-P']=pd.cut(df["PA_max"], intervalos_PA, labels=etiquetas_PA)

intervalos_Edad=[0,25,35,60,75,80]
etiquetas_Edad=["Joven", "Joven-Adulto", "Adulto", "Mayor", "Muy Mayor"]
df['Clasificación-E']=pd.cut(df["Edad"], intervalos_Edad, labels=etiquetas_Edad)

df

# groupping / agrupamos

df2=df.groupby(["Condicion-P", "Clasificación-E","Edad"],as_index=False)["PA_max"].count().sort_values(by="Edad", ascending=True)
df2=df2[(df2 != 0).all(1)].reset_index().drop("index", 1)
df2

# We create different data frames filtered by the condition of the person / Creamos diferentes data frames filtrados por la condición de la persona

bajo, normal, alta= df2.loc[df2["Condicion-P"] == "Bajo"],  df2.loc[df2["Condicion-P"] == "Normal"], df2.loc[df2["Condicion-P"] == "Alta"]
hipertension1 , hipertension2, emergencia= df2.loc[df2["Condicion-P"] == "Hipertensión-1"], df2.loc[df2["Condicion-P"] == "Hipertensión-2"], df2.loc[df2["Condicion-P"] == "Emergencia"]

# Our Plots / Nuestros gráficos

fig_2_1   = px.line(bajo, x=bajo.Edad, y=bajo.PA_max, title="Cantidad de casos con Presion Baja") # Graph_2_1
fig_2_2 = px.line(normal, x=normal.Edad, y=normal.PA_max, title="Cantidad de casos con Presion Normal") # Graph_2_2
fig_2_3 = px.line(alta, x=alta.Edad, y=alta.PA_max, title="Cantidad de casos con Presion Alta") # Graph_2_3
fig_2_4 = px.line(hipertension1, x=hipertension1.Edad, y=hipertension1.PA_max, title="Cantidad de casos con Hipertension Nivel 1") # Graph_2_4
fig_2_5 = px.line(hipertension2, x=hipertension2.Edad, y=hipertension2.PA_max, title="Cantidad de casos con Hipertension Nivel 2") # Graph_2_5
fig_2_6 = px.line(emergencia, x=emergencia.Edad, y=emergencia.PA_max, title="Cantidad de casos Emergencia") # Graph_2_6
"""
[Como añadido hay un parámetro en Plotly que te permite usar líneas para marcar áreas, en las gráficas las uso pero si las detallo aquí el código sería muy grande]
"""
fig_2_1.show()
fig_2_2.show()
fig_2_3.show()
fig_2_4.show()
fig_2_5.show()
fig_2_6.show()

"""
[Aquí a medida que vemos cada tipo de condición, vemos que la cantidad de casos es mayor para gente joven en casos de condiciones normales o bajas pero es mayor para gente 
grande a medida que las condiciones son críticas.]
"""

# Dispersion analysis / Analisis de Dispersión

fig_3_1 = px.box(df, x=df["Clasificación-E"], y=df["PA_max"],color=df["Sexo"]) # Graph_3_1
fig_3_1.show()

fig_3_2 = px.violin(df, y=df["PA_max"], x=df["Clasificación-E"], color=df["Sexo"], box=True, hover_data=df.columns) # Graph_3_2
fig_3_2.show()

"""
Como segundo acercamiento, veremos como la variable IMC podría afectar a la Presión Arterial. Viendo los graficos nos llama la atención como hay muchos jovenes con 
presión alta. Debemos recordar que aparte de la Edad, teníamos también variable como el Sexo y el IMC.
"""

# creamos un data frame agrupando por la condición de PA (la necesitaremos luego) y la PA_max. A esto le pedimos el promedio del IMC para cada caso
# We create a data frame grouping by the PA condition (we will need it later) and the PA_max. We ask this for the average IMC for each case.
df3=df.groupby(['Condicion-P','Edad','Sexo'],as_index=False)[['PA_max', 'IMC']].mean().sort_values(["Edad", "Condicion-P"], ascending=[True, True])
df3

# sub dividimos nuestro dataframe en pequeños dataframes según condición de IMC / we divide our dataframe into small dataframes according to IMC condition

bajo, normal, alta= df3.loc[df3["Condicion-P"] == "Bajo"],  df3.loc[df3["Condicion-P"] == "Normal"], df3.loc[df3["Condicion-P"] == "Alta"]
hipertension1 , hipertension2, emergencia= df3.loc[df3["Condicion-P"] == "Hipertensión-1"], df3.loc[df3["Condicion-P"] == "Hipertensión-2"], df3.loc[df3["Condicion-P"] == "Emergencia"]
hipertension2

fig_4_1 = px.scatter(bajo, x=bajo.IMC, y=bajo.PA_max, title="Promedio de IMC con Presion Baja") # Graph_4_1
fig_4_2 = px.scatter(normal, x=normal.IMC, y=normal.PA_max, title="Promedio de IMC con Presión normal" ) # Graph_4_2
fig_4_3 = px.scatter(alta, x=alta.IMC, y=alta.PA_max, title="Promedio de IMC con Presión Alta") # Graph_4_3
fig_4_4 = px.scatter(hipertension1, x=hipertension1.IMC, y=hipertension1.PA_max, title="Promedio de IMC con Hipertensión nivel 1") # Graph_4_4
fig_4_5 = px.scatter(hipertension2, x=hipertension2.IMC, y=hipertension2.PA_max, title="Promedio de IMC con Hipertensión nivel 2") # Graph_4_5
fig_4_6 = px.scatter(emergencia, x=emergencia.IMC, y=emergencia.PA_max, title="Promedio de IMC con presión Emergencia") # Graph_4_6

fig_4_1.show()
fig_4_2.show()
fig_4_3.show()
fig_4_4.show()
fig_4_5.show()
fig_4_6.show()

"""
Viendo detenidamente los graficos anteriores podemos ver como a medida que pasamos de grupo (condición) de menor a mayor PA, los casos van moviendose levemente de 
izquierda a derecha, es decir van creciendo la PA a medida que crece el IMC. Esto lo podemos notar clasamente en el último grafico de los casos de emergencia.

Si bien la relación es leve, podríamos afirmar que solemos encontrar más personas en estado de emergencia cuando estas tienen un IMC alto.
No nos podríamos basar únicamente en esta variable ya que la cantidad de casos de emergencia con un IMC normal también son muchos.
"""

"""
Como tercer acercamiento veremos si podemos ver alguna relación entre la Edad, IMC y la PA_max
"""
df4=df.groupby(['Sexo','Edad'],as_index=False)[['PA_max', 'IMC']].mean().sort_values(["Edad", "PA_max"], ascending=[True, True])

fig_5_1 = px.scatter_3d(df4, x=df4.Edad, y=df4.PA_max, z=df4.IMC, color=df4.Sexo, size_max=8, title="Relación Edad-IMC-Sexo Completo")
fig_5_1.show()

"""
CONCLUSIONES
        - Podemos confirmar que las variables IMC y Edad afectan a los valores de la Presión Arterial, al menos en nuestro conjunto de datos.
        - La variable Sexo no tiene un gran impacto ya que los valores de PA para Hombres y Mujeres no se sacan una gran diferencia.
        - La variable Edad tiene mucha más influencia en la Presión Arterial que el IMC, aunque el IMC también influye.
"""

# let's discover the relationships between the variables applying a scatter with regression method
# descubramos las relaciones entre las variables aplicando un scatter con método de regresión

df5 = df.groupby(['Edad', 'Sexo'],as_index=False)['PA_max'].mean() 
df6 = df.groupby(['PA_max', 'Sexo'],as_index=False)['IMC'].mean() 

df1_h = df1[(df1.Sexo=="M")]
df1_m = df1[(df1.Sexo=="F")]

fig_6_1 = px.scatter(df5, x=df1_h.Edad, y=df1_h.PA_max,labels={
                     "x": "Edad",
                     "y": "Presion Arterial"
                 },
                title="Edad-PA_max promedios Hombres", trendline="ols")

fig_6_2 = px.scatter(df5, x=df1_m.Edad, y=df1_m.PA_max,labels={
                     "x": "Edad",
                     "y": "Presion Arterial"
                 },
                title="Edad-PA_max promedios Mujeres", trendline="ols")

fig_6_1.show()
fig_6_2.show()
