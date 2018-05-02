import pyttsx3

#Bot settings.

quassi = pyttsx3.init()
sound = quassi.getProperty('voices')
quassi.setProperty('voice', sound[1].id)
quassi.setProperty('rate', 130)
quassi.setProperty('volume', 5)
#engine.say("This is awesome.")
#engine.runAndWait() 
