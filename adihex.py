import pyttsx3 #pip install pyttx3
import datetime
import speech_recognition as sr #pip installsp
import wikipedia
import webbrowser
import os
name = "Alok kumar"

engine = pyttsx3.init("sapi5")

voices = engine.getproperty("voices")
engine.setproperty ("voice",voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runandWait()




def wishme():
    hour = datetime.date.now().hour
    if hour>=0 and hour<=12:
        speak("Good morning, aditya sachan")
    elif hour>12 and hour<18:
        speak("good afternoon, aditya sachan")
    else:
        speak ("Good evening, aditya sachan")
    speak(f"I am {name}, How May I help you? ")







def hearme():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print("you said:",query)
    expectException:
    print("say that again,please")
    return"none"


if__name__ == "__main__":
def wishme():
    while True:
        
        query = hearme().lower()

        if "Wikipedeia" in query:
            speak("searching Wikipedia...")
            query = query.replace("Wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)
        elif "open google" in query:
            webbrowser.open("www.google.com")
        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")
        elif "coding asylum" in query:
            webbrowser.open("https://www.google.com/search?q=apna+college&oq=apnaco&aqs=chrome.")
        elif "plan music" in query:
            music_dir = "c:\\Users\\52141\Downloads\\ssstik-io-1727174135730-65613.mp3"
            songs = os.listdir(music_dir)
            speak("playing music...")
            song = os.path.join(music_dir,song[2]) #os.starfile(path of the song)
            os.startfile(song)
        elif "code" in query:
            os.startfile("c:\\Users\\52141\\Desktop\\hex softwares\\adihex.py")
        elif "your pic" or "your image" in query:
            os.starfile("c:\Users\52141\Desktop\2f3f069e-8f2e-4913-b571-c7d015842f1f.jpg")
        else:
            search = "https://www.google.com//search?q"+query




