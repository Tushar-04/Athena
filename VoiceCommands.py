import speech_recognition as sr 
import pyttsx3
import wolframalpha

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

engine.setProperty('rate', 180)


def speak(audio):
	engine.say(audio)
	engine.runAndWait()


def takeCommand():
	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language ='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		print(e)
		print("Unable to Recognize your voice.")
		return "None"
	
	return query


def wolfarmAlpha (query):
	client = wolframalpha.Client("JPJPHQ-U7455W96LL")
	res = client.query(query)
	try:
			print (next(res.results).text)
			speak(next(res.results).text)
	except StopIteration:
			print ("No results")