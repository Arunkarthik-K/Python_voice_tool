# import required module
import os
import time
import pyttsx3
import speech_recognition as sr

# create object and assign voice
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

rate = engine.getProperty('rate')
engine.setProperty('rate', 180)

# make the speech audible in the system
# engine.runAndWait()

print("\n================================================ Hello Arunkarthik "
      "===============================================")
engine.say('\nHello Arun karthik')

print(" \nThis tool helps you to open below things...")
print("\n\t 1. Google Chrome \n\t 2. VLC Media Player  \n\t 3. Notepad++ "
      "\n\t 4. VMware \n\t 5. MatterMost \n\t 0. Exit")

print("\n(YOU CAN SPEAK LIKE 'OPEN CHROME')")
print("\n============================================ Welcome To Voice App Tool "
      "============================================")

pyttsx3.speak("Welcome to Voice app tool!")
# "By default, chrome will be Opened")
# os.system('start chrome')

# how to use wait() instead of sleep
time.sleep(2)
engine.say("If you need to open more apps!. Talk to me with your requirements")

# make the speech audible in the system
engine.runAndWait()

while True:

    print("Nebula is listening...")

    r = sr.Recognizer()

    with sr.Microphone() as source1:

        audio1 = r.listen(source1)

        try:
            s = r.recognize_google(audio1)
        except sr.UnknownValueError:
            pyttsx3.speak("Level 1 Nebula could not understand the audio")

    while "hello" in s:

        with sr.Microphone() as source2:

            print("Talk to me with your requirements...")
            audio2 = r.listen(source2)

            try:
                p = r.recognize_google(audio2)
            except sr.UnknownValueError:
                pyttsx3.speak("Level 2 Nebula could not understand the audio")

        if ("GOOGLE" in p) or ("SEARCH" in p) or ("WEB BROWSER" in p) or ("CHROME" in p) or ("BROWSER" in p) or (
                "1" == p) \
                or ("open Chrome" in p):
            pyttsx3.speak("Opening Google Chrome")
            dfs = os.system('start chrome')
            break

        elif ("VLCPLAYER" in p) or ("PLAYER" in p) or ("VIDEO PLAYER" in p) or ("2" == p):
            pyttsx3.speak("Opening Vlc Player")
            os.system("vlc")

        elif ("NOTE" in p) or ("NOTES" in p) or ("NOTEPAD" in p) or ("EDITOR" in p) or ("3" == p) or ("open note" in p):
            pyttsx3.speak("Opening Notepad++")
            os.system("start notepad++")
            break

        elif ("VM" in p) or ("VMWARE" in p) or ("4" == p):
            pyttsx3.speak("Opening VMware")
            os.system('vmware-view')

        elif ("MATTER" in p) or ("MOST" in p) or ("MATTERMOST" in p) or ("5" == p):
            pyttsx3.speak("Opening MatterMost")
            os.system("Mattermost")

        # close the program
        elif ("EXIT" in p) or ("QUIT" in p) or ("CLOSE" in p) or ("0" == p) or ("close" in p):
            pyttsx3.speak("Exiting")
            exit()

        # invalid input
        else:
            pyttsx3.speak(p)
            print("Is Invalid, Please Try Again!")
            pyttsx3.speak("Is invalid, Please try again")

    else:
        pyttsx3.speak("Sorry Nebula is still listening. Please try again...")
