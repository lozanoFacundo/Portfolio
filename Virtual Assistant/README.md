ENGLISH:

Sara is a virtual assistant whose goal was to help me automate some actions on my computer.

The way I developed Sara is simple to understand, using Deep Learning I applied the same methodology used in Chatbots so that she identifies what I was saying.

As I am from Argentina, the code has a mix between English and Spanish.

Step by Step:

1- intents.json: The first thing I needed for Sara was the data, these are arranged in a Json file and are related to different actions that I wanted Sara to have.

2- processor.py: This file is in charge of tokenizing the json data, that is, it prepares our data to later be processed in Sara's engine. Different functions are created that together then make the whole.

3- engine.py: This is where we apply artificial intelligence, using a Keras Sequential model we train our model with the previously pre-processed data. In this way we would have the structure of a ChatBot.

4- body.py: In this file you will find the different senses of Sara. On the one hand we have a function that allows her to listen through the microphone and on the other hand she has a function that would allow her to speak. In this case we use libraries like Google Speech Recognition and gTTS + playsound.

5- functions.py: In this file we will concentrate all the functions that we want Sara to have.

6- Sara.py: Importing all the necessary functions from the other files, I put together a simple structure based on If Statements that allow you to use the listener function, process with the engine, call the corresponding function, and respond with the function speaks.

SPANISH:

Sara es un asistente virtual cuyo objetivo era ayudarme a automatizar algunas acciones en mi computadora. 

La forma en la que desarrolle a Sara es simple de entender, utilizando Deep Learning apliqué la misma metodología usada en los Chatbots para que identifique lo que yo decía.

Como yo soy de Argentina, el código tiene un mix entre Ingles y Español.

Paso a paso:

1- intents.json: Lo primero que necesitaba para Sara eran los datos, estos están dispuestos en un archivo Json y están relacionados a diferentes acciones que yo quería que tuviera Sara.

2- procesador.py: Este archivo es el encargado de tokenizar los datos del json, es decir que prepara a nustros datos para luego ser procesados en el motor de Sara. Se crean diferentes funciones que juntas luego hacen al todo.

3- engine.py: Aquí es donde aplicamos la inteligencia artificial, utilizando un modelo Secuencial de Keras entrenamos a nuestro modelo con los datos ya preprocesados anteriormente. De esta forma tendríamos la estructura de un ChatBot.

4- cuerpo.py: En este archivo se encontrarán los diferentes sentidos de Sara. Por un lado tenemos una función que le permite escuchar a través del microfono y  por otro lado tiene una función que le permitiría hablar. En este caso utilizamos librerías cómo Google Speech Recognition y gTTS + playsound.

5- funciones.py: En este archivo concentraremos todas las funciones que queremos que tenga Sara. 

6- Sara.py: Importando todas las funciones necesarias de los demás archivos, armé una estructura simple en base a If Statements que le perimitan utilizar la función de escucha, procesar con el motor, llamar a la función correspondiente, y responder con la función habla.
