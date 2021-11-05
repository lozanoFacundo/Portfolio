# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 14:27:49 2021

@author: facul
"""
import playsound
import os
from gtts import gTTS
import random
import procesador
import speech_recognition as sr
from keras.models import load_model
model= load_model('engine_bot.h5')

def habla(text):
	tts = gTTS(text=text, lang="es")
	r1 = random.randint(1,10000000)
	r2 = random.randint(1,10000000)
	filename = str(r2)+"randomtext"+str(r1) +".mp3"  
	tts.save(filename)
	playsound.playsound(filename)
	os.remove(filename)
    
def escucha():
    escuchando = sr.Recognizer()
    y=True
    while y == True:
        try:
            with sr.Microphone() as source:
            	print("Escuchando...")
            	escuchando.adjust_for_ambient_noise(source, duration=0.2)
            	voice = escuchando.listen(source)
            	entrada = escuchando.recognize_google(voice, language="es-AR")	
            	entrada = entrada.lower()
            y = False
        except sr.UnknownValueError:
            pass
    print("----------------------------------------------------------------")
    print("Tag: " + procesador.tag(entrada, model))
    print("Probability: " + procesador.probability(entrada, model))
    print("Entrada: " + entrada)
    print("----------------------------------------------------------------")
    return entrada