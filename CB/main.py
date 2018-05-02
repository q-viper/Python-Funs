from chatterbot import ChatBot # method to train chatbot
from chatterbot.trainers import  ListTrainer # import chatbot
import os
import pyttsx3 #import text to speech library
import speech_handler as sphnd

bot = ChatBot('Quassi') # create chatbot

bot.set_trainer(ListTrainer) # Set the trainer

for _file in os.listdir('files'): #open directory files
     chats = open('files/' + _file, 'r').readlines() # read each line of individual
     
     bot.train(chats)
        
sphnd.quassi.say("Hii, my name is Quassi. How can I call you?")
sphnd.quassi.runAndWait()
name=input( "Quassi : Hii, my name is Quassi. How can I call you?\n-> ")

sphnd.quassi.say(name + "Such a great name.")
sphnd.quassi.runAndWait()

while True:
     request = input (name + ":")

     response = bot.get_response(request)
    
     if response.confidence > 0.4:
          sphnd.quassi.say(response) # says response
          print('Quassi : ', response, '\n')

     else:
          sphnd.quassi.say("Sorry i have no idea about that.")
          print('Quassi: Sorry i have no idea about that.')

     
     
     
     sphnd.quassi.runAndWait()

     if request == ( "Bye" or  "See you." or "so long"):
          break





