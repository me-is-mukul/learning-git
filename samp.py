import os
from dotenv import load_dotenv
import google.generativeai as genai
import pyttsx3
load_dotenv()

def speak(text):
    # Initialize engine
    engine = pyttsx3.init()
    
    # Set properties (optional)
    engine.setProperty("rate", 150)   # Speed (words per minute)
    engine.setProperty("volume", 1.0)  # Volume (0.0 to 1.0)
    
    # Speak the text
    engine.say(text)
    engine.runAndWait()


key = os.getenv("API_KEY")

genai.configure(api_key=key)


model = genai.GenerativeModel("gemini-1.5-flash")


response = model.generate_content("make a poem")
speak(response.text)





