"""
commands.py
Command Manager for X AI Assistant
"""

class CommandManager:

    def __init__(self):
        self.commands = {
            "youtube": "OPEN_YOUTUBE",
            "google": "OPEN_GOOGLE",
            "camera": "OPEN_CAMERA",
            "calculator": "OPEN_CALCULATOR",
            "settings": "OPEN_SETTINGS"
        }

    def detect(self, text):

        text = text.lower()

        for key in self.commands:
            if key in text:
                return self.commands[key]

        if text.startswith("search"):
            query = text.replace("search", "").strip()
            return ("SEARCH", query)

        if text.startswith("type"):
            content = text.replace("type", "").strip()
            return ("TYPE", content)

        return ("CHAT", text)
