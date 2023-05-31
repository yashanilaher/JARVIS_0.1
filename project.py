#project
import pyttsx3
import speech_recognition as sr
import datetime


engine=pyttsx3.init("sapi5")   #this is used to take voices
voices=engine.getProperty("voices")
# it contains two voices one male and one female
engine.setProperty("voice,voices[0].id)
engine.setProperty("rate",150)   #rate with which jarvis speaks


def speak(audio):
    engine.say(audio)     #this audio will be said by engine for that runAndWait() function is used
    engine.runAndWait()
    
    
def takecommand():
    #it takes our voice from microphone as input and return in the form of string output
    r=sr.Recognizer()
    with sr.microphone() as source:
        print("listening")
        r.pause_threshold=1   #seconds of nonspeaking audio before a phrase is considered complete
        audio=r.listen(source)
    try:
        print("recognizing")
        query=r.recognize_google(audio,language="en-in")
        print(f"user said: {query}\n")
        speak(f"user said: {query}\n")
    except Exception as e:
        print("say that again please....")
        return "none"
    return query
 #yas anila her 