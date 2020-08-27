import os
import pyttsx3
print("Hello User! How can I help you?")
pyttsx3.speak("Hello User! How can I help you?")
while(True):
    p=input("User: ")
    if(("chrome" in p) or ("internet" in p) or("net" in p) or ("Chrome" in p) or ("Internet" in p) or("Net" in p)):
        if(("don't" in p) or ("dont" in p) or ("do not" in p) or ("Don't" in p) or ("Dont" in p)):
            print("OK! What else can I do for you?") 
            pyttsx3.speak("OK! What else can I do for you?")
        else:
            print("Launching Chrome browser for you") 
            pyttsx3.speak("Launching Chrome browser for you")
            os.system("start chrome")
            print("What else can I do for you?") 
            pyttsx3.speak("What else can I do for you?")
    elif((("open" in p) or ("use" in p) or ("run" in p) or ("execute" in p)) and ("notepad" in p)):
        os.system("notepad")
    elif((("don't" in p) or ("do not" in p))):
        print("OK User! What else can I do for you?")
    elif(("mails" in p) or ("email" in p) or ("emails" in p)):
        os.system("start chrome gmail.com")
    elif(("stop" in p) or ("exit" in p)):
        break
    else:
        print("Sorry I do not Understand!")
        print("You can try browsing internet or")
        print("You can try checking your mails")
        print("You can launch Notepad to work")
        print("Or you can simply use stop command to exit")
print("Thank you user! See you again!")
