import webbrowser
import datetime

class CommandEngine:

    def execute(self, command):

        text = command.lower()

        if "open youtube" in text:
            webbrowser.open("https://www.youtube.com")
            return "Opening YouTube, Sir."

        elif "open google" in text:
            webbrowser.open("https://www.google.com")
            return "Opening Google, Sir."

        elif "open github" in text:
            webbrowser.open("https://github.com")
            return "Opening GitHub, Sir."

        elif "what time" in text:
            current = datetime.datetime.now().strftime("%I:%M %p")
            return f"The current time is {current}, Sir."

        elif "search" in text:
            query = text.replace("search", "").strip()
            webbrowser.open(
                f"https://www.google.com/search?q={query}"
            )
            return f"Searching Google for {query}, Sir."

        return None
