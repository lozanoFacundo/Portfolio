# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 11:36:03 2021

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


import speech_recognition as sr
import playsound
import os
from gtts import gTTS
import random

intents=json.loads(open('intents.json', encoding='utf-8').read())
words=pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))


def clean_up_sentence(sentence):
    sentence_words= nltk.word_tokenize(sentence)
    sentence_words= [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words
def bow(sentence, words, show_details=True):
    sentence_words = clean_up_sentence(sentence)
    bag=[0]*len(words)
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" %w)
    return(np.array(bag))

def predict_class(sentence, model):
    p=bow(sentence, words, show_details=False)
    res= model.predict(np.array([p]))[0]
    ERROR_THERESHOLD = 0.25
    results = [[i, r] for i,r in enumerate(res) if r > ERROR_THERESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list=[]
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list
    
def tag(sentence, model):
    p=bow(sentence, words, show_details=False)
    res= model.predict(np.array([p]))[0]
    ERROR_THERESHOLD = 0.25
    results = [[i, r] for i,r in enumerate(res) if r > ERROR_THERESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list=[]
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
        tag= classes[r[0]]
    return tag

def probability(sentence, model):
    p=bow(sentence, words, show_details=False)
    res= model.predict(np.array([p]))[0]
    ERROR_THERESHOLD = 0.25
    results = [[i, r] for i,r in enumerate(res) if r > ERROR_THERESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list=[]
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
        probability= str(r[1])
    return probability

    
def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']==tag):
            result = random.choice(i['responses']) 
            break
        else:
            result = "Repite por favor"
    return result
    

def chatbot_response(msg):
    ints= predict_class(msg, model)
    res = getResponse(ints, intents)
    return res



