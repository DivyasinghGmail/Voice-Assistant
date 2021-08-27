import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser 
import smtplib
import psutil
import pyjokes
import pyautogui
import os
import wolframalpha
import ctypes
import subprocess
import json
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import win32com.client as wincl
import pywhatkit as whatsapp


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id) 
engine.setProperty('rate',180)

#text to speech
def speak(audio):
  
   engine.say(audio)
   print(audio)
   engine.runAndWait()

def time():

   Time=datetime.datetime.now().strftime("%I:%M:%S")
   speak("current time is")
   speak(Time)

   def date():

    year = datetime.datetime.now().year
    month = datetime.datetime.now().month 
    date = datetime.datetime.now().day
    speak("current date is")
    print(date)
    print(month)
    print(year)
   
#to wishMe
def wishMe():

   hour = int(datetime.datetime.now().hour)
   if hour >= 6 and hour< 12:
      speak("good morning Mam!")
    
   elif hour >= 12 and hour < 18:
      speak("good afternoon Mam!")

   elif hour >= 18 and hour < 24:
      speak("good evening Mam!")
    
   else:
      speak("good night Mam!")
    
speak("Welcome mam!")
time()
wishMe()
speak("I am Voice Assistant mam!Please tell me how can i help you?")

#To convert voice into text
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
       print("Listening...")
       r.pause_threshold= 1
       audio = r.listen(source)

    try:
       print("Recognizing...")
       query = r.recognize_google(audio, language='en-US') 
       print(f"user said: {query}\n")
      
    except Exception as e:
       print(e)
       print(" say that again please.....")
       return "none"  
    return query

#to send email
def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('username@gmail.com','password')
    server.sendEmail('username@gmail.com',to,content)
    server.close()
    
def cpu():
    
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+usage)
    
    battery = psutil.sensors_battery()
    speak('battery is at')
    speak(battery.percent)

def joke():
    speak(pyjokes.get_joke())

def screenshot():
    img = pyautogui.screenshot()
    img.save('C:\\Users\\HP\\Desktop\\screenshot.png')

