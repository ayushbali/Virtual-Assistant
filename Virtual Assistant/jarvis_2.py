import speech_recognition as sr
from time import ctime
import webbrowser
import time
from gtts import gTTS
import os
import random
import winsound

# this class will be used to recognize our audio
r = sr.Recognizer()

def recordAudio(ask = False):
    with sr.Microphone() as source:
        # listens our audio for input
        if ask:
            J_speak(ask)
        audio = r.listen(source)
        voiceData = ""
        try:
            voiceData = r.recognize_google(audio)
        except sr.UnknownValueError:
            J_speak("I am sorry sir")
        except sr.RequestError:
            J_speak("I am sorry sir")
        return voiceData

def J_speak(audio_string):
    text = gTTS(text=audio_string, lang='en', slow=False)
    r = random.randint(1,10000000)
    audio = 'audio-'+str(r)+'.mp3'
    text.save(audio)
    os.system(f"start {audio}")
    print(audio_string)
    


def respond(voiceData):
    if "Hello" in voiceData:
        J_speak("Welcome Sir! I am Jarvis")

    if "what's the time" in voiceData:
        J_speak(ctime())

    if "search" in voiceData:
        search = recordAudio("What do you want me to look-up for?")
        if 'video' in search:
            url = "https://www.youtube.com/results?search_query=" + search
            webbrowser.get().open(url)
        else:
            url = "https://www.google.com/search?q=" + search
            webbrowser.get().open(url)
        J_speak("Here is what I found " + search)

    if 'location' in voiceData:
        location = recordAudio("What is the location?")
        url = "https://www.google.co.in/maps/place/" + location
        webbrowser.get().open(url)
    if 'exit' in voiceData:
        exit()


time.sleep(1)
J_speak("How can I help you Sir!")
while 1:
    voiceData = recordAudio()
    respond(voiceData)