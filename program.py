import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjust the speech rate if needed

# Set the voice to the first available voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Change index for different voice (0 for male, 1 for female)

def Command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Processing...")
        audio_text = r.recognize_google(audio, language='en-in')
        print(f"You said: {audio_text}")
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

        if 'open youtube' in query:
            url = "https://www.youtube.com"
            engine.say("Opening YouTube")
            engine.runAndWait()
            webbrowser.open(url)

        elif 'the time' in query or 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            engine.say(f"Sir, the time is {strTime}")
            engine.runAndWait()

        elif 'thanks' in query or 'thank you' in query:
            engine.say("you are welcome i am always available to you ")
            engine.runAndWait()
            is_active = False
        