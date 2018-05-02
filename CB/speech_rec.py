import speech_recognition as sr

# get audio from the microphone                                                                       

r = sr.Recognizer()
with sr.Microphone() as source:
    #print("Please wait. Calibrating microphone...")
    # listen for 1 second and create the ambient noise energy level
    r.adjust_for_ambient_noise(source, duration=0.1)
    print("Say something!")
    audio = r.listen(source,phrase_time_limit=2)
 
try:
    print("You said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))

