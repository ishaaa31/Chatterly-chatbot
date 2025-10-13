import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(model_name="models/gemini-pro-latest")

def generate(prompt: str, system_prompt: str = None) -> str:
    """
    Generates a response using Gemini with optional system prompt.
    """
    try:
        parts = []
        if system_prompt:
            parts.append(system_prompt)
        parts.append(prompt)

        response = model.generate_content(parts)
        return response.text
    except Exception as e:
        return f"[Gemini Error] {str(e)}"
