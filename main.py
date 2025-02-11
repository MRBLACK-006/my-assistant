import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess
import pyautogui
import time
import datetime

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to speech
def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# Function to open Chrome with a given URL
def open_chrome(url):
    browser = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(browser)
    webbrowser.open(url)

# Function to open Spotify and play/pause music
def Spotify():
    subprocess.Popen([r"C:\\Users\\MR.BLACK\\AppData\\Roaming\\Spotify\\Spotify.exe"])
    time.sleep(5)
    pyautogui.press("playpause")
    SpeakText("playing")

# Function to open a game
def game():
    exe_path = r'"D:\GAMES\Horizon - Zero Down CE\HorizonZeroDawn.exe"'
    subprocess.run(["powershell", "Start-Process", exe_path, "-Verb", "RunAs"], shell=True)

# Function to check if a command is in a list of commands
def cmdChecker(mytext, cmdlist):
    for i in cmdlist:
        if mytext == i:
            return True
    return False

# Function to tell the current time
def tell_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    SpeakText(f"The current time is {current_time}")

# Greet the user based on the time of day
hour = datetime.datetime.now().hour
greetings = ""
if 5 <= hour < 12:
    greetings = "Good Morning"
elif 12 <= hour < 17:
    greetings = "Good Afternoon"
elif 17 <= hour < 21:
    greetings = "Good Evening"
else:
    greetings = "Good Night"

SpeakText(greetings + " .......I am your AI assistant, ...I am here to assist you")

# Loop infinitely for user to speak
while True:
    print("Speak: ")

    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2).lower()
            print("You said: ", MyText)

            if MyText == "open chrome":
                SpeakText("opening chrome")
                open_chrome("www.google.com")
            elif MyText == "open youtube":
                SpeakText("opening youtube")
                open_chrome("www.youtube.com")
            elif cmdChecker(MyText, ["open spotify", "play some song", "play some music"]):
                SpeakText("okay, opening spotify")
                Spotify()
            elif MyText == "volume up":
                pyautogui.press("volumeup")
            elif MyText == "volume down":
                pyautogui.press("volumedown")
            elif "search" in MyText:
                search_text = MyText[7:]
                open_chrome("https://www.google.com/search?q=" + search_text)
                SpeakText("searching " + search_text)
            elif cmdChecker(MyText, ["open horizon", "open horizon zero dawn"]):
                SpeakText("okay, opening horizon zero dawn")
                game()
            elif MyText == "what time is it":
                tell_time()
            elif MyText == "open notepad":
                SpeakText("opening notepad")
                subprocess.Popen(["notepad.exe"])
            elif MyText == "open calculator":
                SpeakText("opening calculator")
                subprocess.Popen(["calc.exe"])
            elif MyText == "take screenshot":
                SpeakText("taking screenshot")
                screenshot = pyautogui.screenshot()
                screenshot.save("screenshot.png")
                SpeakText("screenshot saved")
            elif MyText == "goodbye":
                SpeakText("bye bye....see you later")
                break
            else:
                SpeakText("UNKNOWN COMMAND!")
                print("UNKNOWN COMMAND!")

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occurred")
