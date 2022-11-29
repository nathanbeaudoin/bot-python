import speech_recognition as sp
import datetime
import time
from gtts import gTTS
import os 
  
language = 'en'

print("hello, presse ctrl c to stop")
mytext = 'hello presse ctrl c to stop'
textSpeech = gTTS(text=mytext, lang=language, slow=False)
textSpeech.save("bienvenue.mp3")
os.popen("bienvenue.mp3")

# initialize the recognition
rec = sp.Recognizer()

# my device index 
my_micro = sp.Microphone (device_index=1)

with my_micro as source:
    print("Say something ...")
    audio = rec.listen(source) # get voice input from your micro

    to_text = rec.recognize_google(audio) # convert audio to text
    



if(to_text == "hello"):
    print("hello my frend")
    #voix
    mytext = 'hello my frend'
    textSpeech = gTTS(text=mytext, lang=language, slow=False)
    textSpeech.save("bienvenue.mp3")
    os.popen("bienvenue.mp3")

if(to_text == "what time is it"):
    x = datetime.datetime.now()
    print(x)

if(to_text == "How are you"):
    print("I'm fine and you ?")
    #voix
    mytext = 'I m fine and you ?'
    textSpeech = gTTS(text=mytext, lang=language, slow=False)
    textSpeech.save("bienvenue.mp3")
    os.popen("bienvenue.mp3")

if(to_text == "fuck you"):
    print("fuck you too")

if(to_text == "good bye"):
    print("have a nice day")

if(to_text == "help"):
    print("juste speak")
    mytext = 'juste speak'
    textSpeech = gTTS(text=mytext, lang=language, slow=False)
    textSpeech.save("bienvenue.mp3")
    os.popen("bienvenue.mp3")