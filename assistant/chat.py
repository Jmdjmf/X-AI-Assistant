"""
chat.py
Chat Engine
"""

from config.api_keys import OPENAI_API_KEY, GEMINI_API_KEY


class ChatEngine:

    def __init__(self):
        self.name = "X"

    def reply(self, message):

        message = message.strip()

        if not message:
            return "Please say something, Sir."

        if OPENAI_API_KEY:
            return "Sir, OpenAI connection will be added next."

        if GEMINI_API_KEY:
            return "Sir, Gemini connection will be added next."

        return "Sir, no AI API key has been configured yet."
