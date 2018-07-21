# Import the required module for text
# to speech conversion
from gtts import gTTS
from pygame import mixer

# This module is imported so that we can
# play the converted audio
import time, sys, os

def doTTS (arg1):
    # The text that you want to convert to audio
    # mytext = 'Welcome to geeksforgeeks!'

    # Language in which you want to convert
    language = 'en'

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=arg1, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome

    # Playing the converted file
    myobj.save("welcome.mp3")

    mixer.init()
    mixer.music.load('/Users/mahmed/Documents/GitHub/Accessbility-App/welcome.mp3')
    mixer.music.play()

    time.sleep(5)
    return;

# os.system("mpg321 welcome.mp3")
