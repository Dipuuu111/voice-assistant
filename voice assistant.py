import pip

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

install('speech_recognition')
install('webbrowser')
install('playsound')
install('gtts')
install('pywhatkit')
install('wikipedia')

import speech_recognition as sr
import webbrowser
from time import ctime
import time
import playsound
import os
import random
from gtts import gTTS
import pywhatkit
import wikipedia
r = sr.Recognizer()




def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            alexa_talk(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            alexa_talk("Sorry, I didn't get that")
        except sr.RequestError:
            alexa_talk("Sorry,My speech service is down")
        return voice_data


def alexa_talk(audio_string):
    tts = gTTS(text=audio_string, lang="en")
    r = random.randint(1, 100000000)
    audio_file = "audio-" + str(r) + ".mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)



def respond(some_data):


    if "search" in some_data:
        search = record_audio("What do you want to search for?")
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        alexa_talk("Here's what I found on internet")
    if "find location" in some_data:
        location = record_audio("which location do you want?")
        url = "https://google.nl/maps/place/" + location + "/&amp"
        webbrowser.get().open(url)
        alexa_talk("Here's your location")
    if "what is your name" in some_data:
        alexa_talk("my name is VI")
    if "what is the time" in some_data:
        alexa_talk(ctime())
    if "thank you" in some_data:
        alexa_talk("no problem")
    if "thankyou" in some_data:
        alexa_talk("no problem")
    if "thanks" in some_data:
        alexa_talk("no problem")
    if "play" in some_data:
        play = some_data.replace("alexa play", "")
        alexa_talk("playing")
        pywhatkit.playonyt(play)
    if "what is the meaning of" in some_data:
        try:
            question = some_data.replace("alexa what is the meaning of", "")
            info = wikipedia.summary(question, 2)
            alexa_talk(info)
        except wikipedia.exceptions.PageError:
            alexa_talk("sorry I didn't get that")
    if "who is " in some_data:
        try:
            q = some_data.replace("who is", "")
            info2 = wikipedia.summary(q, 2)
            alexa_talk(info2)
        except wikipedia.exceptions.PageError:
            alexa_talk("sorry I didn't get that")
    if "stop" in some_data:
        alexa_talk("thanks,now I will stop")



def start_working():
    time.sleep(1)
    alexa_talk("How can I help you?")
    while 1:
        voice_data = record_audio()
        respond(voice_data)

start_working()
