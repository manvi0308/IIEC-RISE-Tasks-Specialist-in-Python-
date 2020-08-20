# Problem statement: Convert the OS based program into a menu driven program, which will execute the required user query when user will give the input as a text
#Importing required modules
import os    #Required for executing system commands in python
import  pyttsx3   #Its a python text to speech library

engine = pyttsx3.init()   #initializing an object of engine

print('Hello There!!')
engine.speak('Hello I am Starlet!! Your personal assistant , I will help you in opening programs by a single number!!')
engine.speak("Welcome to my tools")

engine.speak('Let me show you what i can do for you!!')
print()
print('Press 1:     For opening chrome browser')
print('Press 2:     To open notepad')
print('Press3:      To open media player')
print('press 4:     To open Internet Explorer')
print('press 5:     To open Sublime Text3')
print('press 6:     To open VLC')

engine.speak('Go ahead type your choice!! Only the number!')
print("Enter your Choice  :",end='')
choice  =  input()
print("You entered  " + choice)

# For switching between various choices entered by user i have used if - elif -else clause
if int(choice)==1:
	os.system("chrome")   #Required command for chrome
elif int(choice)==2:
	os.system("notepad")  #Required command for notepad
elif int(choice)==3:
	os.system("wmplayer")   #Required command for windows media player
elif int(choice)==4:
	os.system("explorer")  #Required command for internet explorer
elif int(choice)==5:
	os.system("sublime_text")  #Required command for sublime text
elif int(choice)==6:
                    os.system("vlc")   #Required command for vlc player
else:
engine.speak("I currently don't support your choice!!Don't worry i will be trained super soon")

engine.runAndWait()
engine.stop()

#So Far So good
#Soon our voice assistant will have many more features where we don't have to type even we will just speak and Starlet will do for us
