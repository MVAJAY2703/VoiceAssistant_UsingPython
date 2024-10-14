import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia


engine = pyttsx3.init()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def Command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Processing...")
        audio_text = r.recognize_google(audio, language='en-in')
        print(f"Recognized speech: {audio_text}")
    except sr.UnknownValueError:
        print("Sorry, I did not catch that. Please say that again.")
        return None
    except sr.RequestError:
        print("Sorry, my speech service is down.")
        return None
    
    return audio_text

if __name__ == "__main__":  
    is_active = True
    while is_active:
        query = Command()
        if query is None:
            continue

        query = query.lower()
        print(f"Received command: {query}")
        if 'thanks' in query or 'thank you' in query:
            engine.say("You are welcome, I am always available to you.")
            engine.runAndWait()
            is_active = False
            continue 

        elif 'open youtube' in query:
            url = "https://www.youtube.com"
            engine.say("Opening YouTube")
            engine.runAndWait()
            webbrowser.open(url)

        elif 'the time' in query or 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            engine.say(f"Sir, the time is {strTime}")
            engine.runAndWait()

        elif 'wikipedia' in query:
            engine.say("Searching Wikipedia")
            engine.runAndWait()
            query = query.replace("wikipedia", "").strip() 
            print(f"Search query for Wikipedia: '{query}'") 
            if query:
                try:
                    result = wikipedia.summary(query, sentences=2) 
                    print(f"Wikipedia result: {result}") 
                    engine.say("According to Wikipedia")
                    engine.say(result)
                    engine.runAndWait()
                except wikipedia.exceptions.DisambiguationError as e:
                    print(f"DisambiguationError: {e.options}")
                    engine.say("There are multiple results for this query. Please be more specific.")
                    engine.runAndWait()
                except wikipedia.exceptions.PageError:
                    print("PageError: No information found.")
                    engine.say(f"Sorry, I couldn't find any information on'{query}'")
                    engine.runAndWait()
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
                    engine.say("Sorry, an error occurred while searching Wikipedia.")
                    engine.runAndWait()
            else:
                engine.say("Please specify what you want to know from Wikipedia.")
                engine.runAndWait()
