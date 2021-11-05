import plotly.express as px
"""
Como primer acercamiento, sabemos que la presión arterial aumenta con la edad y varía dependiendo el sexo por ende en base a esto graficaremos nuestros datos 
para tener un mejor entendimiento:
"""
df1=df.groupby(['Edad', 'Sexo'],as_index=False)['PA_max'].mean() 
# agrupamos en base a la edad y el sexo para tener por cada año de edad y el promedio de presion por genero
df1


fig = px.scatter(df1, x=df1.Edad, y=df1.PA_max, color=df1.Sexo ,labels={"x": "Edad", "y": "Presion Arterial", "color": "Sexo" }, title="Edad-Sexo-PA_max promedios")
fig.show()

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

fig  = px.line(bajo, x=bajo.Edad, y=bajo.PA_max, title="Cantidad de casos con Presion Baja")
fig2 = px.line(normal, x=normal.Edad, y=normal.PA_max, title="Cantidad de casos con Presion Normal")
fig3 = px.line(alta, x=alta.Edad, y=alta.PA_max, title="Cantidad de casos con Presion Alta")
fig4 = px.line(hipertension1, x=hipertension1.Edad, y=hipertension1.PA_max, title="Cantidad de casos con Hipertension Nivel 1")
fig5 = px.line(hipertension2, x=hipertension2.Edad, y=hipertension2.PA_max, title="Cantidad de casos con Hipertension Nivel 2")
fig6 = px.line(emergencia, x=emergencia.Edad, y=emergencia.PA_max, title="Cantidad de casos Emergencia")
"""
As an addition, there is a parameter in Plotly that allows you to use lines to mark areas, in the graphs I use them but if I detail them here the code would be very large]
"""
fig.show()
fig2.show()
fig3.show()
fig4.show()
fig5.show()
fig6.show()

"""
[Aquí a medida que vemos cada tipo de condición, vemos que la cantidad de casos es mayor para gente joven en casos de condiciones normales o bajas pero es mayor para gente 
grande a medida que las condiciones son críticas.]
"""
