from config import GROQ_API_KEY

if GROQ_API_KEY:
    print("Groq API key loaded successfully!")
else:
    print("Groq API key was not loaded.")