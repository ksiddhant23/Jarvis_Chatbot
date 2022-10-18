import pyttsx3, random, sys, webbrowser, pafy, wikipedia, requests, pyautogui, os   #pip install pyttsx3
from urllib.request import urlopen
import pyjokes as pj
from bs4 import BeautifulSoup as bs
import speech_recognition as sr     #pip install speech_recognition
from datetime import datetime
from requests import get

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 188)

def speak(audio):
    print("Jarvis : - ",audio)
    engine.say(audio)
    engine.runAndWait()
speak("Hi there")

d=datetime.now().strftime("%A:%d:%B:%Y")

def myCommand():
    print("Listening...")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=0.6)
        audio = r.listen(source,phrase_time_limit=5)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print("Master: - " + query)

    except sr.UnknownValueError:
        query = myCommand()
    
    except sr.RequestError:
        query = myCommand()

    except sr.WaitTimeoutError:
        query = myCommand()

    return str(query).lower()


def greetMe():
    currentH = int(datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning Master!')

    elif currentH >= 12 and currentH < 18:
        speak('Good Afternoon Master!')

    elif currentH >= 18 and currentH !=0:
        speak('Good Evening Master!')

if __name__ == "__main__":
    greetMe()

    while 1:
        query = myCommand()
        
        if 'hello' in query or 'hi ' in query or "hey" in query or "get up" in query:
            speak(random.choice(["I'm in",'Hello sir','Hi boss','At your service Sir','I\'m up']))

        elif 'bye' in query or "exit" in query or 'see you later' in query or "close everything" in query:
            speak(random.choice(['Bye Sir, have a good day.','Love you boss!','I will be missing you!!','Bye Sir! Love you']))
            print("     👋")
            print("Exiting...")
            sys.exit()

        elif "on youtube" in query:
                ssc = query.split("search for")[-1]
                search_term = ssc.split("on youtube")[0]
                url = "https://www.youtube.co.in/results?search_query=" + search_term
                speak("Here is what I found for " + search_term + " on youtube")
                webbrowser.get().open(url)

        elif 'locate' in query or "where is" in query:
                if "where is" in query:
                    pl=query.split("where is ")[-1]
                else:
                    pl=query.split("locate ")[-1]
                speak("Locating " + pl)
                speak("Just a second")
                webbrowser.open("https://www.google.co.in/maps/place/"+pl+"/")
                speak("Here is " + pl + " on map")
        
        elif "game" in query:
                speak("choose among rock paper or scissor")
                moves=["rock", "paper", "scissor"]
                cmove=random.choice(moves)
                Pmove=myCommand().lower()
                pmove=Pmove.lower()
                speak("I chose " + cmove)
                speak("You chose " + pmove)
                if "rock" in pmove == cmove == "rock":
                    speak("The match is draw")
                elif "scissor" in pmove == cmove== "scissor":
                    speak("The match is draw")
                elif "paper" in pmove == cmove== "paper":
                    speak("The match is draw")
                elif "rock" in pmove and cmove== "scissor":
                    speak("You won")
                elif "rock" in pmove and cmove== "paper":
                    speak("I won")
                elif "paper" in pmove and cmove== "rock":
                    speak("You won")
                elif "paper" in pmove and cmove== "scissor":
                    speak("I won")
                elif "scissor" in pmove and cmove== "paper":
                    speak("You won")
                elif "scissor" in pmove and cmove== "rock":
                    speak("I won")
                else:
                    speak("Wrong choice!")

        elif "toss a coin" in query:
                moves=["head", "tail"]   
                cmove=random.choice(moves)
                speak("I chose " + cmove + " for you ")
          

        elif "roll a dice" in query:
            moves=["1","2","3","4","5","6"]   
            cmove=random.choice(moves)
            speak("I got " + cmove + " for you on dice")

        elif "capture" in query or "my screen" in query or "take a screenshot" in query or "what's on my screen" in query or "take screenshot" in query:
                myScreenshot = pyautogui.screenshot()
                strTime = datetime.now().strftime("%H_%M_%S")
                myScreenshot.save('screenshot'+strTime+'.png')
                speak("Screenshot done")
                speak("Here's the screenshot")
                os.startfile('screenshot'+d+'.png')

        elif 'joke' in query or "jokes" in query:
                try:
                    speak(pj.get_joke('en','all'))
                except:
                    res = get('https://icanhazdadjoke.com/',headers={"Accept":"application/json"})
                    if res.status_code == requests.codes.ok:
                        speak(str(res.json()['joke']))
                    else:
                        speak('Oops! I ran out of jokes')

        elif "definition of" in query or 'define' in query:
                try:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak(results)
                except:
                    speak("Sorry, I wasn't able to find the definition")

        elif "search for " in query:
                ssc = query.split("search for ")[-1]
                url = "https://google.co.in/search?q=" + ssc
                speak("Here is what I found for " + ssc + " on google")
                webbrowser.get().open(url)

        #time & date
        elif 'the time' in query or 'time now' in query:
            strTime = datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        
        elif "the date" in query or "today's date" in query:
            dateT=datetime.now().strftime("%B:%d:%A:%Y")
            speak("Today's date is "+dateT)
        
        #Internet
        elif 'news' in query or 'news feeds' in query or 'get me news' in query:
            speak(random.choice(["Here are the top five news of the day","Here's your latest news",'Just a second']))
            try:
                news_url=get("https://news.google.com/news/rss").content
                soup_page=bs(news_url,"lxml")
                news_list=soup_page.findAll("item")
                for news in news_list[:5]:
                    speak(news.title.text)
                speak("These were the top headlines, Have a nice day Sir!!..")
            except Exception as e:
                speak("An Error Occurred")
        else:
            speak("I don't know the answer to your query yet!!")

