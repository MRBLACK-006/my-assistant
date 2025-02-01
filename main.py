# Python program to translate
# speech to text and text to speech


import speech_recognition as sr
import pyttsx3 
import webbrowser
import subprocess
import pyautogui
import time
import datetime
# Initialize the recognizer 
r = sr.Recognizer() 

# Function to convert text to
# speech
def SpeakText(command):
    
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()


def open_chrome(url):
   browser = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
   webbrowser.get(browser)
   #You can do webbrowser.open(url, 0) if you want to open in the same window, 1 is a new window, 2 is a new tab. Default behaviour opens them in a new tab anyway.
   #See https://docs.python.org/2/library/webbrowser.html
   webbrowser.open(url)
    
def Spotify():
    subprocess.Popen([r"C:\\Users\\MR.BLACK\AppData\\Roaming\Spotify\Spotify.exe"])
    time.sleep(5)
    pyautogui.press("playpause")
    SpeakText("playing")

    
# Loop infinitely for user to
# speak
hour = datetime.datetime.now().hour
greetings = ""
if 5 <= hour < 12:
    greetings = "Good Morning"
elif 12 <= hour < 17:
    greetings = "Good Afternoon"
elif 17 <= hour < 21:
    greetings = "Good Evneing"
else:
    greetings = "Good Night"

SpeakText(greetings + " sir i am here to serve you")
while(1):    
    print("speak : ")
    
    # Exception handling to handle
    # exceptions at the runtime
    try:
        
        # use the microphone as source for input.
        with sr.Microphone() as source2:
            
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
            r.adjust_for_ambient_noise(source2, duration=0.2)
            
            #listens for the user's input 
            audio2 = r.listen(source2)
            
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            # MyText = r.recognize_tensorflow(audio2)

            MyText = MyText.lower()
            print("you said : ",MyText)

            if(MyText == "open chrome"):
                SpeakText("opening chrome")
                open_chrome("www.google.com")
            elif(MyText == "open youtube"):
                SpeakText("opening youtube")
                open_chrome("www.youtube.com")
            elif(MyText== "open spotify" or MyText == "play some song"or MyText== "play some music"):
                SpeakText("okay dumb shit am opening spotify" )
                Spotify()
            elif(MyText == "volume up"):
                pyautogui.press("volumeup")
            elif(MyText == "volume down"):
                pyautogui.press("volumedown")
            elif("search" in MyText):
                "search youtube"
                search_text = MyText[7:]
                open_chrome("https://www.google.com/search?q="+search_text)
                SpeakText("searching " + search_text)
            elif(MyText == "goodbye"):
                SpeakText("bye bye see you later ")
                break

            
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        
    except sr.UnknownValueError:
        print("unknown error occurred")


