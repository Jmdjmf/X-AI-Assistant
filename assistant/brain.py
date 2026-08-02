"""
brain.py
Brain Module for X AI Assistant
"""

class Brain:

    def __init__(self):
        self.name = "X"
        self.version = "1.0"
        self.status = "Ready"

    def think(self, command):

        command = command.lower()

        if "hello" in command:
            return "Hello, Sir! How can I help you today?"

        elif "who are you" in command:
            return "I am X, your personal AI assistant, Sir."

        elif "how are you" in command:
            return "I'm functioning perfectly, Sir."

        elif "bye" in command:
            return "Goodbye, Sir. Have a wonderful day."

        else:
            return "I'm sorry, Sir. I don't understand that command yet."
