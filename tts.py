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
    # print(arg1)
    # Language in which you want to convert
    language = 'en'
    print('here is the input: ' + str(arg1))

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=arg1, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome

    # Playing the converted file
    myobj.save("welcome.mp3")
    print('hello there')
    mixer.init()
    mixer.music.load('/Users/lahari/slackathon/Accessbility-App/welcome.mp3')
    mixer.music.play()
    print('we made it')
    time.sleep(5)
    return;
print('did you reach')
doTTS(sys.argv[1])
# os.system("mpg321 welcome.mp3")
