import speech_recognition as sr

def gettext(qstn, delay):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=delay)
        print(qstn+" ..Speak now")
        audio = r.listen(source,phrase_time_limit=10)
    try:
        response = r.recognize_google(audio)
        print('You said: ',response)
        return response
    except:
        raise Exception("Audio Not Captured")