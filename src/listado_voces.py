from encodings import utf_8
import pyttsx3
engine=pyttsx3.init()
voces=engine.getProperty('voices')

for voz in voces:
    print(voz, voz.id)
    engine.setProperty("voice", voz.id)
    engine.say("hello brother")
    engine.runAndWait()
    engine.stop