if __name__ == "__main__":
   
    while True:
        query = takeCommand().lower()
        # All the commands said by user will be
		# stored here in 'query' and will be
		# converted to lower case for easily
		# recognition of command

        if 'date' in query:
            date()

        elif 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query)
            speak("according to wikipedia")
            print(results)
            speak(results)
         
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("okay mam,opening youtube")

        elif 'open facebook'in query:
            webbrowser.open("facebook.com")
            speak("okay mam,opening facebook")

        elif 'open inatagram'in query:
            webbrowser.open("intagram.com")
            speak("okay mam,opening instagram")

        elif 'open whatsapp'in query:
            webbrowser.open("whatsapp.com")
            speak("okay mam,opening whatsapp")

        elif 'open twitter'in query:
            webbrowser.open("twiter.com")
            speak("okay mam,opening twiter")
        
        elif 'open linkedin'in query:
            webbrowser.open("linkedin.com")
            speak("okay mam,opening linkedin")

        elif 'open snapchat'in query:
            webbrowser.open("snapchat.com")
            speak("okay mam,opening snapchat")

        elif 'open pinterst'in query:
            webbrowser.open("pinterest.com")
            speak("okay mam,opening pinterest")

        elif 'open github'in query:
            webbrowser.open("github.com")
            speak("okay mam,opening github")

        elif 'open opera'in query:
            webbrowser.open("opera.com")
            speak("okay mam,opening opera")

        elif 'open ebay'in query:
            webbrowser.open("ebay.com")
            speak("okay mam,opening ebay")

        elif 'open office'in query:
            webbrowser.open("office.com")
            speak("okay mam,opening office")

        elif 'open netflix'in query:
            webbrowser.open("netflix.com")
            speak("okay mam,opening netflix")

        elif 'open spotify'in query:
            webbrowser.open("spotify.com")
            speak("okay mam,opening spotify")

        elif 'open bing'in query:
            webbrowser.open("bing.com")
            speak("okay mam,opening bing")

        elif 'open oracle'in query:
            webbrowser.open("oracle.com")
            speak("okay mam,opening oracle")

        elif 'open gmail'in query:
            webbrowser.open("gmail.com")
            speak("okay mam,opening gmail")

        elif 'open disney'in query:
            webbrowser.open("disney.com")
            speak("okay mam,opening disney")

        elif 'open cloud'in query:
            webbrowser.open("cloud.gmail.com")
            speak("okay mam,opening cloud")

        elif 'open dictionary'in query:
            webbrowser.open("dictionary.com")
            speak("okay mam,opening dictionary")

        elif 'open uber'in query:
            webbrowser.open("uber.com")
            speak("okay mam,opening uber")

        elif 'open yahoo'in query:
            webbrowser.open("yahoo.com")
            speak("okay mam,opening yahoo")

        elif 'open gmail'in query:
            webbrowser.open("gmail.com")
            speak("okay mam,opening gmail")

        elif 'open telegram'in query:
            webbrowser.open("telegram.com")
            speak("okay mam,opening telegram")

        elif 'open naukari'in query:
            webbrowser.open("naukari.com")
            speak("okay mam,opening naukari")

        elif 'open udemy'in query:
            webbrowser.open("udemy.com")
            speak("okay mam,opening udemy")

        elif 'open skype'in query:
            webbrowser.open("skype.com")
            speak("okay mam,opening skype")

        elif 'open qoura'in query:
            webbrowser.open("quora.com")
            speak("okay mam,opening quora")

        elif 'open snapdeal'in query:
            webbrowser.open("snapdeal.com")
            speak("okay mam,opening snapdeal yahoo")

        elif 'open amazon'in query:
            webbrowser.open("amazon.in")
            speak("okay mam,opening amazon")

        elif 'open stackoverflow'in query:
            webbrowser.open("stackoverflow.com")
            speak("okay mam,opening stackoverflow")

        elif 'open flipkart'in query:
            webbrowser.open("flipkart.com")
            speak("okay mam,opening flipkart")

        elif 'open myntra'in query:
            webbrowser.open("myntra.com")
            speak("okay mam,opening myntra")

        elif 'open zomato'in query:
            webbrowser.open("zomato.com")
            speak("okay mam,opening zomato")

        elif 'open swiggy'in query:
            webbrowser.open("swiggy.com")
            speak("okay mam,opening swiggy")

        elif ' search in chrome' in query:
            speak('what should I search?')
            search_Term = takeCommand().lower()
            wb.open("https://www.google.com/intl/en/chrome/"+search_term)
        
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("okay mam,opening google")

        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")
            speak("okay mam,opening wikipedia")

        elif 'open google drive' in query:
            webbrowser.open("drive.google.com")
            speak("okay mam,opening google drive")
         
        elif 'send a email' in query:
            try:
                speak("what should i say?")            
                content=takeCommand()

                #provide Receiver email address
                speak("who is the reciever?")
                Receiver = input("Enter Reciver's Email :")
                to = input()
                sendEmail(to, content)
                speak("Email has been sent !")
			
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'cpu' in query:
            cpu()
        
        elif 'battery' in query:
            battery()
       
        elif 'joke' in query:
            joke()

        elif 'screenshot' in query:
            speak("ok mam")
            screenshot()

        elif 'play music' in query:
            music_dir = 'E:\HP\musics'  
            songs = os.listdir(music_dir)
            speak('what should I play?')
            search_Term = takeCommand().lower()
            no = int(search_Term.replace('number'))
            os.startfile(os.path.join(music_dir,songs[no]))

        elif 'open notedpad' in query:
            notedpad = "C:\\WINDOWS\\system32\\notepad.exe"
            speak("okay mam,opening notepad...")
            os.startfile(notedpad)

        elif 'close notepad' in query:
            speak("okay mam,closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif 'open command prompt' in query:
            speak("okay mam,opening command prompt...")
            os.system("start cmd")

        elif 'close command prompt' in query:
            speak("okay mam, closing command prompt")
            os.system("taskkill /f /im cmd.exe")

        elif 'open dev' in query:
            dev = "C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe"
            speak("okay mam,opening dev...")
            os.startfile(dev)

        elif 'open turbo' in query:
            turbo = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Turbo C++\Turbo C++ 3.2."
            speak("opening turbo...")
            os.startfile(turbo)

        elif 'open Code' in query:
            Code = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("okay mam,opening Code ...")
            os.startfile(Code)

        elif 'open python' in query:
            python = "F:\\HP\\python 3.95"
            speak("okay mam,opening python...")
            os.startfile(python)

        elif 'open Pictures' in query:
            Pictures = "E:\HP"
            speak("okay mam,opening Pictures...")
            os.startfile(Pictures)

        elif 'open videos' in query:
            videos = "E:\HP"
            speak("okay mam,opening videos...")
            os.startfile(videos)
        
        elif 'open movies' in query:
            movies = "E:\HP"
            speak("okay mam,opening MOVIES...")
            os.startfile(movies)

        elif 'open Downloads' in query:
            speak("okay mam,opening Downloads ...")
            os.system("start Downloads")

        elif 'open screenshot' in query:
            movies = "C:\\Users\\HP\\Pictures"
            speak("okay mam,opening screenshot...")
            os.startfile(screenshot)

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your Ip address is {ip}")

        elif "write a notes" in query:
            speak("What should i write, Mam?")
            notes = takeCommand()
            file = open('notes.txt', 'w')
            speak("Mam, Should i include date and time")
            ans = takeCommand()
            if 'yes' in ans or 'sure' in ans:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(notes)
                speak('Done Taking Notes,Mam')
            else:
                file.write(notes)
		
        elif "show note" in query:
            speak("Showing Notes")
            file = open("notes.txt", "r")
            print(file.read())
            speak(file.read())

        elif 'calculate' in query:
            app_id = "5WVUH3-P3X5TYX7YK"
            client = wolframalpha.Client("5WVUH3-P3X5TYX7YK")
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif 'search' in query or 'play' in query:
			
            query = query.replace("search", "")
            query = query.replace("play", "")		
            webbrowser.open(query)

        elif "what is" in query or "who is" in query:
            # Use the same API key
            # that we have generated earlier
            client = wolframalpha.Client("5WVUH3-P3X5TYX7YK")
            res = client.query(query)

            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")

        elif "weather" in query:
            #use the same key
            client = wolframalpha.Client("5WVUH3-P3X5TYX7YK")
            res = client.query(query)
			
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")
            
        
        elif 'news' in query:
            try:
                jsonObj = urlopen("https://newsapiorg/v2/top-headlines?country=us&category=entertainment&apiKey=45dc90b641584bc9a3768b797e579b66")
                data = json.load(jsonObj)
                i = 1
                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')
				
                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description']+ '\nj')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                print(str(e))

        elif 'whatsapp' in query:
                whatsapp.sendwhatmsg("+19999999999","hi",0,0)

        elif "where is" in query:
                query = query.replace("where is", "")
                location = query
                speak("User asked to Locate"+location)
                webbrowser.open("https://www.google.co.in/maps/@26.0575234,83.1756084,15z" + location + "")

        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
                speak("Wait ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')

        elif "don't listen" in query or "stop" in query:
                speak("for how much time you want to stop from listening commands")
                a = int(takeCommand())
                time.sleep(a)
                print(a)

        elif 'empty recycle bin' in query:
                winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                speak("Recycle Bin Recycled")

        elif "restart" in query:
                subprocess.call(["shutdown", "/r"])
			
        elif "hibernate" in query or "sleep" in query:
                speak("Hibernating")
                subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
                speak("Make sure all the application are closed before sign-out")
                time.sleep(5)
                subprocess.call(["shutdown", "/l"])
 
        elif 'hello' in query:
            speak("Hello Mam")
        
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Mam?")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "who i am" in query:
            speak("If you talk then definitely you r human.")

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Dibya.")
       
        elif "who are you" in query:
            speak("I am your voice assistant created by dibya")

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()