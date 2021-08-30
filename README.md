# Voice-Assistant



![Voice assistant](https://user-images.githubusercontent.com/86322884/131216316-f59cb832-0d42-4a89-aaee-57d843960f18.png)



A voice assistant or intelligent personal assistant is a software agent that can perform tasks or services for an individual based on verbal commands.
Voice assistant service built with python using Visual studio. It can understand human speech and perform basic task designed by the client.

Voice assistant:"Loading your personal Assistant.... Hello, Good Morning" (Greets the user according to time),you can ask your assistant’ questions, media playback via voice, and manage other basic tasks such as email, to-do lists, open or close any application etc with verbal commands.

In this repository I provide a step by step tutorial on building a voice assistant using python.
Simple voice-based desktop/laptop assistant that has the capability to:

* Open the subreddit in the browser.

* Open any website in the browser.

* Send an email to your contacts.

* Launch any system application.

* Tells you the current weather and temperature of almost any city.

* Tells you the current time.

* Greetings.

* Play you a song on VLC media player(of course you need to have VLC media player installed in your laptop/desktop).

* Tells you latest news feeds.

* Tells you about almost anything you ask.

* Supports two different user input modes (text or speech), user can write or speek in the mic.

* Answers in general questions (via call Wolfram API), e.g (' tell me the highest building')

The implemented Voice assistant can perform the following tasks:

1.Opens a wepage : Youtube , G-Mail , Google Chrome , StackOverflow, twitter, facebook etc.

  user : Open Youtube
 
2.Predicts time

  user : What is the time
 
3.Fetch Top headlines from Times of India

  user: what's the latest news?

4.Searches data from web

  user: Search Butterfly images from web

5.Ask geographical and computational questions

  user: What is the capital of California? / what is Sin 90?
 
6.Predict Weather of different Cities

  user: What is the weather likely now in Kerala?

7.Abstarct necessary information from wikipedia

  user: Who is Bill Gates according to Wikipedia
 The voice assistant abstarcts first 3 lines of wikipedia and gives the information to the user.
 
8.Ask about what task it can perform and who created it

  user: Who is Bill Gates according to Wikipedia
 
10.Turn off your pc when required

  user: Please turn off my PC
   
Getting Started

Create KEYs for third party APIs
Voice assistant uses third party APIs for speech recognition,web information search, weather forecasting etc. All the following APIs have free no-commercial API calls. Subscribe to the following APIs in order to take FREE access KEYs.

OpenWeatherMap: API for weather forecast.

WolframAlpha: API for answer questions.

NewsAPI: API for latest news.

Libraries required to be installed using Pip Command:

1.request

Requests: Requests is used for making GET and POST requests. To install this module type the below command in the terminal.

pip install requests

2.Speech recognition

Speech Recognition:- Since we’re building an Application of voice assistant, one of the most important things in this is that your assistant recognizes your voice (means what you want to say/ ask). To install this module type the below command in the terminal.It allow us to convert audio into text for further processing. To install this module type the below command in the terminal.
 
pip install SpeechRecognition

3.Pyttsx3

pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.pyttsx is a cross-platform text to speech library which is platform independent. The major advantage of using this library for text-to-speech conversion is that it works offline. To install this module type the below command in the terminal

pip install pyttsx3

If you recieve errors such as No module named win32com.client, No module named win32, or No module named win32api, you will need to additionally install pypiwin32.

Usage :
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()

4.Wikipedia

Wikipedia:- As we all know Wikipedia is a great source of knowledge, we have used the Wikipedia module to get information from Wikipedia or to perform a Wikipedia search. To install this module type the below command in the terminal

pip install wikipedia

5.Pyjokes:- Pyjokes is used for collection Python Jokes over the Internet. To install this module type the below command in the terminal.

pip install pyjokes

6.Wolfram Alpha

WolframAlpha:- It is used to compute expert-level answers using Wolfram’s algorithms, knowledgebase and AI technology. To install this module type the below command in the terminal.
 
pip install wolframaplha

In-Built libraries required to be imported:

1.datetime

Datetime:- Date and Time is used to showing Date and Time. This module comes built-int with Python

2.web browser

Web browser:- To perform Web Search. This module comes built-in with Python.It provides a high-level interface which allows displaying Web-based documents to users. To install this module type the below command in the terminal.

pip install webbrowser

3.subprocess

Subprocess:- This module is used for getting system subprocess details which are used in various commands i.e Shutdown, Sleep, etc. This module comes built-in with Python.

Methodology

* You can use any IDE like Anaconda, Visual Studio etc.

* So the first step is to create a function for a voice which has arguments. Also, we are using Speech API to take voice as input. There are two defaultvoices in our computer I.e. Male and Female. So you can use either any from these. Also, check the voice function by giving some text input and it will beconverted into voice.

* You can create a new function for wishing the user. Use if_else condition statement for allocating the wished output.
E.g. If its time between 12 to 18 then the system will say “Good Evening”. Along with this, you can get a welcome voice also. E.g. “Welcome, How may I help you.

* After that, you have to install the speech recognition model and then import it.

* Define a new function for taking command from a user. Also mention class for speech recognition and input type like microphone etc. Also mention pause_threshold.

* Set a query for voice recognition language. You can use Google engine to convert your voice input to the text.

* You have to install and import some other packages like pyttsx3, Wikipedia etc. Pyttsx3 helps you to convert text input to speech conversion. • If you ask for any information then it will display the result in textual format. You can convert it very easily in the voice format as we have already defined a function in our code previously.

* Else you ask to open YouTube in the query then it will go to the YouTube address automatically. For that, you have to install a web browser package and import it.

* In the same way, you can add queries for many websites like Google, Instagram, Faceboo, stackoverflow etc.

* The next task is to play the songs. It is same as you have done before. Add a query for “play songs”. Also, add the location of songs folder so that assistant will play the song from that only.

* So the main question is that how the queries work?…. So here we are using conditional statements. If the computer hears voice command which contains word youtube then it will go to the YouTube page address, if the voice contains google command then it will go to the Google search page and so
many accordingly.

* You can add so many pages and commands for your Voice assistant

Conclusion

Hope you liked our project where we created a voice assistant that can understand voice command using speech recognition in Python. We just showed you a prototype, but you can add as many creative features and functionalities as you require.

Happy reading:)

