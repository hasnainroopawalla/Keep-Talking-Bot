import random
import time
from gtts import gTTS
import os
import speech_recognition as sr

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("pcvoice.mp3")
    os.system("start pcvoice.mp3")
    
def recognize_speech_from_mic(recognizer, microphone):
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"

    return response

recognizer = sr.Recognizer()
microphone = sr.Microphone()

def gettext():
    print('Speak')
    guess = recognize_speech_from_mic(recognizer, microphone)
    if guess["transcription"]:
        text = guess["transcription"]
        print("You said:",text)
        
    ##    speak(text)
        return text
    
    
    if not guess["success"]:
        print("I didn't catch that. What did you say?\n")
    if guess["error"]:
        print("ERROR: {}".format(guess["error"]))


