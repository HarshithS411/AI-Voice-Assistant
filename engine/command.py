import pyttsx3
import speech_recognition as sr
import eel
def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.setProperty('rate',170)
    print(voices)
    engine.say( text)
    engine.runAndWait()
    
    
import eel
import speech_recognition as sr

@eel.expose
def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening...')
        eel.DisplayMessage('Listening...')  # Display message on the frontend
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=6)
        except Exception as e:
            print("Error capturing audio:", e)
            eel.DisplayMessage("Error capturing audio.")
            return ""

    try:
        print('Recognizing...')
        eel.DisplayMessage('Recognizing...')  # Display message on the frontend
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        eel.DisplayMessage(query)  # Display recognized text on the frontend
        speak(query)
    except sr.UnknownValueError:
        eel.DisplayMessage("Could not understand audio.")
        return ""
    except sr.RequestError:
        eel.DisplayMessage("Speech recognition service is unavailable.")
        return ""
    except Exception as e:
        print("An error occurred:", e)
        eel.DisplayMessage("An error occurred during recognition.")
        return ""

    return query.lower()
