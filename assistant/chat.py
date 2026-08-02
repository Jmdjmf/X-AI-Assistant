import os
import google.generativeai as genai

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

SYSTEM_PROMPT = """
You are X, a professional AI assistant.
Your name is X.
Be friendly, intelligent, and helpful.
Give clear and accurate answers.
"""

class ChatEngine:
    def __init__(self):
        self.model = genai.GenerativeModel(
            "models/gemini-3.5-flash",
            system_instruction=SYSTEM_PROMPT
        )

        self.chat = self.model.start_chat(history=[])

    def reply(self, message):
        try:
            response = self.chat.send_message(message)
            return response.text
        except Exception as e:
            return f"Sorry, I found an error: {e}"






