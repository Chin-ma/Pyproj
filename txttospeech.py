import os
import pyttsx3
import speech_recognition as sr

r = sr.Recognizer()

while(1):
    def speakText():
        voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.setProperty('voice', voice_id)

        if(r.recognize_google(audio) == 'what is your name'):
            engine.say('Zira')
        elif(r.recognize_google(audio) == 'how are you'):
            engine.say('I am fine and you?')
        elif(r.recognize_google(audio) == 'yeah I am fine'):
            engine.say('Nice to hear!')
        elif(r.recognize_google(audio) == 'what things can you do'):
            engine.say('I can tell you todays temperature, I can open an application for you, Some things are yet to be added')
        elif(r.recognize_google(audio) == 'open Notepad'):
            engine.say('Opening notepad')
            os.system("start notepad")
        elif(r.recognize_google(audio) == 'close notepad'):
            engine.say('Closing notepad')
            os.system('TSKILL notepad')
        elif(r.recognize_google(audio) == 'stop'):
            engine.say('OK, I wont speak anymore')
            exit(0)
        else:
            engine.say('Sorry i dont know about this')
        engine.runAndWait()

    with sr.Microphone() as source: 
        r.adjust_for_ambient_noise(source)
        print("Please say something!!")
        audio = r.listen(source)

    try:
        print("You said: \n" + r.recognize_google(audio))
    except Exception as e:
        print(e)


    if __name__ == "__main__":
        speakText()