from function import function_sound
import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from time import ctime
from gtts import gTTS

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            assistant_speak(ask)
            audio = r.listen(source)
            voice_data = ''
            try:
                voice_data = r.recognize_google(audio)
            except sr.UnknownValueError:
                assistant_speak("Sorry, I don't get it")
            except sr.RequestError:
                assistant_speak("Sorry, my speech service is done")
            return  voice_data

def assistant_speak(audio_string):
    tts = gTTS(text=audio_string, lang="en")
    r = random.randint(1, 1000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'Who are you?' in voice_data:
        assistant_speak('Iam your assistant, call me Bwo')

    if 'what is the time now?' in voice_data:
        assistant_speak(ctime())

    if 'search' in voice_data:
        search = record_audio('what to search about?')
        url = 'https://google.com/search?q' + search
        webbrowser.get().open(url)
        assistant_speak('here is it' + search)

    if 'find location' in voice_data:
        location = record_audio('what is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        assistant_speak('here is it' + location)

    if 'go to sleep' in voice_data:
        assistant_speak('ok, good night')
        exit()
time.sleep(1)
assistant_speak('Hi, how can i help you?')
while True:
    voice_data = record_audio()
    respond(voice_data)
