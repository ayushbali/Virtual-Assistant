import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib


# getting and setiing up the voice 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#creating function for taking audio 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("Jarvis at your service sir. Tell me what to do")


# taking microphone input from the user and converts it into string
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 100
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in') 
        print("user said", query)        
    except Exception as e:
        # print(e)
        print("Didn't recognized what you've said sir")
        return "None"
    return query

#   EMAIL FUBNCTION
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rishu.baliab@gmail.com', 'ayushbali0611')
    server.sendmail('rishu.baliab@gmail.com', to, content)
    server.close()


if __name__ == "__main__" :
    wish()
    
    # executing tasks
    if 1:
        query = takeCommand().lower() #takes our query in lower case 

        #executing tasks on basis of query
        if "quit" in query:
            exit()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak("According to Wikipedia, ")
            speak(results)

        elif 'open google' in query:
            webbrowser.open("google.com")
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
        elif "open reddit" in query:
            webbrowser.open("www.reddit.com")

        elif 'play some muisc' or 'play me a song' or 'play music' in query:
            musicDirectory = 'E:\\Music'
            songs = os.listdir(musicDirectory)
            os.startfile(os.path.join(musicDirectory, songs[17]))
            
        elif "send an email to shivam" or "email me" in query: 
            try:
                speak("What do you want to say Sir?")
                content = takeCommand()
                to = "rishu.baliab@gmail.com"
                #function to send emauk
                sendEmail(to, content)         
                speak("Email has been sent sir!")
            except Exception as e:
                print(e)
                speak("Sorry I couldn't send the email")                