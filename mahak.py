from pip import main
import speech_recognition as sr
import pyttsx3
import wikipedia

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def listen():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        querry = r.recognize_sphinx(audio)
        print("User Said : {} ".format(querry))
    except Exception as e:
        print(e)
        print("Sorry could not understand audio")
        return "None"
    
    return querry


if __name__== "__main__":
    speak("Hello, I am your stupid assistant Mehak, You can ask me anything But I don't think I can help because I am stupid")
    while True:
        querry = listen().lower()

        if 'wikipedia' in querry:
            speak('searching wikipedia...')
            querry = querry.replace('wikipedia', "")
            result = wikipedia.summary(querry, sentences = 2)
            speak("According to wikipedia")
            speak(result)
