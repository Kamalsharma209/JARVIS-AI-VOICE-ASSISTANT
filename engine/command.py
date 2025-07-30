import pyttsx3
import speech_recognition as sc
import eel

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Set to the first voice
    engine.setProperty('rate', 174)  # Set speech rate
    print(voices)
    engine.say(text)
    engine.runAndWait()

@eel.expose
def takecommand():
    r=sc.Recognizer()
    with sc.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source,10,6)
    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        eel.DisplayMessage(query)
        speak(query)
        eel.ShowHood()
    except Exception as e:
        return ""
    return query.lower() 