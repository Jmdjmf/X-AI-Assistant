import os
import google.generativeai as genai

# Configure Gemini using the environment variable
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))


class ChatEngine:
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-2.5-flash")
        self.chat = self.model.start_chat(history=[])

    def reply(self, message):
        try:
            response = self.chat.send_message(message)
            return response.text
        except Exception as e:
            return f"Sorry Sir, I found an error: {e}"
