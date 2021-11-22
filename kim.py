#LIBRARIESsx3   
#pytt (text to speech conversion library)
#SpeechRecognition	(automatic recognition of human speech)

from tkinter import *
import numpy as np
import cv2
import PIL.Image, PIL.ImageTk   #[Python Imaging Library]   #( provides the python interpreter with image editing capabilities.)
import pyttsx3
import datetime     
import speech_recognition as sr
import wikipedia
import webbrowser
import os           #(creating and removing a directory (folder))
import random
import smtplib      #(used to send mail to any internet machine )
import pyowm        #(library for OpenWeatherMap web APIs)
from PIL import Image
import requests
import pywhatkit as pk      #(Play a YouTube video, Perform a Google Search.)


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

window = Tk()

global var
global var1

var = StringVar()
var1 = StringVar()


""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate

engine.setProperty('rate', 200)     # setting up new voice rate


def get_location():
    """ Function To Print GeoIP Latitude & Longitude """
    ip_request = requests.get('https://get.geojs.io/v1/ip.json')
    my_ip = ip_request.json()['ip']
    geo_request = requests.get('https://get.geojs.io/v1/ip/geo/' +my_ip + '.json')
    geo_data = geo_request.json()
    geo = geo_data['city']
    return geo


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        var.set("Good Morning Sir") 
        window.update()
        speak("Good Morning Sir!")
    elif hour >= 12 and hour <= 18:
        var.set("Good Afternoon Sir!")
        window.update()
        speak("Good Afternoon Sir!")
    else:
        var.set("Good Evening Sir")
        window.update()
        speak("Good Evening Sir!")
    speak("Myself KIM! How may I help you sir") 

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening...")
        window.update()
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        var.set("Recognizing...")
        window.update()
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        return "None"
    var1.set(query)
    window.update()
    return query

def play():
    btn2['state'] = 'disabled'
    btn0['state'] = 'disabled'
    btn1.configure(bg = 'orange')
    wishme()
    while True:
        btn1.configure(bg = 'orange')
        window.update()
        city=get_location() 
        var.set(city) 
        query = takeCommand().lower()
        if 'exit' in query:
            var.set("Bye sir")
            btn1.configure(bg = '#5C85FB')
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            window.update()
            speak('See you again boss. I will be there when ever you call me')
            break

        
        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            var.set("Sir the time is %s" % strtime)
            window.update()
            speak("Sir, the time is %s" %strtime)
        

        elif 'date' in query:
            strdate = datetime.datetime.today().strftime("%d %m %y")
            var.set("Sir today's date is %s" %strdate)
            window.update()
            speak("Sir today's date is %s" %strdate) 
        

        elif "who is" in query:
            query=query.replace('who is', '')
            
            engine.setProperty('rate', 160)
            results = wikipedia.summary(query, sentences=2) 
            var.set(query)
            window.update()                   
            speak("According to wikipedia"+ results)        
    

        elif 'open youtube' in query:
            engine.setProperty('rate', 200)
            var.set('opening Youtube')
            window.update()
            speak('opening Youtube sir, Enjoy')
            webbrowser.open("youtube.com")
            break

        elif 'open coursera' in query:
            var.set('opening coursera')
            window.update()
            speak('opening coursera')
            webbrowser.open("coursera.com")

        elif 'open google' in query:
            var.set('opening google')
            window.update()
            speak('opening google sir')
            webbrowser.open("google.com")

        elif 'hello' in query:
            var.set('Hello Everyone! My self KIM')
            window.update()
            speak('Hello Everyone! My self KIM')

        elif 'play' in query:
            query = query.replace('play', '')
            var.set('Playing '+ query)
            speak('Playing '+ query + ', enjoy sir')
            pk.playonyt(query)
            break
        

        elif 'search' in query: 
            query = query.replace('search', '')
            var.set('searching for ' + query)
            speak('Searching for' + query)           
            pk.search(query)

        elif 'thank you' in query:
            var.set("It was my pleasure Sir")
            window.update()
            speak("It was my pleasure Sir")
            

        elif 'what can you do for me' in query:
            var.set('I can do multiple tasks for you sir.\n tell me whatever you want to perform sir')
            window.update()
            speak('I can do multiple tasks for you sir. tell me whatever you want to perform sir')


        elif 'how old are you' in query:
            var.set("I am a Young Rockstar.")
            window.update()
            speak("I am a Young Rockstar sir")
            

        elif 'your name' in query:
            var.set("Myself KIM Sir, An Voice Virtual Assistant")
            window.update()
            speak('myself KIM sir,  An Voice Virtual Assistant')


        elif 'who created you' in query:
            var.set('My Creators are Materminds.')
            window.update()
            speak('My Creators are Masterminds')

              
def update(ind):
    frame = frames[(ind)%100]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)

label2 = Label(window, textvariable = var1, bg = '#FAB60C')
label2.config(font=("Courier", 20))
var1.set('User Said:')
label2.pack()

label1 = Label(window, textvariable = var, bg = '#ADD8E6')
label1.config(font=("Courier", 20))
var.set('Welcome')
label1.pack()

frames = [PhotoImage(file='assist.gif',format = 'gif -index %i' %(i)) for i in range(100)]
window.title('KIM-AI')

label = Label(window, width = 500, height = 500)
label.pack()
window.after(0, update, 0)

btn0 = Button(text = 'WISH ME',width = 20, command = wishme, bg = '#5C85FB')
btn0.config(font=("Courier", 12))
btn0.pack()
btn1 = Button(text = 'START',width = 20,command = play, bg = '#5C85FB')
btn1.config(font=("Courier", 12))
btn1.pack()
btn2 = Button(text = 'EXIT',width = 20, command = window.destroy, bg = '#5C85FB')
btn2.config(font=("Courier", 12))
btn2.pack()


window.mainloop()
