'''
Virtual Assistant --> make conversations, locate maps, greetings...

#TTS --> gTTS (google text to speech)
#file to speech --> playsound
#stt --> SpeechRecognition
#uuid --> organize files
#webbrowser --> open web applications
#time --> gives you current time
#customMethods --> rps game, qrcode, number game, play video

'''

import os
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import uuid
import webbrowser
import customMethods as cm
from time import ctime

#Identify voice
def listen():
    """SpeechRecognition"""
    #check mic as source
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source, phrase_time_limit=5)
    #Store the audio in a variable
    data = ""
    try:
        data = r.recognize_google(audio, language='en-US')
        print(f"User said : {data}\n")
    except sr.UnknownValueError:
        print("Say that again please...")
    except sr.RequestError:
        print("Request Failed")
    return data

# listen()

#separate functions for responding back and virtual assistant actions
def speak(String):
    """Responding function to get audio saved and text is spoken back"""
    print(String)
    tts = gTTS(text = String)
    #only modify content without creating new file
    tts.save('Speech.mp3')
    name = 'Speech%s.mp3'%str(uuid.uuid4())
    tts.save(name)
    playsound(name)
    os.remove(name)

def va(data):
    """Now we will map our conditions"""
    if "hello" in data:  #Greets the user
        listening = True
        speak("Hey, hai good to see you")
    
    elif "how are you" in data:  #Checks how the user is doing
        listening = True
        speak("I'm Fine, Thanks")
    
    elif "time" in data:  #Gives the current time
        listening = True
        speak(ctime())
    
    elif "open Google" in data:  #Opens Google in the web browser
        listening = True
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    
    elif "locate" in data:  #Opens Google Maps for a specific location
        speaking = True
        speak("Where do you want to Locate?")
        new_data = listen()
        url = "https://www.google.com/maps/place/" + new_data
        webbrowser.open(url)
    
    elif "video" in data:  #Opens a YouTube video
        speak("Playing Video")
        webbrowser.open("https://www.youtube.com/watch?v=wfch4ECkeDI")
    
    elif "movie" in data:  #Plays a movie in the local storage
        speaking = True
        speak("Playing Movie")
        cm.video()
    
    elif "qr" in data.lower():  #Generates a QR code for a website link
        speaking = True
        speak("Tell me a website link to generate QR Code for...")
        cm.qrgen(input("Enter website link : "))
        speak("QR code generated successfully")
    
    elif "rock paper scissors" in data.lower():  #Plays rock, paper, scissors with the user
        speaking = True
        speak("Rock paper scissors it is!")
        input_ = input("Enter Player1's move : ")
        speak(cm.rps(input_))
    
    elif "number game" in data.lower():  #Plays a guessing game with the user
        speaking = True
        speak("Number game it is!")
        input_ = int(input("Enter a number between 1 and 10 : "))
        speak(cm.numgame(input_))
    
    elif "stop" in data:  #Ends the Virtual Assistant
        listening = False
        speak("Bye")
    
    try:
        return listening
    except UnboundLocalError:
        print("Mismatched, speak correctly")

#main function that starts the virtual assistant
print("Starting...")
speak("Hello!")
listening = True
while listening:
    data = listen()
    listening = va(data)
