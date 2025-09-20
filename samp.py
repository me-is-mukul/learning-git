import os
from dotenv import load_dotenv
import google.generativeai as genai
import pyttsx3
import speech_recognition as sr
load_dotenv()

r = sr.Recognizer()

def speak(text):
    engine = pyttsx3.init()

    engine.setProperty("rate", 150)   
    engine.setProperty("volume", 1.0) 

    engine.say(text)
    engine.runAndWait()


key = os.getenv("API_KEY")

genai.configure(api_key=key)


model = genai.GenerativeModel("gemini-1.5-flash")


# response = model.generate_content("make a poem")
# speak(response.text)

# with sr.Microphone() as source:
#     print("🎙️ Speak something...")
#     #r.adjust_for_ambient_noise(source)   # optional (reduces background noise)
#     audio = r.listen(source, timeout=5, phrase_time_limit=10)

# try:
#     # Recognize using Google Speech Recognition (free, online)
#     text = r.recognize_google(audio)
#     print("You said:", text)

# except sr.UnknownValueError:
#     print("Sorry, I could not understand your speech.")
# except sr.RequestError:
#     print("Could not request results, check your internet connection.")



print(sr.Microphone.list_microphone_names())



