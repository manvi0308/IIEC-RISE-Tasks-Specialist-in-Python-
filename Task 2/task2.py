# importing the required modules
import speech_recognition as sr
import webbrowser as wb
import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 180)     # setting up new voice rate
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

pyttsx3.speak("Hello Manvi")
print()
# introductory messages
print("WELCOME TO THE STARLET WORLD".center(125))                    
engine.runAndWait()
pyttsx3.speak("Hello i am starlet, your virtual assistant")
pyttsx3.speak("How can i help you...?")

# to display a message that tells/prompts a user to speak his/her requirements
while True:
  print()
  print("I  am getting you, please speak up your requirements : ", end='')

  # after the user will begin speaking
  r  =  sr.Recognizer()
# just to recognize the voice spoken by us
  with sr.Microphone() as source:
      pyttsx3.speak('start speaking...')
      audio = r.listen(source)
      pyttsx3.speak('Listened to your requirements.. Let me do it for you..!!')

  # to recongnize the voice spoken by us
  ch = r.recognize_google(audio)

  /* Now the identification of what user wants us to do
  1) If only Hi/HELLO etc*/
  if("hello" in ch) or ("hi" in ch) and ("heya" in ch) or ("hey" in ch):
    pyttsx3.speak("hello Manvi , I hope you are in good mood as always...?")

    # now if the user asks about the bot
  elif("fine" in ch) or ("what" in ch) and ("about" in ch):
    pyttsx3.speak("I am in good health i am nicely trained by  you")

    # about starlet
  elif("tell" in ch) or ("about" in ch) and ("yourself" in ch):
    pyttsx3.speak("i am your voice assistant Starlet, You know what and i can control linux server for you")

    # usage of date command
  elif("date" in ch):
    wb.open("http://192.168.29.56/cgi-bin/local.py?x=date")
    pyttsx3.speak("Let me show you today's date")

    # usage of calendar command
  elif("calendar" in ch):
    wb.open("http://192.168.29.56/cgi-bin/local.py?x=cal")
    pyttsx3.speak("Let me show you calendar")

    #ip address
  elif("IP" in ch )or ("ip address" in ch) or "address" in ch):
    wb.open("http://192.168.29.56/cgi-bin/local.py?x=ifconfig")
    pyttsx3.speak("showing IP address")

    #active ports
  elif("active ports" in ch) or ("ports" in ch):
    wb.open("http://192.168.29.56/cgi-bin/local.py?x=netstat%20-tnlp")
    pyttsx3.speak("showing active ports")

 # run apache webserver
  elif("status" in ch) or ("webserver" in ch) and ("apache" in ch) or ("httpd" in ch):
    wb.open("http://192.168.29.56/cgi-bin/local.py?x=systemctl%20status%20httpd")
    pyttsx3.speak("apache webserver is running")
  
  elif("yum" in ch) or ("module" in ch) and ("list" in ch):
    wb.open("http://192.168.29.56/cgi-bin/local.py?x=yum%20module%20list")
    pyttsx3.speak("Here is the long list of modules")
    
  elif("package" in ch) or ("firefox" in ch):
    wb.open("http://192.168.29.56/cgi-bin/local.py?x=yum%20whatprovides%20firefox")
    pyttsx3.speak("Here is the package name of firefox")
    
  elif("ping" in ch) or ("google" in ch) and ("server" in ch):
    wb.open("http://192.168.29.56/cgi-bin/local.py?x=ping%20-c%205%208.8.8.8")
    pyttsx3.speak("Server is Ping able")
    
  elif ("How" in ch) and ("you can" in ch) or ("help me" in ch):
    pyttsx3.speak("i can help you in following ways")
    print()
    print("!! I can help you in following ways !!".center(126))
    pyttsx3.speak("I will help you with basic linux commands")
    print()
    print(" * Basic Linux Commands".center(126))
    pyttsx3.speak("Also Basic Networking")
    print()
    print(" * Basic Networking".center(126))
    pyttsx3.speak("Create User and Restrict User for Specific Program")
    print()
    print(" * Create User and Restrict User for Specific Program".center(126))

    pyttsx3.speak("Configuration of Docker")
    print()
    print(" * Configuration of Docker".center(126))

    pyttsx3.speak("Hadoop Setup")
    print()
    print(" * Hadoop Setup".center(126))

    pyttsx3.speak("Provision of EC-2 Instance")
    print()
    print(" * Provision of EC-2 Instance".center(126))

  elif("check docker" in ch) or ("verify" in ch):
    wb.open("http://192.168.29.56/cgi-bin/local.py?x=rpm%20-q%20docker-ce")
    pyttsx3.speak("docker is not installed....")

  elif("configure docker" in ch) or ("install" in ch) and ("configure" in ch):
    wb.open("http://192.168.29.56/cgi-bin/local.py?x=yum%20install%20docker-ce%20--nobest%20-y")
    pyttsx3.speak("installing docker....")

  elif("start service" in ch) or ("start docker servie") and ("service") in ch:
    wb.open("http://192.168.29.56/cgi-bin/local.py?x=systemctl%20start%20docker%20")
    pyttsx3.speak("starting docker service....")

  elif("verify docker" in ch) and ("installed" in ch):
    wb.open("http://192.168.29.56/cgi-bin/local.py?x=rpm%20-q%20docker-ce")
    pyttsx3.speak("Now docker is present in your linux server....")

  elif("how many" in ch) and ("docker containers" in ch) or ("containers" in ch):
    wb.open("http://192.168.29.56/cgi-bin/local.py?x=docker%20ps")
    pyttsx3.speak("There is no docker containers")

  elif("how many" in ch) and ("docker images" in ch) or ("images" in ch):
    wb.open("http://192.168.29.56/cgi-bin/local.py?x=docker%20images")
    pyttsx3.speak("There are several images")

  elif("pull" in ch) or ("wordpress" in ch) and ("image" in ch):
    wb.open("http://192.168.29.56/cgi-bin/local.py?x=docker%20pull%20wordpress")
    pyttsx3.speak("word press image is successfully pulled")

  elif("launch" in ch) and ("docker container" in ch):
    wb.open("http://192.168.29.56/cgi-bin/local.py?x=docker%20run%20-dit%20wordpress")
    pyttsx3.speak("word press container is successfully launched")

  elif("verify" in ch) and ("docker container" in ch) or ("container launched" in ch):
    wb.open("http://192.168.29.56/cgi-bin/local.py?x=docker%20ps")
    pyttsx3.speak("wordpress container is running....")

  elif("list" in ch) or ("Cgi" in ch) or ("bin" in ch) :
    wb.open("http://192.168.29.56/cgi-bin/local.py?x=ls")
    pyttsx3.speak("these are the files present in CGI BIN...")

  elif("JDK" in ch) or ("java jdk" in ch) and ("java" in ch):
    wb.open("http://192.168.29.56/cgi-bin/local.py?x=rpm%20-q%20jdk1.8")
    pyttsx3.speak("java jdk is not present...")
  elif("hadoop" in ch) or ("aadoop" in ch):
    wb.open("http://192.168.29.56/cgi-bin/local.py?x=rpm%20-q%20hadoop")
    pyttsx3.speak("hadoop is not present...")
  elif("setup java" in ch) or ("install java" in ch) or ("configure java jdk" in ch):
    wb.open("http://192.168.29.56/cgi-bin/local.py?x=rpm%20-ivh%20jdk-8u171-linux-x64.rpm")
    pyttsx3.speak("java jdk is successfully installed...")
  elif("install hadoop" in ch) or ("setup aadoop" in ch) or ("configure hadoop" in ch):
    wb.open("http://192.168.29.56/cgi-bin/local.py?x=rpm%20-ivh%20 hadoop-1.2.1-1.x86_64.rpm%20--force")
    pyttsx3.speak("hadoop is successfully installed...")
  elif("create" in ch) or ("directory" in ch):
    wb.open("http://192.168.29.56/cgi-bin/local.py?x=mkdir%20/namenode")
    pyttsx3.speak("directory created")
  elif("setup or start" in ch) or ("namenode" in ch) or ("masternode" in ch):
    wb.open("http://192.168.29.56/cgi-bin/local.py?x=hadoop-daemon.sh%20start%20namenode")
    pyttsx3.speak("name node started")
  elif("report" in ch) or ("dfs" in ch) or ("admin" in ch):
    wb.open("http://192.168.29.56/cgi-bin/local.py?x=hadoop%20dfsadmin%20-report")
    pyttsx3.speak("here is the report of hadoop cluster")
  elif("SDK" in ch) or ("python library" in ch):
    wb.open("http://192.168.29.56/cgi-bin/local.py?x=pip3%20install%20boto3")
    pyttsx3.speak("boto three is already satisfied")
  elif("aws" in ch) or ("CLI" in ch) or ("command line" in ch):
    wb.open("http://192.168.29.56/cgi-bin/local.py?x=pip3%20install%20awscli")
    pyttsx3.speak("AWS CLI is already satisfied")
  elif("provision" in ch) or ("ec2" in ch) or ("instance" in ch):
    wb.open("http://192.168.29.56/cgi-bin/local.py?x=python3%20ec2.py")
    pyttsx3.speak("OS is successfully provisioned")
  elif("hping3" in ch) or ("establish" in ch):
    wb.open("http://192.168.29.56/cgi-bin/local.py?x=yum%20install%20hping3%20-y")
    pyttsx3.speak("H ping three is successfully installed")  
  elif("user" in ch) or ("mickey" in ch):
    wb.open("http://192.168.29.56/cgi-bin/local.py?x=useradd%20mickey")
    pyttsx3.speak("mickey user has been created")  
  elif("restrict" in ch) or ("addy" in ch):
    wb.open("http://192.168.29.56/cgi-bin/local.py?x=useradd%20-s%20/usr/bin/cal%20addy")
    pyttsx3.speak("aaditya user has been created and restricted") 
  elif ("exit" in ch) or ("quit" in ch) or ("bye" in ch):
    pyttsx3.speak("see you soon,, have a nice day...!!!")
    break
  else:
    print("Sorry didnt get you!!")
