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
        querry = r.recognize_google(audio)
        print("User Said : {} ".format(querry))
    except sr.UnknownValueError:
        print("Sorry could not understand audio")
        return "None"
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return "None"
    
    return querry


if __name__== "__main__":
    speak("Hello, I am your assistant, how may I help you today?")
    while True:
        querry = listen().lower()

        if 'wikipedia' in querry:
            speak('searching wikipedia...')
            querry = querry.replace('wikipedia', "")
            try:
                result = wikipedia.summary(querry, sentences = 2)
                speak("According to wikipedia")
                speak(result)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("Multiple pages were found. Please try again with a more specific query.")
                print(e)
            except wikipedia.exceptions.PageError as e:
                speak("Sorry, no information was found. Please try again with a different query.")
                print(e)

