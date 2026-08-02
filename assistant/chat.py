import google.generativeai as genai
from config.api_keys import GEMINI_API_KEY


class ChatEngine:

    def __init__(self):

        genai.configure(api_key=GEMINI_API_KEY)

        self.model = genai.GenerativeModel("gemini-2.5-flash")

        self.chat = self.model.start_chat(history=[])

    def reply(self, message):

        try:

            response = self.chat.send_message(message)

            return response.text

        except Exception as e:

            return f"Sorry Sir, I found an error: {e}"
