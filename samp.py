import google.generativeai as genai

genai.configure(api_key="AIzaSyDiYFvfGtswXQ0hthizIz72kOkYxYx_ics")


model = genai.GenerativeModel("gemini-1.5-flash")


response = model.generate_content("make a shayri.")
print(response.text)
