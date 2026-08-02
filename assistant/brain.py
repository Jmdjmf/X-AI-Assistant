"""
brain.py
Professional Brain for X AI Assistant
"""

class Brain:

    def __init__(self):

        self.name = "X"
        self.version = "1.0"

    def think(self, command):

        command = command.lower().strip()

        # Greetings
        if command in ["hello", "hi", "hey"]:
            return "Hello, Sir. How may I assist you?"

        # Identity
        elif "who are you" in command:
            return "I am X, your personal AI assistant, Sir."

        # Health
        elif "how are you" in command:
            return "I'm functioning perfectly, Sir."

        # Time
        elif "time" in command:
            from datetime import datetime
            return "Sir, the current time is " + datetime.now().strftime("%I:%M %p")

        # Date
        elif "date" in command:
            from datetime import datetime
            return "Today's date is " + datetime.now().strftime("%d %B %Y")

        # Open YouTube
        elif "youtube" in command:
            return "Opening YouTube, Sir."

        # Open Google
        elif "google" in command:
            return "Opening Google, Sir."

        # Search
        elif command.startswith("search"):
            query = command.replace("search", "").strip()
            return f"Searching for {query}, Sir."

        # Stop
        elif command in ["stop", "exit", "quit"]:
            return "Goodbye, Sir."

        # Unknown
        else:
            return "I'm still learning, Sir. I didn't understand that command."
