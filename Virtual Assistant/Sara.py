# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 12:36:48 2021

@author: facul
"""

import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer= WordNetLemmatizer()
import pickle
import numpy as np
from keras.models import load_model
model= load_model('engine_bot.h5')
import json
import random
import procesador


import funciones
import cuerpo


intents=json.loads(open('intents.json', encoding='utf-8').read())
words=pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))


y= True
x= True
while y == True:
    entrada = cuerpo.escucha()
    tag1=procesador.tag(entrada, model)
    if tag1 == "saludo":
        cuerpo.habla(procesador.chatbot_response(entrada))
        x=True
        while x == True:
            entrada = cuerpo.escucha()
            sara=procesador.chatbot_response(entrada)
            tag=procesador.tag(entrada, model)
            
            if tag == "despedida":
                cuerpo.habla(sara)
                break
            elif tag == "buenos_dias":
                cuerpo.habla(sara)
                funciones.buenos_dias()
            elif tag == "musica_ambiente":
                cuerpo.habla(sara)
                funciones.musica_ambiente()
            elif tag == "google":
                cuerpo.habla(sara)
                funciones.google()
            elif tag == "busca_google":
                cuerpo.habla(sara)
                busqueda = entrada
                funciones.busca_google(entrada)
            elif tag == "que_hora_es":
                funciones.que_hora_es()
            elif tag == "que_dia_es_hoy":
                funciones.que_dia_es_hoy()
            elif tag == "whatsapp":
                funciones.whatsapp()
            elif tag == "youtube":
                funciones.youtube()
            elif tag == "espacio_trabajo":
                cuerpo.habla(sara)
                funciones.espacio_trabajo()
            elif tag == "agradecimiento":
                cuerpo.habla(sara)
            elif tag == "correo":
                cuerpo.habla(sara)
                funciones.gmail()
            elif tag == "clima":
                funciones.clima()
            elif tag == "drive":
                cuerpo.habla(sara)
                funciones.drive()
            elif tag == "tomar_nota":
                cuerpo.habla(sara)
                entrada_nota = cuerpo.escucha()
                funciones.nota(entrada_nota)
                cuerpo.habla("Listo")
            elif tag == "programacion":
                cuerpo.habla(sara)
                funciones.programacion()

            else:
                cuerpo.habla(sara)
        






