import pyttsx3
import os

pyttsx3.speak("Welcome to Alexa! Chat us with your requirements!")
print("Welcome to Alexa ! Chat us with your requirements!")
pro_list=["chrome","vlc","control panel","notepad","kmplayer","documents","pictures","wordpad","firefox","msclock","mspaint"]   #list can be modified as per requirements
result=0
while True:
    pyttsx3.speak("What do you want to do now?  ")
    print("What do you want to do now?   ",end=" ")
    user=input().lower( )
    if ("run" in user) or ("launch" in user) or ("execute" in user) or ("open" in user) or ("start" in user) or ("activate" in user) or ("visit" in user) or ("go" in user):
        if "text editor" in user:
            os.system("notepad")
        else:
            for item in pro_list:
                if item in user:
                    pyttsx3.speak(item + "opening! Please wait! ")
                    os.system(item)
                    result=1
        if result !=1:
            pyttsx3.speak("Not found....Try again!")
            print("Not found....Try again!")
    elif ("exit" in user) or ("quit" in user) or ("end" in user) or ("close" in user) or ("leave" in user) or ("depart" in user) or ("escape" in user):
        print("\nThank you!\n Have a great day!")
        pyttsx3.speak("Thank you!\nHave a great day!")
        break
    else:
        pyttsx3.speak("Invalid Input!\tTry again!")
        print("Invalid Input!\tTry again!")
