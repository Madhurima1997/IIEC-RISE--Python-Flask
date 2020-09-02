import os
import pyttsx3
print("Hello User! How can I help you?")
pyttsx3.speak("Hello User! How can I help you?")
while(True):
    p=input("User: ")
    if(("chrome" in p) or ("internet" in p) or("net" in p) or ("Chrome" in p) or ("Internet" in p) or("Net" in p) or ("browse" in p) or ("Browse" in p) or ("browsing" in p) or ("Browsing" in p) or ("surf" in p) or ("Surf" in p) or ("surfing" in p) or ("Surfing" in p)):
        if(("don't" in p) or ("dont" in p) or ("do not" in p) or ("Don't" in p) or ("Dont" in p)):
            print("OK! What else can I do for you?") 
            pyttsx3.speak("OK! What else can I do for you?")
        else:
            print("Launching Chrome browser for you") 
            pyttsx3.speak("Launching Chrome browser for you")
            os.system("start chrome")
            print("What else can I do for you?") 
            pyttsx3.speak("What else can I do for you?")
    elif(("note" in p) or ("Note" in p) or ("document" in p) or ("Document" in p) or ("text" in p) or ("Text" in p) or ("jot" in p) or ("write" in p) or ("Write" in p) or ("notepad" in p) or ("Notepad" in p) or ("word" in p) or ("editor" in p) or ("Editor" in p) or ("msword" in p) or ("MsWord" in p) or ("MSWord" in p)):
        if(("don't" in p) or ("dont" in p) or ("do not" in p) or ("Don't" in p) or ("Dont" in p)):
            print("OK! What else can I do for you?") 
            pyttsx3.speak("OK! What else can I do for you?")
        elif(("notepad" in p)or ("Notepad" in p)):
            print("Launching notepad for you!")
            pyttsx3.speak("Launching notepad for you")
            os.system("notepad")
            print("What else can I do for you?") 
            pyttsx3.speak("What else can I do for you?")
        elif(("word" in p) or ("msword" in p) or ("MsWord" in p) or ("MSWord" in p)):
            print("Launching Microsoft Word for you!")
            pyttsx3.speak("Launching Microsoft Word for you")
            os.system("start winword")
            print("What else can I do for you?") 
            pyttsx3.speak("What else can I do for you?")
        else:
            print("Which editor do you want to use? MSWord or Notepad ?")
            pyttsx3.speak("Which editor do you want to use? MSWord or Notepad ?")
            x=input("User: ")
            if(("notepad" in x)or ("Notepad" in x)):
                print("Launching notepad for you!")
                pyttsx3.speak("Launching notepad for you")
                os.system("notepad")
                print("What else can I do for you?") 
                pyttsx3.speak("What else can I do for you?")
            elif(("word" in x) or ("msword" in x) or ("MsWord" in x) or ("MSWord" in x)):
                print("Launching Microsoft Word for you!")
                pyttsx3.speak("Launching Microsoft Word for you")
                os.system("start winword")
                print("What else can I do for you?") 
                pyttsx3.speak("What else can I do for you?")
            else:
                print("Sorry User! I do not support this editor")
                pyttsx3.speak("Sorry User! I do not support this editor")
                print("What else can I do for you?")
                pyttsx3.speak("What else can I do for you?")
    elif(("Thanks" in p) or ("Thank" in p) or ("thanks" in p) or ("thank" in p)):
        print("Glad to help you!")
        pyttsx3.speak("Glad to help you!")
    elif(("mails" in p) or ("email" in p) or ("emails" in p) or ("Mail" in p) or ("Email" in p) or ("Emails" in p) or ("mail" in p)):
        if (("don't" in p) or ("dont" in p) or ("do not" in p) or ("Don't" in p) or ("Dont" in p)):
            print("OK! What else can I do for you?")
            pyttsx3.speak("OK! What else can I do for you?")
        else:
            print("Launching Gmail for you!")
            pyttsx3.speak("Launching Gmail for you")
            os.system("start chrome gmail.com")
            print("What else can I do for you?") 
            pyttsx3.speak("What else can I do for you?")
    elif(("stop" in p) or ("exit" in p) or ("Exit" in p) or ("Stop" in p) or ("will be all" in p) or ("That's all" in p) or ("that's all" in p) or ("thats all" in p)):
        break
    else:
        print("Sorry I do not Understand!")
        pyttsx3.speak("Sorry I do not Understand! You can try the following")
        print("You can try browsing internet or")
        print("You can try checking your mails")
        print("You can launch Notepad to work")
        print("Or you can simply use stop command to exit")
print("Thank you user! See you again!")
pyttsx3.speak("Thank you user! See you again!")
