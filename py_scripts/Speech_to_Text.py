
# coding: utf-8

# In[1]:

import speech_recognition as sr
from pygame import mixer # Load the required library


# In[2]:

# Install
# sudo pip uninstall pyaudio
# conda install -c akode pyaudio 
# pip install SpeechRecognition
# pip install urllib3
# pip install pygame


# Test
# python -m speech_recognition


# In[32]:

accepted = 'kim.mp3'
rejected = 'error.mp3'

def play_tone(tone):
    mixer.init()
    mixer.music.load(tone)
    mixer.music.play()


# In[33]:

def levenshtein(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]


# In[34]:

trigger_word = 'hey handy'
command_words = ['send','repeat','read']


# In[58]:

def record_audio(state):
    r = sr.Recognizer()
    m = sr.Microphone()
    
    try:
        log("A moment of silence, please...")
#         with m as source: r.adjust_for_ambient_noise(source)
        log("Set minimum energy threshold to {}".format(r.energy_threshold))
        while True:
            log("Say something!")
            with m as source: audio = r.listen(source,timeout=115)
            log("Got it! Now to recognize it...")
            try:
                
                
                # recognize speech using Google Speech Recognition
                value = r.recognize_google(audio).lower()
                
                # Look for trigger word
                if(state==1): 
                    bol, command =  state1(value)
                    if(bol):
                        play_tone(accepted)
                        return bol, command
                # Look for audio command 
                elif(state==2): 
                    bol, command, text = state2(value)
                    if(bol): 
                        return  command, text
                    
                # Execute command

            except sr.UnknownValueError:
                play_tone(rejected)
                log("Oops! Didn't catch that")
            except sr.RequestError as e:
                
                
                log("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
    except KeyboardInterrupt:
        pass


# In[52]:

def state1(value):
    log('State 1 '+value)
    
    text = (value).encode("utf-8")
    log("Hadi ----------->"+text)
    log(levenshtein(trigger_word,text))

    if(levenshtein(trigger_word,text)<=3):
        log("Key word recognized")
        return True,value
    return False,''
def state2(value):
    word = ''
    log('State 2 '+value)
    for w in command_words:
        log('Looking for '+w)
        if(w in value):
            log('Command found '+w)
            return True,w,value
    return False,'',''
    
def state3(command,value):
    log('State 3 '+value)
    
    text = value.replace(command,"",1)
    if(command == 'send'): send(text)
    elif(command == 'read'): read(text)
    elif(command == 'repeat'): repeat(text)
    


# In[53]:

def send(text):
    print("*send "+text+"*")
    
def read(text):
    print("*read")
    
def repeat(text):
    print("*repeat")


# In[54]:

def log(text):
    print('')


# In[57]:

# 1. State: look for key word
found,_ = record_audio(state = 1)

log('***************************************')
# # 2. State: Recognized command
if(found): command,value = record_audio(state = 2)
log('command found '+command)

# print('***************************************')

# 3. State: execute command
state3(command,value)


# In[ ]:

# Wait for trigger word

# Once recieved trigger word, wait for command

#

