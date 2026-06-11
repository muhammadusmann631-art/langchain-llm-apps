import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# Gemini model select karo
model = genai.GenerativeModel("gemini-2.5-flash")

# Prompt bhejna
response = model.generate_content("web is vercel")

# Output print karna
print(response.text)
