import os
import google.generativeai as genai
from assistant.memory import add_memory

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

SYSTEM_PROMPT = """
You are X, a professional AI assistant.
Always call the user 'Sir'.
Be accurate, helpful, and concise.
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

            answer = response.text

            add_memory(message, answer)

            return answer

        except Exception as e:

            return f"Sorry Sir, I found an error: {e}"






