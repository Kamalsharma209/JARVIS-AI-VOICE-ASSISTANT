import pyttsx3

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Set to the first voice
    engine.setProperty('rate', 174)  # Set speech rate
    print(voices)
    engine.say(text)
    engine.runAndWait()


    speak("Hello, this is a test of the text-to-speech engine.")