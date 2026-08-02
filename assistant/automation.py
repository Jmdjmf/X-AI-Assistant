"""
automation.py
Automation Module for X AI Assistant
"""

import webbrowser


class Automation:

    def __init__(self):
        self.status = "Ready"

    def open_youtube(self):
        print("Opening YouTube, Sir...")
        webbrowser.open("https://www.youtube.com")

    def open_google(self):
        print("Opening Google, Sir...")
        webbrowser.open("https://www.google.com")

    def search_google(self, query):

        print(f"Searching Google for '{query}', Sir...")

        url = "https://www.google.com/search?q=" + query.replace(" ", "+")

        webbrowser.open(url)

    def search_youtube(self, query):

        print(f"Searching YouTube for '{query}', Sir...")

        url = "https://www.youtube.com/results?search_query=" + query.replace(" ", "+")

        webbrowser.open(url)

    def open_website(self, url):

        webbrowser.open(url)

    def type_text(self, text):

        print("Typing feature will be added in the Android version.")

    def get_status(self):

        return self.status
