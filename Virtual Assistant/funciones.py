# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 15:41:20 2021

@author: facul
"""
import datetime
import requests
import json
from datetime import date
import cuerpo
import procesador
import webbrowser
import random
import datetime
import time
import pywhatkit
import subprocess



musica_de_ambiente = ["https://www.youtube.com/watch?v=bmVKaAV_7-A", "https://www.youtube.com/watch?v=rPt79QYxXEc&t=1028s", 
"https://www.youtube.com/watch?v=5qap5aO4i9A", "https://www.youtube.com/watch?v=DWcJFNfaw9c", "https://www.youtube.com/watch?v=CfPxlb8-ZQ0"]


def buenos_dias(): 
    # as i am from Córdoba, this function returns my city weahter
    # cómo soy de Córdoba, esta función me devuelve el clima de mi ciudad
    import time
    cuerpo.habla("Actualmente son las" + str(datetime.datetime.now().strftime("%I:%M %p")))
    user_api = "Complete con su API key"
    location = "Córdoba"
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()
    if api_data["cod"] == "404":
        print("Invalid city: {}, Please check your city name.".format(location))
    else:
        temp_city = ((api_data['main']['temp']) - 273.15)
        weather_desc = api_data['weather'][0]['description']
        hmdt = api_data['main']['humidity']
        wind_spd = api_data['wind']['speed']
        date_time = datetime.datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
        print ("-------------------------------------------------------------")
        print ("Clima en Córdoba - {}  || {}".format(location.upper(), date_time))
        print ("-------------------------------------------------------------")
        cuerpo.habla ("Temperatura actual en córdoba: {:.2f} deg C".format(temp_city))
        cuerpo.habla ("Clima actual          :" + weather_desc)
        print ("Humedad actual        :",hmdt, '%')
        print ("Velocidad del viento actual    :",wind_spd ,'kmph')
def musica_ambiente():
	webbrowser.open(random.choice(musica_de_ambiente))

def google():
    webbrowser.open("https://www.google.com/")

def que_hora_es():
    time = datetime.datetime.now().strftime("%I:%M %p")
    cuerpo.habla("Son las " + str(time))

def que_dia_es_hoy():
    dia=(datetime.datetime.now().strftime("%d"))
    mes=(datetime.datetime.now().strftime("%B"))
    # as i speak spanish, i needed to get the month in Spanish
    # paso el mes a español
    if mes[0:4] == "Janu":
        mes_español= "Enero"
    elif mes[0:4] == "Febr":
        mes_español= "Febrero"
    elif mes[0:4] == "Marc":
        mes_español= "Marzo"
    elif mes[0:4] == "Apri":
        mes_español= "Abril"
    elif mes[0:3] == "May":
        mes_español= "Mayo"
    elif mes[0:4] == "June":
        mes_español= "Junio"
    elif mes[0:4] == "July":
        mes_español= "Julio"
    elif mes[0:4] == "Augu":
        mes_español= "Agosto"
    elif mes[0:4] == "Sept":
        mes_español= "Septiembre"
    elif mes[0:4] == "Octo":
        mes_español= "Octubre"
    elif mes[0:4] == "Nove":
        mes_español= "Noviembre"
    elif mes[0:4] == "Dece":
        mes_español= "Diciembre"
    cuerpo.habla("Hoy es " + dia + "de " + mes_español)
    
def whatsapp():
    webbrowser.open("https://web.whatsapp.com/")
    
def youtube():
    webbrowser.open("https://www.youtube.com/")
def espacio_trabajo():
    webbrowser.open("https://www.notion.so/")
    
def busca_google(busqueda):
    busqueda = busqueda.replace("busca en google", " ")
    pywhatkit.search(busqueda)
    
def gmail():
    webbrowser.open("https://mail.google.com")

def drive():
    webbrowser.open("https://drive.google.com")
    
def clima():
    import time
    user_api = "Ingresa tu Key acá"
    location = "Córdoba"
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()
    if api_data["cod"] == "404":
        print("Invalid city: {}, Please check your city name.".format(location))
    else:
        temp_city = ((api_data['main']['temp']) - 273.15)
        weather_desc = api_data['weather'][0]['description']
        hmdt = api_data['main']['humidity']
        wind_spd = api_data['wind']['speed']
        date_time = datetime.datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
        print ("-------------------------------------------------------------")
        print ("Clima en Córdoba - {}  || {}".format(location.upper(), date_time))
        print ("-------------------------------------------------------------")
        cuerpo.habla ("Temperatura actual en córdoba: {:.2f} deg C".format(temp_city))
        cuerpo.habla ("Clima actual          :" + weather_desc)
        print ("Humedad actual        :",hmdt, '%')
        print ("Velocidad del viento actual    :",wind_spd ,'kmph')
        
def nota(text):
 	date = datetime.datetime.now()
 
 	file_name =str(date).replace(":", "-") + "-note.txt"
 	with open(file_name, "w") as s:
 		s.write(text)
 	subprocess.Popen(["notepad.exe", file_name])

def programacion():
	webbrowser.open("https://github.com/")
	webbrowser.open("https://stackoverflow.com/")
	webbrowser.open("https://www.kaggle.com/")
    
    
    

