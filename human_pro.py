#menu_driven_program
import pyttsx3
import os

pyttsx3.speak("Welcome to Alexa, your virtual assistant ! ")
print("Welcome to Alexa, your virtual assistant ! ")
while True:
    print("_"*50)
    pyttsx3.speak("What do you want to do now?  ")
    print("What do you want to do now?   ",end=" ")
    user=input().lower( )
    if ("exit" in user) or ("quit" in user) or ("end" in user) or ("close" in user) or ("leave" in user) or ("depart" in user) or ("escape" in user):
        pyttsx3.speak("\nThank  you! \nHave a great day!")
        print("\nThank  you! \nHave a great day!")
        break
    elif ("run" in user) or ("launch" in user) or ("execute" in user) or ("open" in user) or ("start" in user) or ("activate" in user) or ("visit" in user) or ("go" in user):
        if("browser" in user):
            if ("chrome" not in user) and ("firefox" not in user):
                pyttsx3.speak("Which browser you want to open? ")
                browser=input("Which browser you want to open?  ")
            if ("chrome" in browser) or ("chrome" in user):
                pyttsx3.speak("chrome opening!  Please wait!")
                os.system("chrome")
            elif ("firefox" in user) or ("firefox" in browser):
                pyttsx3.speak("firefox opening!  Please wait!")
                os.system("firefox")
        elif ("text editor" in user):
            if ("notepad" not in user) and ("notepad++" not in user) and ("wordpad" not in user):
                pyttsx3.speak("Which text editor you want to open? ")
                editor=input("Which text editor you want to open?  ")
            if ("notepad" in user) or ("notepad" in editor):
                pyttsx3.speak("notepad opening!  Please wait!")
                os.system("notepad")
            elif ("notepad++" in user) or ("notepad++" in editor):
                pyttsx3.speak("notepad++ opening!  Please wait!")
                os.system("notepad++")
            elif ("wordpad" in user) or ("wordpad" in editor):
                pyttsx3.speak("wordpad opening!  Please wait!")
                os.system("write")
        elif ("media player" in user):
            if ("vlc" not in user) and("windows media player" not in user):
                pyttsx3.speak("Which media player you want to open? ")
                media=input("Which media player you want to open?  ")
            if ("vlc" in user) or ("vlc" in media):
                pyttsx3.speak("vlc media player opening!  Please wait!")
                os.system("vlc")
            elif ("windows media player" in user) or ("windows media player" in media):
                pyttsx3.speak("windows media player opening!  Please wait!")
                os.system("wmplayer")
        elif ("networks" in user):
            pyttsx3.speak("Network connections opening!  Please wait!")
            os.system("control netconnections")
        elif ("paint" in user):
            pyttsx3.speak("paint opening!  Please wait!")
            os.system("mspaint")
        elif ("calculator" in user):
            pyttsx3.speak("calculator opening!  Please wait!")
            os.system("calc")
        elif ("control panel" in user):
            pyttsx3.speak("control panel opening!  Please wait!")
            os.system("control")
        elif ("windows explorer") or ("File explorer" in user) or ("explorer" in user):
            pyttsx3.speak("windows explorer opening!  Please wait!")
            os.system("explorer.exe")
        elif ("task manager" in user):
            pyttsx3.speak("task manager opening!  Please wait!")
            os.system("taskmgr")
        elif ("volume" in user):
            pyttsx3.speak("sound and volume opening!  Please wait!")
            os.system("sndvol")
        elif ("documents" in user):
            pyttsx3.speak("documents opening!  Please wait!")
            os.system("documents")
        elif ("settings" in user):
            pyttsx3.speak("settings opening!  Please wait!")
            os.system("ms-settings:")
        elif ("date" in user) or ("time" in user):
            pyttsx3.speak("date and time  opening!  Please wait!")
            os.system("timedate.cpl") 
        elif ("windows defender" in user):
            pyttsx3.speak("windows defender opening!  Please wait!")
            os.system("windowsdefender")
        elif ("weather" in user):
            pyttsx3.speak("weather opening!  Please wait!")
            os.system("bingweather")        
        else:
            pyttsx3.speak("Not found....Try again!")
            print("Not found....Try again!")
    else:
        pyttsx3.speak("Invalid Input!\tTry again!")
        print("Invalid Input!\tTry again!")
    print()
