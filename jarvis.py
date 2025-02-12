import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
print (voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Hello, Good Morning Boss")
    elif hour>=12 and hour<18:
        speak("Hello, Good Afternoon Boss")
    else:
        speak("Hello, Good Evening Boss")

    speak("Im JARVIS , How may i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en')
        print(f"User said: {query}\n")

    except Exception as e:

        print('say that again pls sir')
        return "None"
    return query       


if __name__=="__main__":
    wishMe()
    takeCommand()