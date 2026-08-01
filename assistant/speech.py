"""
speech.py
Voice Recognition Module for X AI Assistant
"""

class SpeechEngine:

    def __init__(self):
        self.status = "Idle"

    def start(self):
        self.status = "Listening"
        print("🎤 X is listening...")

    def stop(self):
        self.status = "Stopped"
        print("🛑 X stopped listening.")

    def get_status(self):
        return self.status
