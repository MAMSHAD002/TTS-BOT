import pyttsx3

def Speak(Audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)
    print(Audio)
    engine.say(Audio)
    engine.runAndWait()



Speak('Anything you want to say')    