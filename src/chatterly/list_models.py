import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("AIzaSyDmqemE0beuWIwX75E4HVTtCAlLUtcIf4c"))

for m in genai.list_models():
    print(m.name)
