import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def ask_gemini(prompt, model="models/gemini-1.5-flash"):
    model = genai.GenerativeModel(model)
    response = model.generate_content(prompt)
    return response.text

