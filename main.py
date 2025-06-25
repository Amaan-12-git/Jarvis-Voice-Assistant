import wikipedia
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import pyjokes
import datetime
# import requests
# import pygame
# import os
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='pyttsx3.drivers.nsss')

# recognizer = sr.Recognizer()
try:
    engine = pyttsx3.init()
    engine.setProperty('rate', 150) 
except Exception as e:
    print(f"Error initializing text-to-speech engine: {e}")

def speak(text):
     engine.say(text)
     engine.runAndWait()

def processCommand(c):
     if "open google" in c:
          webbrowser.open("https://google.com")
     elif "open youtube" in c:
          webbrowser.open("https://youtube.com")
     elif "open facebook" in c:
          webbrowser.open("https://facebook.com")
     elif "open linkedin" in c:
          webbrowser.open("https://linkedin.com")
     elif "open instagram" in c:
          webbrowser.open("https://instagram.com")
     elif "open twitter" in c:
          webbrowser.open("https://twitter.com")
     elif "open whatsapp" in c:
          webbrowser.open("https://web.whatsapp.com")
     elif c.lower().startswith("play"):
          song = c.lower().split(" ")[1]
          link = musicLibrary.music[song]
          webbrowser.open(link)
     elif c.lower().startswith("open spotify"):
          webbrowser.open("https://clone-of-spotify.freewebhostmost.com")
     elif c.lower().startswith("search"):
          search = c.lower()[7:]
          print(search)
          webbrowser.open(f"https://www.google.com/search?q={search}")
     elif 'wikipedia' in c:
            c = c.replace("wikipedia", "")
            results = wikipedia.summary(c, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
     elif 'joke' in c:
          speak(pyjokes.get_joke())
     elif 'the time' in c:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")    
            speak(f"Sir, the time is {strTime}")

if __name__ =="__main__":
     speak("Initializing Jarvis")
     while True:
          r = sr.Recognizer()
          print("Recognizing...")
          try:
               with sr.Microphone() as source:
                    print("Listening...")
                    audio = r.listen(source, timeout=4, phrase_time_limit=2)
                    # print(audio) # <speech_recognition.audio.AudioData object at 0x0000014A1454B2C0>
               word = r.recognize_google(audio)
               print(word) # hello
               if(word.lower() == "stop" or word.lower() == "exit"):
                    break
               if(word.lower() == "jarvis"):
                    speak("Jarvis Active")
                    with sr.Microphone() as source:
                         print("Speak...")
                         audio = r.listen(source, timeout=4, phrase_time_limit=2)
                         command = r.recognize_google(audio).lower()
                         print(command)
                         processCommand(command)
          except Exception as e:
               print("Error; {0}".format(e))
