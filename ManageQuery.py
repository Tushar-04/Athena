import pyjokes
import subprocess
import webbrowser
import wikipedia
import pyjokes
import VoiceCommands as vc
import datetime
import time
import requests



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 4 and hour<12:
        vc.speak("Good Morning Sir !")
    elif hour>= 12 and hour<18:
        vc.speak("Good Afternoon Sir !")
    else:
        vc.speak("Good Evening Sir !")

    assname =("Athena 1 point o")
    vc.speak("I am your Assistant")
    vc.speak(assname)     
    

def proccesQuery(query,ch):
    if ('wikipedia' in query or "search" in query or "what is" in query or "who is" in query) and('on youtube' not in query and "on google" not in query) :
        vc.speak('Searching Wikipedia...')
        query = query.replace("on wikipedia", "")
        query = query.replace("search ", "")
        results = wikipedia.summary(query, sentences = 3)
        vc.speak("According to Wikipedia")
        print(results)
        vc.speak(results)
    
    elif 'exit' in query or "stop listing" in query:
        vc.speak("Thanks for giving me your time")
        exit()

    elif 'shutdown system' in query:
        vc.speak("Hold On a Sec ! Your system is on its way to shut down")
        subprocess.call('shutdown / p /f')
    elif "restart" in query:
        subprocess.call(["shutdown", "/r"])
    elif "hibernate" in query or "sleep" in query:
        vc.speak("Hibernating")
        subprocess.call("shutdown / h")
    elif "log off" in query or "sign out" in query:
        vc.speak("Make sure all the application are closed before sign-out")
        time.sleep(5)
        subprocess.call(["shutdown", "/l"])

    elif 'open google' in query:
        vc.speak("Here you go to Google\n")
        webbrowser.open_new_tab("google.com")
    
    elif 'on google' in query:
        query = query.replace("search ", "")
        query = query.replace("on google", "")
        vc.speak("Here you go to Google\n")
        webbrowser.open_new_tab("https://www.google.com/search?q="+query)

    elif 'open youtube' in query:
        vc.speak("Here you go to Youtube\n")
        webbrowser.open_new_tab("https://youtube.com")
    
    elif "open wikipedia" in query:
        webbrowser.open("wikipedia.com")
    
    elif 'on youtube' in query:
        query = query.replace("search ", "")
        query = query.replace("on youtube", "")
        vc.speak("Here you go to Youtube\n")
        webbrowser.open_new_tab("https://www.youtube.com/results?search_query="+query)
    
    elif 'joke' in query:
        vc.speak(pyjokes.get_joke())
    
    elif "weather" in query:
        api_key = "33507e541ae781813c832323b86ec6da"
        vc.speak(" City name ")
        if(ch==0):
            city_name=input("City name : ")
        else:
            city_name = vc.takeCommand()
        
        complete_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
        response = requests.get(complete_url)
        
        if response.status_code != "404":
            x = response.json()
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
            vc.speak(" Temperature (in kelvin unit) is " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) is "+str(current_pressure) +"\n humidity (in percentage) is " +str(current_humidiy) +"\n description is " +str(weather_description))
        else:
            vc.speak(" City Not Found ")
            print(" City Not Found ")
    
    elif "how are you" in query:
        vc.speak("I'm fine, glad you asked me that")
    
    elif "play video" in query or "play music":
        pass
    
    else:
        vc.wolfarmAlpha(query)