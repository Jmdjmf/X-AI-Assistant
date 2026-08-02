"""
chat.py
AI Chat Engine
"""

import requests


class ChatEngine:

    def __init__(self):
        self.name = "X"
        self.version = "1.0"

    def reply(self, message):

        message = message.strip()

        if message == "":
            return "Please say something, Sir."

        return f"I understood: {message}\nSir, our online AI engine will be connected in the next step."
