import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("rate",175)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Dhruv Sir!")

    elif hour>12 and hour<18:
        speak("Good Afternoon Dhruv Sir!")

    else:
        speak("Good Evening Dhruv Sir!")

    speak("I am Jarvis, Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        r.energy_threshold = 700
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()  

        if "wikipedia" in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Yes sir")  
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            speak("Yes sir")
            webbrowser.open("https://www.google.com/")

        # elif 'open unacademy' in query:
        #     speak("Yes sir")
        #     webbrowser.open("https://unacademy.com/goal/jee-main-and-advanced-preparation/TMUVD")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")
            
        # elif 'Play music' in query:
        #     speak("Yes sir")
        #     webbrowser.open("https://open.spotify.com/")

        elif 'shut down' in query:
            break