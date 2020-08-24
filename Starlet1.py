import os
import pyttsx3
import datetime
import webbrowser
import wikipedia

#One time initialization
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 150 )    # Speed percent (can go over 100)
engine.setProperty('volume', 1.0)  # Volume 0-1


#Greetings function

def greetUser():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        engine.say("Wishing you a bright morning")

    elif hour >= 12 and hour < 18:
        engine.say("I hope you are having a good day!!Good Afternoon Ma'am!")

    else:
        engine.say("Hope that you had a really productive day , GOOOOOD Evening ")
#Main code begins here
greetUser()
engine.say('Hello I am Starlet , your virtual assistant !!Welcome to my tools')

while (1):
	

	engine.say('Enter 1 for chrome:')
	engine.say('Enter 2 for wmplayer:')
	engine.say('Enter 3 for word:')
	engine.say('Enter 4 for powerpoint:')
    	engine.say('Enter 5 for Notepad++')
    	engine.say('Enter 6 for Youtube:')
	
	
	engine.say('ENTER YOUR CHOICE')
	
	print('Enter your choice')
	
	#Taking user input for choice
	choice = input()
	if int(choice)==1:
		engine.say('Opening Chrome for you!!')
		os.system('chrome')
	elif int(choice)== 2:
		engine.say('Opening Windows media player')
		os.system('wmplayer')
	elif int(choice) == 3:
		engine.say('Opening word for you!!')
		os.system('WINWORD')
	elif int(choice) == 4:
		engine.say('Opening Powerpoint for you')
		os.system('POWERPNT')
    	elif int(choice) == 5:
        engine.say('Opening Notepad++ for you')
        os.system('notepad++')
    	else:
        engine.say('Opening Youtube for you')
        webbrowser.open(https://www.youtube.com/, new=0, autoraise=True)
	engine.runAndWait()
