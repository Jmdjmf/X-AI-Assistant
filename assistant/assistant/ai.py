"""
ai.py
AI Engine for X AI Assistant
"""

class AIEngine:

    def __init__(self):
        self.name = "X"
        self.mode = "Professional"

    def reply(self, text):

        text = text.lower()

        if "hello" in text:
            return "Hello, Sir."

        elif "thank you" in text:
            return "You're welcome, Sir."

        elif "good morning" in text:
            return "Good morning, Sir."

        elif "good night" in text:
            return "Good night, Sir."

        else:
            return "I understood your message, Sir. I'm still learning and will improve as we continue developing me."
